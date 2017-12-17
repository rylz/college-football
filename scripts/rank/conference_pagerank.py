#!/usr/bin/python
__doc__ = """Rank conferences based on whole season and postseason results.

Uses pagerank both with and without a victory margin consideration, and prints results to console.

"""

import argparse

import cfb

def report_pagerank(games):
    conf_pr = cfb.rank.pagerank.ConferencePagerank(games)
    conf_pr.compile()
    conf_pr_margin = cfb.rank.pagerank.ConferencePagerank(games, margin_of_victory=True)
    conf_pr_margin.compile()

    print('  Without Margin-of-Victory Weighting')
    for i, (conference_id, pr) in enumerate(sorted(conf_pr.pr, key=lambda t: t[1], reverse=True)):
        conf = cfb.team.conference_name(conference_id)
        rank = i+1
        print(f'    {rank:2}. {conf} ({pr:.3})')

    print('  With Margin-of-Victory Weighting')
    for i, (conference_id, pr) in enumerate(sorted(conf_pr_margin.pr, key=lambda t: t[1], reverse=True)):
        conf = cfb.team.conference_name(conference_id)
        rank = i+1
        print(f'    {rank:2}. {conf} ({pr:.3})')

if __name__ == '__main__':
    # Command line parameters
    parser = argparse.ArgumentParser(
            description='Predict bowl outcomes given season results')
    parser.add_argument('-y', '--year', action='store', type=int, required=True)
    args = parser.parse_args()

    all_games = [cfb.game.Game(g) for g in cfb.game.lookup(year=args.year)
            if cfb.game.Game(g).team_stats]
    post_games = [cfb.game.Game(g) for g in cfb.game.lookup(year=args.year, week=20)
            if cfb.game.Game(g).team_stats]

    if all_games:
        print(f'{args.year} Entire Season Conference Ranking:')
        report_pagerank(all_games)

    if post_games:
        print(f'{args.year} Bowl Season Conference Ranking:')
        report_pagerank(post_games)
