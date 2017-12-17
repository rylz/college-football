__doc__ = """Model for historical rankings.

For ranking algorithms, see rank/. This only allows recall and comparison of existing rankings.

"""

import cfb

class ranking_type:
  ap_poll = 1
  coach_poll = 2
  playoff_committee = 3


class Ranking(object):
  """Interface to allow comparison of various ranking methods."""
  def get_teams(self, limit=25):
    raise NotImplementedError()


class HistoricalRanking(Ranking):
  def __init__(self, ranking_type, year, week):
    self.ranking_type = ranking_type
    self.year = year
    self.week = week

  def get_teams(self, limit=25):
    """Gets a ranked list of teams, from top to bottom.

    Returns a list of tuples formatted (team_id, rank, points).

    """
    sql = '''
      SELECT team, rank, points FROM ranking
      WHERE
        ranking_type_id = %s AND
        year = %s AND
        week = %s
      ORDER BY rank DESC LIMIT %s
    '''
    params = (self.ranking_type, self.year, self.week, limit)

    return list(cfb.db.query(sql, params))


def compare_ranking_ranks(ranking1, ranking2):
  """A measure of the difference between two rankings using only the ranks.

  All teams not present in one ranking, but present in the other, are treated
  as if they were tied for last.

  Order doesn't matter - will always return a nonnegative value.

  """
  diff = 0
  ranking_map1 = {team_id: rank for team_id, rank, _ in ranking1.get_teams()}
  ranking_map2 = {team_id: rank for team_id, rank, _ in ranking2.get_teams()}

  for team_id, rank in ranking_map1.items():
    diff += abs(rank - ranking_map2.get(team_id, len(ranking_map2)))

  # account for any teams in the second ranking that weren't in the first
  for team_id, rank in ranking_map2.items():
    if team_id not in ranking_map1:
      diff += len(ranking_map1) - rank

  return diff


def add_ranking(ranking_type, year, week, data):
  """Add ranking data to the database.

  ranking_type should be one of the values in the ranking_type enum.

  year should be an integer representing what season the data comes from.

  week should be an integer indicating the week, where 0 means preason.

  data should be a list of tuples
    (team_id, rank, points)
  where team_id refers to the integer ID assigned to each team in the database.

  """
  sql = 'INSERT INTO ranking (ranking_type_id, year, week, team, rank, points) VALUES\n'
  sql += cfb.db.sql_lists([
    (ranking_type, year, week, team_id, rank, points)
    for team_id, rank, points in data
  ])
  cfb.db.query(sql)
