class ConditionMismatchException(Exception):
  """
  """

  def __init__(self, message = 'condition dis not match', expected=None, actual=None):
    super(ConditionMismatchException, self).__init__()
    self.message = message
    if expected is not None:
      self.message += '''expected: {}'''.format(expected)
    if actual is not None:
      self.message += '''actual: {}'''.format(actual)
