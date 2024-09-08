from pygraph.classes.directed_graph import DirectedGraph
from . import pygraph_pagerank

import cfb

class _Pagerank(cfb.ranking.Ranking):
  """Abstract class for shared logic between pagerank methods."""

  def __init__(self, games, eligible=None, node_fn=None, weight_fn=lambda g: 1):
    """Setup initial state, but do not compute rank yet.

    games is a list of cfb.game.Game objects whose results will decide
    direction of edges in the pagerank graph.

    eligible, if provided, is a list of entities that are eligible to be ranked.
    It is only used as a filter on the final output - e.g. FCS teams may be
    excluded, but they can still pass and receive pagerank in the algorithm.

    node_fn is a function that takes a Game object and returns keys for the
    winning and losing entites. If not provided, we just use the team_ids. But
    for example, this could allow us to rank by conference, division, or schools
    with bird mascots vs. mammals.

    weight_fn is a function that takes a Game object and returns an interger to
    use as an edge weight for that game. By default, everything gets weight 1,
    but this can be used to assign more importance to certain games or reward
    margin of victory.

    Note that most of these ranking by common characteristics like conference
    won't currently work since we're using a pagerank that doesn't support
    edge weights or multiple edges between the same pair of nodes.

    """
    self.games = games
    self.eligible = eligible
    self.node_fn = node_fn
    self.weight_fn = weight_fn
    # pr eventually contains tuples of (entity id, pagerank value), but
    # we don't compute it on initialization to allow more flexibility in when
    # that computation runs.
    self.pr = None

  def compile(self):
    # build the digraph
    gr = DirectedGraph()
    for game in self.games:
      winner, loser = self.node_fn(game)
      if not gr.has_node(winner):
        gr.add_node(winner)
      if not gr.has_node(loser):
        gr.add_node(loser)
      if winner == loser:
        # possible in implementations where node_fn returns non-unique data
        # like conferences
        continue

      if not gr.has_edge((loser, winner)):
        gr.add_edge((loser, winner), wt=self.weight_fn(game))
      else:
        wt = gr.edge_weight((loser, winner))
        gr.del_edge((loser, winner))
        gr.add_edge((loser, winner), wt=wt+self.weight_fn(game))

    self.pr = pygraph_pagerank.pagerank(gr).items()
    if self.eligible:
      self.pr = filter(lambda item: item[0] in self.eligible, self.pr)

  def get_teams(self, limit=25):
    if not self.pr:
      self.compile()

    return [
      t for t, score in
      sorted(self.pr, key=lambda item: item[1], reverse=True)[:limit]]


class TeamPagerank(_Pagerank):
  """Rank all teams based on wins/losses with no weighting on e.g. margin."""
  def __init__(self, games, eligible=None, margin_of_victory=False):
    if margin_of_victory:
      super(TeamPagerank, self).__init__(
        games, eligible=eligible,
        node_fn=lambda game: (game.winner(), game.loser()),
        weight_fn=lambda game: game.team_stats[game.winner()]['points'] -
            game.team_stats[game.loser()]['points'])
    else:
      super(TeamPagerank, self).__init__(
        games, eligible=eligible,
        node_fn=lambda game: (game.winner(), game.loser()))


class ConferencePagerank(_Pagerank):
  """Rank all conferences based on wins/losses with no weighting on e.g. margin."""
  def __init__(self, games, eligible=None, margin_of_victory=False):
    if margin_of_victory:
      super(ConferencePagerank, self).__init__(
        games, eligible=eligible,
        node_fn=lambda game: (cfb.team.Team(game.winner()).conference_id, cfb.team.Team(game.loser()).conference_id),
        weight_fn=lambda game: game.team_stats[game.winner()]['points'] -
            game.team_stats[game.loser()]['points'])
    else:
      super(ConferencePagerank, self).__init__(
        games, eligible=eligible,
        node_fn=lambda game: (cfb.team.Team(game.winner()).conference_id, cfb.team.Team(game.loser()).conference_id))
