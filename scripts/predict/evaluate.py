#!/usr/bin/python

import click

from collections import defaultdict

import cfb

cli = click.Group()

@cli.command()
@click.option('--year', '-y', type=int, required=True, help='year')
@click.option('--week', '-w', type=int, required=True, help='week')
def evaluate(year, week):
    predictions = cfb.game.get_predictions(year, week)
    model_predictions = defaultdict(dict)
    # NB: ignoring prediction model version
    for prediction_model, _, game_id, away_points, home_points in predictions:
        model_predictions[prediction_model][game_id] = (away_points, home_points)
    games = cfb.game.lookup(year=year, week=week)

    model_evaluations = {model: defaultdict(int) for model in model_predictions}
    for game_id in games:
        game = cfb.game.Game(game_id)
        away_points = game.team_stats[cfb.game.Game(game_id).game_info['away_team']]['points']
        home_points = game.team_stats[cfb.game.Game(game_id).game_info['home_team']]['points']
        for model in model_predictions:
            if game_id in model_predictions[model]:
                predicted_away, predicted_home = model_predictions[model][game_id]
                wl_correct = (home_points > away_points) == (predicted_home > predicted_away)
                if wl_correct:
                    model_evaluations[model]['wl_correct'] += 1

                else:
                    model_evaluations[model]['wl_incorrect'] += 1

                # spread
                vegas_spread =  game.spread
                if vegas_spread:
                    actual_spread = away_points - home_points
                    predicted_spread = predicted_away - predicted_home
                    spread_correct = (round(predicted_spread * 2 - vegas_spread * 2) > 0) == (round(actual_spread * 2 - vegas_spread * 2) > 0)
                    if spread_correct:
                        model_evaluations[model]['beat_spread'] += 1
                    else:
                        model_evaluations[model]['lost_spread'] += 1

                # over-under
                vegas_over_under =  game.over_under
                if vegas_over_under:
                    actual_over_under = away_points + home_points
                    predicted_over_under = predicted_away + predicted_home
                    over_under_correct = (round(predicted_over_under * 2 - vegas_over_under * 2) > 0) == (round(actual_over_under * 2 - vegas_over_under * 2) > 0)
                    if over_under_correct:
                        model_evaluations[model]['beat_over_under'] += 1
                    else:
                        model_evaluations[model]['lost_over_under'] += 1

                print(f"{game.summary}:")
                print(f"  Predicted: {predicted_away}-{predicted_home} (correct={wl_correct})")
                if vegas_spread:
                    print(f"  Spread: {game.spread} (correct={spread_correct})")
                if vegas_over_under:
                    print(f"  Over-Under: {game.over_under} (correct={over_under_correct})")

    print(model_evaluations)
    return model_evaluations


@cli.command()
@click.option('--year', '-y', type=int, required=True, help='year')
@click.pass_context
def evaluate_whole_season(ctx, year):
    model_evaluations = {
        m: {
            'wl_correct': 0,
            'wl_incorrect': 0,
            'beat_spread': 0,
            'lost_spread': 0,
            'beat_over_under': 0,
            'lost_over_under': 0,
        }
        for m in [1,2,3,4]
    }
    for week in range(3, 15):
        week_evaluations = ctx.invoke(evaluate, year=year, week=week)
        print(week_evaluations.keys())
        for m in model_evaluations:
            for k in model_evaluations[m]:
                model_evaluations[m][k] += week_evaluations[m][k]

    print(model_evaluations)

if __name__ == '__main__':
    cli()
