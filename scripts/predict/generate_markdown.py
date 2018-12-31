#!/usr/bin/python

import click

from collections import defaultdict

import cfb

@click.command()
@click.option('--year', '-y', type=int, required=True, help='year')
@click.option('--week', '-w', type=int, required=True, help='week')
def generate_markdown(year, week):
    predictions = cfb.game.get_predictions(year, week)
    model_predictions = defaultdict(dict)
    # NB: ignoring prediction model version
    for prediction_model, _, game_id, away_points, home_points in predictions:
        model_predictions[prediction_model][game_id] = (away_points, home_points)
    games = cfb.game.lookup(year=year, week=week)
    # TODO better handling for seasons with uncommon numbers of weeks
    final_ap = {team_id: rank for team_id, rank, _ in cfb.ranking.HistoricalRanking(
        cfb.ranking.ranking_type.ap_poll, year, 14).get_teams()}

    # summarize results
    def team_label(team_id):
        summary = ''
        if team_id in final_ap:
            summary += f'#{final_ap[team_id]} '
        summary += cfb.team.Team(team_id).nickname
        return summary

    win_results = defaultdict(list)
    for game_id in games:
        game = cfb.game.Game(game_id)
        for model in model_predictions:
            p = model_predictions[model].get(game_id)
            if p:
                win_results[model] += [
                        '{}{} {:.0f}{}<br>{}{} {:.0f}{}'.format(
                            '**' if p[0] > p[1] else '',
                            team_label(game.game_info['away_team']),
                            p[0],
                            '**' if p[0] > p[1] else '',
                            '**' if p[0] < p[1] else '',
                            team_label(game.game_info['home_team']),
                            p[1],
                            '**' if p[0] < p[1] else '')]

    win_results = win_results.items()
    print('| Bowl Game | ' + ' | '.join(str(model) for model, _ in win_results) + ' | Actual Result |')
    for i in range(len(games)):
        game = cfb.game.Game(games[i])
        game_result = ""
        if game.team_stats:
            away_points = game.team_stats[game.game_info['away_team']]['points']
            home_points = game.team_stats[game.game_info['home_team']]['points']
            game_result += '{}{} {:.0f}{}<br>{}{} {:.0f}{}'.format(
                '**' if away_points > home_points else '',
                team_label(game.game_info['away_team']),
                away_points,
                '**' if away_points > home_points else '',
                '**' if away_points < home_points else '',
                team_label(game.game_info['home_team']),
                home_points,
                '**' if away_points < home_points else '')

        print(f'| {cfb.game.Game(games[i]).series} | '  + ' | '.join(results[i] for _, results in win_results) + f' | {game_result} |')


if __name__ == '__main__':
    generate_markdown()
