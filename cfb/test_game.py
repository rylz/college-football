import unittest

import cfb


class TestGame(unittest.TestCase):
  def setup(self):
    # TODO better way to manage this
    cfb.config.DB_NAME = 'cfb_test'
    cfb.db.query('DELETE FROM team_nickname')
    cfb.db.query('DELETE FROM game')
    cfb.db.query('DELETE FROM team_game_stats')
    self.away_team = cfb.team.add_team('Away School', 'Fighting Travelers', 1, nicknames=['Away'])
    self.home_team = cfb.team.add_team('Home School', 'Where the Heart Is', 1, nicknames=['Home'])
    self.game_id = cfb.game.add_game(
      2015, 2, self.away_team, self.home_team, 21, 17, 1447619829)

  def test_summary(self):
    self.setup()
    game_obj = cfb.game.Game(self.game_id)
    self.assertEqual(
      '21 Away @ Home 17',
      game_obj.summary)
    self.assertEqual(
      self.away_team,
      game_obj.winner())
    self.assertEqual(
      self.home_team,
      game_obj.loser())

    # TODO test for scheduled but not completed game

  def test_lookup(self):
    self.setup()
    game_id2 = cfb.game.add_game(
        2015, 3, self.home_team, self.away_team, 21, 17, 1447619830)
    self.assertEqual(
      [self.game_id, game_id2],
      cfb.game.lookup()
    )
    self.assertEqual(
      [self.game_id, game_id2],
      cfb.game.lookup(year=2015)
    )
    self.assertEqual(
      [self.game_id],
      cfb.game.lookup(year=2015, week=2)
    )
    self.assertEqual(
      [game_id2],
      cfb.game.lookup(year=2015, week=3)
    )
    self.assertEqual(
      [self.game_id],
      cfb.game.lookup(home_team=self.home_team)
    )
    self.assertEqual(
      [game_id2],
      cfb.game.lookup(home_team=self.away_team)
    )
    self.assertEqual(
      [self.game_id, game_id2],
      cfb.game.lookup(either_team=self.home_team)
    )


if __name__ == '__main__':
  # TODO use nosetests instead
  unittest.main()
