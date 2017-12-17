from . import base
import cfb

class _WinsOverX(base.Feature):
  def __init__(self, year, team_id):
    self.year = year
    self.team_id = team_id

  @property
  def value(self):
    val = 0
    for game in cfb.game.team_games_of_season(self.year, self.team_id):
      if game.winner() == self.team_id and self.condition(game.loser()):
        val += 1
    return val

  def condition(self, opponent_id):
    """Stub to implement the condition that defines which wins are quality."""
    raise NotImplementedError()


class WinsOverTop25(_WinsOverX):
  @property
  def ranking(self):
    return cfb.ranking.get_most_recent(
      cfb.ranking.ranking_type.ap_poll, year=self.year)

  def condition(self, opponent_id):
    return opponent_id in self.ranking


class WinsOverTeamsWithWinningRecords(_WinsOverX):
  def condition(self, opponent_id):
    opponent_season = cfb.game.team_games_of_season(self.year, opponent_id)
    opponent_wins = sum(int(g.winner() == opponent_id) for g in opponent_season)
    return opponent_wins * 2 >= len(opponent_season)


class WinsOverFCSTeams(_WinsOverX):
  def condition(self, opponent_id):
    return cfb.team.Team(opponent_id).conference_id == cfb.team.conference.fcs
