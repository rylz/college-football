# college-football
Schema, data model, and scripts for analyzing college football data

This is intended to be a general schema and data model that is usable for any analysis you might like to do on college football data. It currently includes scripts to do:
* Regressions (linear and random forest) to predict game scores
* Ranking conferences with PageRank
* Comparisons of different rankings of teams, for use in evaluating ranking predictors

The repository does not include data for game results and past rankings - only static data for teams and their conferences. I'm still uncertain of the best way to share this data - as a SQL dump, CSV with an import script, or something else. If you would like to work with this code and my data before I post the data, let me know and I can share it with you.

Dependencies:
* Python 3
* Beautiful Soup 4
* https://github.com/pmatiello/python-graph
* mysqlclient
