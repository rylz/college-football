import time

from enum import Enum

import cfb

class Game(object):
  def __init__(self, game_id):
    self.game_id = game_id

  @property
  def game_info(self):
    return _get_game(self.game_id)

  @property
  def team_stats(self):
    return _get_game_team_stats(self.game_id)

  @property
  def summary(self):
    """Returns a string summarizing the outcome of a played game, or the
    timing of a scheduled one."""
    summary = '%s @ %s' % (
      cfb.team.Team(self.game_info['away_team']).nickname,
      cfb.team.Team(self.game_info['home_team']).nickname,
    )

    away_stats = self.team_stats.get(self.game_info['away_team'])
    home_stats = self.team_stats.get(self.game_info['home_team'])
    if away_stats and home_stats:
      summary = '%d %s %d' % (
        away_stats['points'], summary, home_stats['points'])
    else:
      summary = '%s (%s)' % (
        summary, time.strftime('%Y-%m-%d %H:%M'))
    return summary

  def winner(self):
    """Returns the winning team's id."""
    # TODO support ties for historic games
    return max((stats['points'], team_id) for team_id, stats in self.team_stats.items())[1]

  def loser(self):
    """Returns the losing team's id."""
    # TODO support ties for historic games
    return min((stats['points'], team_id) for team_id, stats in self.team_stats.items())[1]

  @property
  def series(self):
    """Returns the name of the associated series, if any."""
    return _get_series(_get_game_series(self.game_id))['series_name']

  @property
  def spread(self):
    """Returns the spread for the home team, if available."""
    return _get_spread(self.game_id)

  @property
  def over_under(self):
    """Returns the total over under for the game, if available."""
    return _get_over_under(self.game_id)


def _get_game(game_id):
  """Gets game summary.

  Returns a dictionary with keys
    'year'
    'week'
    'away_team' as an id
    'home_team' as an id
    'kickoff_time' as a unix timestamp in UTC, if available

  For results, see _get_game_team_stats.

  """
  sql = '''
    SELECT year, week, away_team, home_team, kickoff_time
    FROM game
    WHERE game_id = %s
  '''
  params = (game_id,)
  results = cfb.db.query(sql, params)[0]

  return {
    'year': results[0],
    'week': results[1],
    'away_team': results[2],
    'home_team': results[3],
    'kickoff_time': results[4],
  }


def _get_game_series(game_id):
  """Gets the list of series this game belongs to.

  Returns a list of series_ids.

  """
  sql = '''
    SELECT series_id
    FROM series_game
    WHERE game_id = %s
  '''
  params = (game_id,)
  return cfb.db.query(sql, params)[0]


def _get_game_team_stats(game_id):
  """Gets game result.

  Returns a dictionary
    {team_id: {
      'points'
      'total_yards'
      'top'}
    }
  with both teams' stats in a game, if available.

  """
  sql = '''
    SELECT team_id, points, total_yards, top
    FROM team_game_stats
    WHERE game_id = %s
  '''
  params = (game_id,)
  result = {}
  for row in cfb.db.query(sql, params):
    result[row[0]] = {
      'points': row[1],
      'total_yards': row[2],
      'top': row[3],
    }

  return result


def lookup(year=None, week=None, either_team=None, away_team=None, home_team=None):
  """Return a list of game_ids that match the specified data.

  If team is specified, it will match either home or away.

  """
  where_clauses = []
  params = []
  for name, value in [
      ('year', year), ('week', week), ('away_team', away_team), ('home_team', home_team)]:
    if value:
      where_clauses.append('%s = %%s' % name)
      params.append(value)
  if either_team:
    where_clauses.append('%s IN (home_team, away_team)')
    params.append(either_team)
  sql = 'SELECT game_id FROM game'
  if where_clauses:
      sql += ' WHERE ' + ' AND '.join(where_clauses)
  sql += ' ORDER BY kickoff_time ASC'
  return [row[0] for row in cfb.db.query(sql, tuple(params))]


def add_game(year, week, away_team, home_team, away_points=None, home_points=None, kickoff_time=None, series_id=None):
  """Add game result to the database.

  year should be an integer representing what season the data comes from.

  away_team and home_team should be integers indicating team ids in the db.

  week should be an integer indicating the week.

  If points are unspecified, this will be considered a "scheduled" future game.
  (TODO add a column to game table for states like this)

  kickoff time, if specified, should be a unix timestamp.

  """
  game_id = lookup(year, week, away_team=away_team, home_team=home_team)
  if game_id:
      game_id = game_id[0]
      # TODO update kickoff time if necessary
  else:
      sql = '''
        INSERT INTO game (year, week, away_team, home_team, kickoff_time) VALUES
        (%s, %s, %s, %s, %s)
      '''
      params = (year, week, away_team, home_team, kickoff_time)
      game_id = cfb.db.query(sql, params)

  if away_points is not None and home_points is not None:
      sql = '''
        REPLACE INTO team_game_stats (game_id, team_id, points) VALUES (%s, %s, %s)
      '''
      params = (game_id, away_team, away_points)
      cfb.db.query(sql, params)
      params = (game_id, home_team, home_points)
      cfb.db.query(sql, params)

  if series_id:
    sql = '''
      REPLACE INTO series_game (series_id, game_id) VALUES
      (%s, %s)
    '''
    params = (series_id, game_id)
    cfb.db.query(sql, params)

  return game_id


