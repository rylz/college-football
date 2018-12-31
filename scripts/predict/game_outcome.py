#!/usr/bin/python
__doc__ = """Predict game outcomes given season results to date.

Uses team and conference pagerank differences, latest AP ranking differences, average points allowed
and gained to predict each team's points scored independently. Performs a simple regression on
regular season results using ranking to date as input.

"""

import argparse
from datetime import datetime
import random
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

import cfb

def compile_data(games, input_vector):
    """Organize data from game results into an input matrix and output vector.

    games is a list of Game objects whose data will be compiled.

    input_vector is a function mapping (team_id, opp_id) into the vector used for regression and
    prediction.

    Returns two parallel lists - the points array and the input matrix.

    """
    # parallel arrays for input/output
    points = []
    input_vectors = []
    for g in games:
        home = g.game_info['home_team']
        away = g.game_info['away_team']
        points.append(g.team_stats[home]['points'])
        points.append(g.team_stats[away]['points'])
        input_vectors.append(input_vector(home, away))
        input_vectors.append(input_vector(away, home))

    return (points, input_vectors)

MODELS = {
    'linear': LinearRegression,
    'rf': RandomForestRegressor,
}

if __name__ == '__main__':
    # Command line parameters
    parser = argparse.ArgumentParser(
            description='Predict game outcomes given season results to date')
    parser.add_argument('-y', '--year', action='store', type=int, required=True)
    parser.add_argument('-w', '--week', action='store', type=int, required=True)
    parser.add_argument(
            '-m', '--model', action='store', type=str, choices=MODELS.keys(), default='linear')
    parser.add_argument('-v', '--victorymargin', action='store_true')
    parser.add_argument('-d', '--depth', action='store', type=int)
    parser.add_argument('-l', '--leafsize', action='store', type=int)
    parser.add_argument('-s', '--stats_feature', action='store_true', help='Use team season stats as a model feature.')
    args = parser.parse_args()

    if args.depth or args.leafsize:
        assert args.model == 'rf', \
                'depth and leafsize are parameters for random forests only.'

    regular_season_game_ids = cfb.game.lookup(year=args.year)
    games = list(filter(
        lambda g: g.game_info['week'] < args.week, [cfb.game.Game(g) for g in regular_season_game_ids]))
    team_pr = cfb.rank.pagerank.TeamPagerank(games, margin_of_victory=args.victorymargin)
    team_pr.compile()
    team_pr = {team_id: pr for team_id, pr in team_pr.pr}
    conf_pr = cfb.rank.pagerank.ConferencePagerank(games)
    conf_pr.compile()
    conf_pr = {conf_id: pr for conf_id, pr in conf_pr.pr}
    latest_ap = {team_id: rank for team_id, rank, _ in cfb.ranking.HistoricalRanking(
        cfb.ranking.ranking_type.ap_poll, args.year, args.week - 1).get_teams()}

    test = random.sample(games, len(games)//10)
    train = list(set(games).difference(set(test)))

    def input_vector(team_id, opp_id):
        pr_diff = team_pr.get(team_id, 0) - team_pr.get(opp_id, 0)
        conf_pr_diff = conf_pr[cfb.team.Team(team_id).conference_id] - \
                conf_pr[cfb.team.Team(opp_id).conference_id] 
        ap_rank_diff = latest_ap.get(team_id, 26) - latest_ap.get(opp_id, 26)
        opp_points_allowed = cfb.features.points.PointsAllowedPerGame(args.year, opp_id).value
        ppg = cfb.features.points.PointsPerGame(args.year, team_id).value
        if not args.stats_feature:
            return (pr_diff, conf_pr_diff, ap_rank_diff, opp_points_allowed, ppg)

        opp_rypg = cfb.features.team_stats.SeasonYPG(args.year, opp_id, yard_type=cfb.features.team_stats.YardType.rushing).value
        opp_pypg = cfb.features.team_stats.SeasonYPG(args.year, opp_id, yard_type=cfb.features.team_stats.YardType.passing).value
        return (pr_diff, conf_pr_diff, ap_rank_diff, opp_points_allowed, ppg, opp_rypg, opp_pypg)

    kwargs = {}
    if args.depth:
        kwargs['max_depth'] = args.depth
    if args.leafsize:
        kwargs['min_samples_leaf'] = args.leafsize
    regr = MODELS[args.model](**kwargs)
    train_points, train_vectors = compile_data(train, input_vector)
    regr.fit(train_vectors, train_points)
    print("R^2 of training set:", regr.score(train_vectors, train_points))
    test_points, test_vectors = compile_data(test, input_vector)
    print("R^2 of test set:", regr.score(test_vectors, test_points))
    if args.model == 'rf':
        print("Feature importances:", regr.feature_importances_)

    predict_games = [cfb.game.Game(g) for g in cfb.game.lookup(year=args.year, week=args.week)]
    predict_vectors = []
    for g in predict_games:
        home = g.game_info['home_team']
        away = g.game_info['away_team']
        predict_vectors.append(input_vector(away, home))
        predict_vectors.append(input_vector(home, away))
    predict_points = regr.predict(predict_vectors)

    # summarize results
    def team_label(team_id):
        summary = ''
        if team_id in latest_ap:
            summary += f'#{latest_ap[team_id]} '
        summary += cfb.team.Team(team_id).nickname
        return summary

    game_predictions = {}
    for i, g in enumerate(predict_games):
        home = g.game_info['home_team']
        away = g.game_info['away_team']
        dt = datetime.fromtimestamp(g.game_info['kickoff_time'])
        print(team_label(away), predict_points[2*i])
        print(team_label(home), predict_points[2*i + 1])
        print()
        game_predictions[g.game_id] = (predict_points[2*i], predict_points[2*i + 1])

    # save predictions for certain models
    if args.model == 'rf':
        if args.victorymargin and args.stats_feature:
            prediction_model = cfb.game.PredictionModelType.pagerank_rf_margin_of_victory_with_opp_ypg
        elif not args.victorymargin and args.stats_feature:
            prediction_model = cfb.game.PredictionModelType.pagerank_rf_with_opp_ypg
        elif args.victorymargin:
            prediction_model = cfb.game.PredictionModelType.pagerank_rf_margin_of_victory
        else:
            prediction_model = cfb.game.PredictionModelType.pagerank_rf
        cfb.game.save_predictions(game_predictions, prediction_model)
