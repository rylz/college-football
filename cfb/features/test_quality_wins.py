import unittest

import cfb


class TestQualityWins(unittest.TestCase):
  def test_wins_over_top25(self):
    # TODO better way to manage this
    cfb.config.DB_NAME = 'cfb_test'
    away_team1 = cfb.team.add_team('Away School', 'Fighting Travelers', 1)
    away_team2 = cfb.team.add_team('Away School 2', 'Surrendering Travelers', 1)
    away_team3 = cfb.team.add_team('Away School 3', 'White Flags', 1)
    home_team = cfb.team.add_team('Home School', 'Where the Heart Is', 1)
    # the home team managed to play 3 games at the same time!
    cfb.game.add_game(2015, 2, away_team1, home_team, 21, 17, 1447619829)
    cfb.game.add_game(2015, 2, away_team2, home_team, 0, 17, 1447619829)
    cfb.game.add_game(2015, 2, away_team3, home_team, 0, 77, 1447619829)
    # TODO assertion time


if __name__ == '__main__':
  # TODO use nosetests instead
  unittest.main()
