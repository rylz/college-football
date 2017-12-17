import re

import cfb

class conference(object):
  fcs = 100


class Team(object):
  def __init__(self, team_id):
    self.team_id = team_id

  @property
  def nickname(self):
    return _get_nicknames(self.team_id)[0]

  @property
  def conference_id(self):
    return _get_team(self.team_id)['conference_id']

  @property
  def mascot(self):
    return _get_team(self.team_id)['mascot']


def _get_team(team_id):
  """Get a dictionary of basic team info.

  Returns a dict with keys
    'school'
    'mascot'
    'conference_id'

  """
  sql = '''
    SELECT school, mascot, conference_id
    FROM team
    WHERE team_id = %s
  '''
  params = (team_id,)
  result = cfb.db.query(sql, params)[0]
  return {
    'school': result[0],
    'mascot': result[1],
    'conference_id': result[2],
  }


def _get_nicknames(team_id):
  """Returns a list of all nicknames for a team."""
  sql = '''
    SELECT nickname
    FROM team_nickname
    WHERE team_id = %s
    UNION
    SELECT school
    FROM team
    WHERE team_id = %s
  '''
  params = (team_id, team_id)
  return [r[0] for r in cfb.db.query(sql, params)]


def add_team(school, mascot, conference_id, nicknames=None):
  """Add a team to the DB. Should be rarely used outside of tests."""
  sql = '''
    INSERT INTO team (school, mascot, conference_id)
    VALUES (%s, %s, %s)
  '''
  params = (school, mascot, conference_id)
  team_id = cfb.db.query(sql, params)
  nicknames = nicknames or []
  for nickname in nicknames:
    nickname = _canonicalize_nickname(nickname)
    add_nickname(team_id, nickname)
  return team_id


def add_nickname(team_id, nickname):
  sql = '''
    INSERT INTO team_nickname (nickname, team_id)
    VALUES (%s, %s)
  '''
  params = (nickname, team_id)
  cfb.db.query(sql, params)


def add_external_id(team_id, data_source, external_id):
    sql = """
        INSERT IGNORE INTO team_id_map (data_source_id, external_id, team_id)
        VALUES (
            (SELECT data_source_id FROM data_source WHERE name = %s),
                %s, %s)
    """
    if not lookup_external_id(data_source, external_id):
        result = cfb.db.query(sql, (data_source, external_id, team_id))


def _canonicalize_nickname(nickname):
  nickname = nickname.replace('St.', 'State')
  nickname = nickname.replace('Coll.', 'College')
  nickname = nickname.replace('W.', 'Western')
  nickname = nickname.replace('Cent.', 'Central')
  nickname = nickname.replace('East.', 'Eastern')
  nickname = nickname.replace('Wash.', 'Washington')
  nickname = re.sub('[^A-Za-z ()&]', ' ', nickname).strip()
  return nickname.lower()


def lookup(team_string):
  """Lookup a team_id from our DB given a string used to refer to them.

  The idea is to eventually build up a search index for all commonly used names
  for a team.

  Checks direct nickname matches (with some canonicalization) and partial school name matches.

  """
  nickname = _canonicalize_nickname(team_string)
  sql = '''
    SELECT team_id FROM team_nickname
    WHERE
      nickname = %s
    UNION
    SELECT team_id FROM team
    WHERE
      school LIKE %s
  '''
  args = (nickname, '%%%s%%' % team_string)
  results = cfb.db.query(sql, args)
  assert len(results) > 0, 'Query %s returned no results' % team_string
  return results[0][0]


def lookup_external_id(data_source, external_id):
    sql = """
        SELECT team_id
        FROM team_id_map NATURAL JOIN data_source
        WHERE
            name = %s AND
            external_id = %s
    """
    result = cfb.db.query(sql, (data_source, external_id))

    if result:
        return result[0][0]


def conference_name(conference_id):
  """Lookup the name for a conference id."""
  sql = '''
    SELECT name
    FROM conference
    WHERE conference_id = %s
  '''
  params = (conference_id,)
  return cfb.db.query(sql, params)[0][0]
