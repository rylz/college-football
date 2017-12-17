DROP TABLE IF EXISTS conference;
CREATE TABLE conference (
  conference_id TINYINT UNSIGNED NOT NULL PRIMARY KEY,
  name VARCHAR(32) NOT NULL
);

DROP TABLE IF EXISTS team;
CREATE TABLE team (
  team_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  conference_id TINYINT UNSIGNED NOT NULL,
  school VARCHAR(64) NOT NULL,
  mascot VARCHAR(32) NOT NULL
);

DROP TABLE IF EXISTS team_nickname;
CREATE TABLE team_nickname (
  nickname VARCHAR(32) NOT NULL PRIMARY KEY,
  team_id INT UNSIGNED NOT NULL REFERENCES team(team_id)
);

-- mappings from id spaces in other datasets into our id space
DROP TABLE IF EXISTS data_source;
CREATE TABLE data_source (
  data_source_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(32) NOT NULL
);

DROP TABLE IF EXISTS team_id_map;
CREATE TABLE team_id_map (
  data_source_id TINYINT UNSIGNED NOT NULL REFERENCES data_source(data_source_id),
  external_id VARCHAR(128) NOT NULL, -- string for flexibility; could be str representation of int
  team_id INT UNSIGNED NOT NULL REFERENCES team(team_id),
  PRIMARY KEY (data_source_id, external_id)
);

DROP TABLE IF EXISTS ranking_type;
CREATE TABLE ranking_type (
  ranking_type_id TINYINT UNSIGNED NOT NULL PRIMARY KEY,
  ranking_name VARCHAR(32) NOT NULL
);

DROP TABLE IF EXISTS player_position;
CREATE TABLE player_position (
    position_abbr CHAR(2) NOT NULL PRIMARY KEY,
    position_name VARCHAR(32) NOT NULL,
    position_group VARCHAR(32) NOT NULL,
    yahoo_id VARCHAR(16) NOT NULL,
    INDEX(position_group),
    INDEX(yahoo_id)
);

DROP TABLE IF EXISTS ranking;
CREATE TABLE ranking (
  ranking_type_id TINYINT UNSIGNED NOT NULL,
  year SMALLINT UNSIGNED NOT NULL,
  week TINYINT UNSIGNED NOT NULL,
  team INT UNSIGNED NOT NULL,
  rank TINYINT UNSIGNED NOT NULL,
  points INT UNSIGNED,
  final BOOL DEFAULT 0, -- is this the final week of the season?
  PRIMARY KEY (ranking_type_id, year, week, team)
);

-- game table contains all info about a game that could not be derived from
-- in-game statistics, i.e. all info that would be known AHEAD of time
DROP TABLE IF EXISTS game;
CREATE TABLE game (
  game_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  year SMALLINT UNSIGNED NOT NULL,
  week TINYINT UNSIGNED NOT NULL,
  -- following field not redundant; neutral site games, and home stadiums change
  -- stadium_id INT NOT NULL REFERENCES stadium(stadium_id),
  away_team INT UNSIGNED NOT NULL REFERENCES team(team_id),
  home_team INT UNSIGNED NOT NULL REFERENCES team(team_id),
  kickoff_time INT UNSIGNED -- unix timestamp (UTC)
);

-- annual series, like rivalries, championships, bowl games
DROP TABLE IF EXISTS series;
CREATE TABLE series (
  series_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  series_name VARCHAR(32) NOT NULL,
  series_type TINYINT NOT NULL,
  metadata TEXT
);

DROP TABLE IF EXISTS series_game;
CREATE TABLE series_game (
  series_id INT UNSIGNED REFERENCES series(series_id),
  game_id INT UNSIGNED REFERENCES game(game_id),
  PRIMARY KEY (series_id, game_id),
  KEY (game_id)
);

DROP TABLE IF EXISTS team_game_stats;
CREATE TABLE team_game_stats (
  game_id INT UNSIGNED NOT NULL REFERENCES game(game_id),
  team_id INT UNSIGNED NOT NULL REFERENCES team(team_id),
  points SMALLINT UNSIGNED NOT NULL,
  total_yards SMALLINT,
  top SMALLINT UNSIGNED, -- time of possession in seconds
  PRIMARY KEY (game_id, team_id)
);

-- player table can have multiple entries for the same human at different teams/positions
DROP TABLE IF EXISTS player;
CREATE TABLE player (
    player_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(32) NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    team_id INT UNSIGNED REFERENCES team(team_id),
    -- both years are "known so far" and can change as we get more info
    first_year INT UNSIGNED NOT NULL,
    last_year INT UNSIGNED NOT NULL,
    -- for now, only a primary position is supported
    position_abbr INT UNSIGNED REFERENCES player_position(position_abbr),
    uniform_number INT UNSIGNED
);

-- don't have most of this data yet, so many columns are aspirational :p
DROP TABLE IF EXISTS player_game_stats;
CREATE TABLE player_game_stats (
  game_id INT UNSIGNED NOT NULL REFERENCES game(game_id),
  player_id INT UNSIGNED NOT NULL REFERENCES player(player_id),
  points SMALLINT UNSIGNED,
  snap_count SMALLINT UNSIGNED,
  rush_attempts SMALLINT UNSIGNED,
  rush_yards SMALLINT,
  pass_attempts SMALLINT UNSIGNED,
  pass_yards SMALLINT,
  receptions SMALLINT UNSIGNED,
  recv_yards SMALLINT,
  tackles SMALLINT UNSIGNED,
  PRIMARY KEY (game_id, player_id)
);

-- play-by-play
DROP TABLE IF EXISTS play;
CREATE TABLE play (
  game_id INT UNSIGNED NOT NULL REFERENCES game(game_id),
  team_id INT UNSIGNED NOT NULL REFERENCES player(player_id),
  -- arbitrary seq id used for ordering plays; gaps are allowed but seq_ids must be unique per-game
  game_seq_id INT UNSIGNED NOT NULL,
  -- defined in code for now. denote things like "kickoff," "offensive play," etc.
  play_type TINYINT UNSIGNED NOT NULL,
  -- state at beginning of play
  quarter TINYINT UNSIGNED NOT NULL,
  down TINYINT UNSIGNED NOT NULL,
  togo TINYINT UNSIGNED NOT NULL,
  yards_to_endzone TINYINT UNSIGNED NOT NULL,
  -- number of seconds left in the quarter
  gameclock SMALLINT UNSIGNED NOT NULL,
  -- UTC time of play
  realtime INT UNSIGNED NOT NULL,
  yards_earned TINYINT UNSIGNED,
  PRIMARY KEY (game_id, team_id, game_seq_id)
);

-- NB: can have multiple actions per play, e.g. catch and run and fumble
DROP TABLE IF EXISTS player_play_action;
CREATE TABLE player_play_action (
  -- references play PK
  game_id INT UNSIGNED NOT NULL,
  team_id INT UNSIGNED NOT NULL,
  game_seq_id INT UNSIGNED NOT NULL,
  player_id INT UNSIGNED NOT NULL REFERENCES player(player_id),
  -- defined in code for now. denote things like "ran," "fumbled," etc.
  action_type TINYINT UNSIGNED NOT NULL,
  yards TINYINT UNSIGNED,
  PRIMARY KEY (game_id, team_id, game_seq_id, player_id)
);
