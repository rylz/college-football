import unittest

import cfb

class MockRanking(cfb.ranking.Ranking):
  """A test helper that only implements get_teams().

  Simply returns the provided object.

  """
  def __init__(self, get_teams_output):
    self.get_teams_output = get_teams_output

  def get_teams(self, limit=25):
    return self.get_teams_output[:25]


class TestCompareRanking(unittest.TestCase):
  def test_equality(self):
    ranking1 = MockRanking([
      (1, 1, 10),
      (5, 2, 1),
    ])
    self.assertEqual(0, cfb.ranking.compare_ranking_ranks(ranking1, ranking1))

  # TODO more test cases

if __name__ == '__main__':
  # TODO use nosetests instead
  unittest.main()
