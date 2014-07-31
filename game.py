STARTING_PIECE = 'A'

class Board:
  def __init__(self):
    """ starting tile is 0,0 - the rest are offset from the starting tile"""
    self.board = {}  # dict of (x,y) to PlacedTile
    self.board[(0,0)] = STARTING_PIECE

  def display(self):
    horizontal_bounds, vertical_bounds = self.get_bounds()
    min_x, max_x = horizontal_bounds
    min_y, max_y = vertical_bounds

    # xrange is inclusive in start and exclusive in end, IE [s..e)
    # so we add +1 offset to be safe
    for y in xrange(min_y, max_y + 1):
      for x in xrange(min_x, max_x + 1):
        print self.board.get((x, y), '.'),
      print'\n',

  def get_bounds(self):
    """ returns a tuple of tuples ((x_min, x_max), (y_min, y_max)) """
    board_keys = self.board.keys()
    min_x = min(p[0] for p in board_keys)
    max_x = max(p[0] for p in board_keys)
    min_y = min(p[1] for p in board_keys)
    max_y = max(p[1] for p in board_keys)
    return ((min_x, max_x), (min_y, max_y))

def __test__():
  print("before")
  b = Board()
  b.board[(-2, -2)] = 'X'
  b.board[(-3, -0)] = 'Y'
  b.board[(4, 1)] = 'Z'
  b.display()
  print("after")

if __name__ == '__main__':
  __test__()
