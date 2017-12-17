class Feature(object):
  """Interface for ranking features.

  Only defines the need to provide a value for now.

  TODO define standard __init__ interface

  """
  @property
  def value(self):
    raise NotImplementedError()
