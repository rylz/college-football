import MySQLdb

import cfb

conn = None

def _get_connection():
  global conn
  if conn is None:
    conn = MySQLdb.connect(
        host=cfb.config.DB_HOST, user=cfb.config.DB_USER,
        passwd=cfb.config.DB_PASS, db=cfb.config.DB_NAME)
    conn.autocommit(1)
  return conn

def query(q, args=None):
  """For SELECT queries, returns an iterable of tuples of the results."""
  # TODO better error handling
  c = _get_connection().cursor()
  c.execute(q, args)
  if q.strip()[:6].lower() == 'select':
    return c.fetchall()
  else:
    return c.lastrowid


def sql_list(l):
  """Returns a string sql-formatted list for a python list."""
  # TODO sanitize
  return '(%s)' % ','.join([str(_) for _ in l])


def sql_lists(l):
  """Returns a string sql-formatted list of lists for a python list of lists."""
  return ','.join([sql_list(_) for _ in l])