class series_type(object):
  bowl_game = 1
  conference_championship = 2
  rivalry = 3
  national_championship = 4
  playoff_semifinal = 5


def add_series(name, type, metadata=None):
  """Add a series type.

  Should be rarely used, as new series are not created very often.

  type should be one of the integers defined in series_type.

  metadata should be type-specific, e.g. a conference championship should use
  this field to specify the conference_id.
  TODO better define fields for each type

  """
  sql = '''
    INSERT INTO series (series_name, series_type, metadata) VALUES
    (%s, %s, %s)
  '''
  params = (name, type, metadata)
  return cfb.db.query(sql, params)


def lookup_series(name):
  """Return the id for a series name, if it exists."""
  sql = '''
    SELECT series_id
    FROM series
    WHERE
      series_name = %s
  '''
  params = (name,)
  result = cfb.db.query(sql, params)
  if len(result) == 1:
    return result[0][0]

  # TODO better way to index this
  # handle changing sponsorships by accepting names as substrings
  for series_id, series_name in cfb.db.query('SELECT series_id, series_name FROM series'):
    if series_name in name:
      return series_id


def _get_series(series_id):
  """Gets game summary.

  Returns a dictionary with keys
    'series_name'
    'series_type'
    'metadata' if available

  """
  sql = '''
    SELECT series_name, series_type, metadata
    FROM series
    WHERE
      series_id = %s
  '''
  params = (series_id,)
  results = cfb.db.query(sql, params)[0]

  return {
    'series_name': results[0],
    'series_type': results[1],
    'metadata': results[2],
  }


def team_games_of_season(year, team_id):
    sql = '''
        SELECT game_id
        FROM game
        WHERE
            %s in (away_team, home_team) AND
            year = %s
    '''
    return [Game(game_id) for game_id in cfb.db.query(sql, (team_id, year))]


class PredictionModelType(Enum):
  pagerank_rf = 1
  pagerank_rf_margin_of_victory = 2
  pagerank_rf_with_opp_ypg = 3
  pagerank_rf_margin_of_victory_with_opp_ypg = 4


def get_predictions(year, week):
  """Return a list of predictions for a given week.

  Returns a list of tuples:
    (prediction_model, prediction_model_version, game_id, away_points, home_points)."""
  sql = '''
    SELECT prediction_model, version, game.game_id, away_points, home_points
    FROM game_prediction
    NATURAL JOIN game
    WHERE
      year = %s AND
      week = %s
  '''
  params = (year, week)
  results = cfb.db.query(sql, params)

  return list(results)


def get_prediction(game_id, prediction_model, version=0):
  """Return a prediction for a given game and model.

  Returns a tuple (away_points, home_points)."""
  sql = '''
    SELECT away_points, home_points
    FROM game_prediction
    WHERE
      game_id = %s AND
      prediction_model = %s AND
      version = %s
  '''
  params = (game_id, prediction_model.value, version)
  result = cfb.db.query(sql, params)[0]

  return result


def save_predictions(prediction_data, prediction_model, version=0):
  """Save predictions for a given model.

  prediction_data should be a dict of the form:
    game_id: (away_points, home_points)
  """
  prediction_time = int(time.time())
  sql = '''
    INSERT INTO game_prediction (prediction_model, version, prediction_time, game_id, away_points, home_points)
    VALUES
  '''
  sql += ','.join(f'({prediction_model.value}, {version}, {prediction_time}, {game_id}, {away_points}, {home_points})'
      for game_id, (away_points, home_points) in prediction_data.items())
  cfb.db.query(sql)


class SportsBook(Enum):
  five_dimes = 24
  bovada = 25
  mybookieag = 29


def _get_spread(game_id, book=SportsBook.bovada):
  """Return the spread for a given game and sports book.

  Returns a single float home_spread."""
  sql = '''
    SELECT home_spread
    FROM game_odds
    WHERE
      game_id = %s AND
      book_id = %s
  '''
  params = (game_id, book.value)
  result = cfb.db.query(sql, params)
  if result:
      return result[0][0]


def _get_over_under(game_id, book=SportsBook.bovada):
  """Return the total over-under for a given game and sports book.

  Returns a single float over_under, or None if unavailable."""
  sql = '''
    SELECT over_under
    FROM game_odds
    WHERE
      game_id = %s AND
      book_id = %s
  '''
  params = (game_id, book.value)
  result = cfb.db.query(sql, params)
  if result:
      return result[0][0]


def record_odds(game_id, book_id, update_time, home_spread=None, over_under=None):
  """Record the odds for a given game and book.

  If any of the optional kwargs are left as None, we write NULL to the db.

  Note that update_time is not the time we wrote the update to the db, but the time the bookie
  updated these odds (so we can't just default to now).
  """
  assert update_time
  assert home_spread or over_under, "No use writing all NULLs to the db..."
  sql = '''
    REPLACE INTO game_odds (game_id, book_id, update_time, home_spread, over_under) VALUES
    (%s, %s, %s, %s, %s)
  '''
  params = (game_id, book_id, update_time, home_spread or None, over_under or None)
  cfb.db.query(sql, params)
