class Player:

  def __init__(self, status):
      self.name = status[0]
      self.points = int(status[1])
  def __repr__(self):
        return repr((self.name, self.points))
  def sortPoints (self):
    return self.points