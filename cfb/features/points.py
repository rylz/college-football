from . import base
import cfb

class PointsAllowedPerGame(base.Feature):
    def __init__(self, year, team_id):
        self.year = year
        self.team_id = team_id

    @property
    def value(self):
        val = 0
        games = cfb.game.team_games_of_season(self.year, self.team_id)
        played_games = len(games)
        for game in games:
            if not game.team_stats:
                # game is schedules and hasn't been played yet
                played_games -= 1
                continue
            opponent = set(game.team_stats.keys()).difference(set([self.team_id])).pop()
            val += game.team_stats[opponent]['points']
        if len(games) == 0:
            return 0.0
        return float(val) / played_games


class PointsPerGame(base.Feature):
    def __init__(self, year, team_id):
        self.year = year
        self.team_id = team_id

    @property
    def value(self):
        val = 0
        games = cfb.game.team_games_of_season(self.year, self.team_id)
        played_games = len(games)
        for game in games:
            if not game.team_stats:
                # game is schedules and hasn't been played yet
                played_games -= 1
                continue
            val += game.team_stats[self.team_id]['points']
        if len(games) == 0:
            return 0.0
        return float(val) / played_games
