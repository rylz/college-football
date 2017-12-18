#!/usr/bin/python
__doc__ = """Predict bowl outcomes given season results.

Uses team and conference pagerank differences, final AP ranking differences, average points allowed
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
            description='Predict bowl outcomes given season results')
    parser.add_argument('-y', '--year', action='store', type=int, required=True)
    parser.add_argument(
            '-m', '--model', action='store', type=str, choices=MODELS.keys(), default='linear')
    parser.add_argument('-v', '--victorymargin', action='store_true')
    parser.add_argument('-d', '--depth', action='store', type=int)
    parser.add_argument('-l', '--leafsize', action='store', type=int)
    args = parser.parse_args()

    if args.depth or args.leafsize:
        assert args.model == 'rf', \
                'depth and leafsize are parameters for random forests only.'

    regular_season_game_ids = set(cfb.game.lookup(year=args.year)).difference(
            set(cfb.game.lookup(year=args.year, week=20)))
    games = [cfb.game.Game(g) for g in regular_season_game_ids]
    team_pr = cfb.rank.pagerank.TeamPagerank(games, margin_of_victory=args.victorymargin)
    team_pr.compile()
    team_pr = {team_id: pr for team_id, pr in team_pr.pr}
    conf_pr = cfb.rank.pagerank.ConferencePagerank(games)
    conf_pr.compile()
    conf_pr = {conf_id: pr for conf_id, pr in conf_pr.pr}
    # TODO better handling for seasons with uncommon numbers of weeks
    final_ap = {team_id: rank for team_id, rank, _ in cfb.ranking.HistoricalRanking(
        cfb.ranking.ranking_type.ap_poll, args.year, 14).get_teams()}

    test = random.sample(games, len(games)//10)
    train = list(set(games).difference(set(test)))

    def input_vector(team_id, opp_id):
        pr_diff = team_pr[team_id] - team_pr[opp_id]
        conf_pr_diff = conf_pr[cfb.team.Team(team_id).conference_id] - \
                conf_pr[cfb.team.Team(opp_id).conference_id] 
        ap_rank_diff = final_ap.get(team_id, 26) - final_ap.get(opp_id, 26)
        opp_points_allowed = cfb.features.points.PointsAllowedPerGame(args.year, opp_id).value
        ppg = cfb.features.points.PointsPerGame(args.year, team_id).value
        return (pr_diff, conf_pr_diff, ap_rank_diff, opp_points_allowed, ppg)

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

    bowl_games = [cfb.game.Game(g) for g in cfb.game.lookup(year=args.year, week=20)]
    predict_vectors = []
    for g in bowl_games:
        home = g.game_info['home_team']
        away = g.game_info['away_team']
        predict_vectors.append(input_vector(away, home))
        predict_vectors.append(input_vector(home, away))
    predict_points = regr.predict(predict_vectors)

    # summarize results
    def team_label(team_id):
        summary = ''
        if team_id in final_ap:
            summary += f'#{final_ap[team_id]} '
        summary += cfb.team.Team(team_id).nickname
        return summary

    for i, g in enumerate(bowl_games):
        home = g.game_info['home_team']
        away = g.game_info['away_team']
        dt = datetime.fromtimestamp(g.game_info['kickoff_time'])
        print(f'{g.series} ({dt.month}/{dt.day}):')
        print(team_label(away), predict_points[2*i])
        print(team_label(home), predict_points[2*i + 1])

    # finally, determine the national championship matchup and predict it!
    if predict_points[-4] > predict_points[-3]:
        rose_bowl_winner = bowl_games[-2].game_info['away_team']
    else:
        rose_bowl_winner = bowl_games[-2].game_info['home_team']
    if predict_points[-2] > predict_points[-1]:
        sugar_bowl_winner = bowl_games[-1].game_info['away_team']
    else:
        sugar_bowl_winner = bowl_games[-1].game_info['home_team']
    predict_vectors = [
            input_vector(rose_bowl_winner, sugar_bowl_winner),
            input_vector(sugar_bowl_winner, rose_bowl_winner)]
    predict_points = regr.predict(predict_vectors)
    print('National Championship')
    print(team_label(rose_bowl_winner), predict_points[0])
    print(team_label(sugar_bowl_winner), predict_points[1])
