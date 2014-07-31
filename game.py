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
    occupied_locations = self.board.keys()
    min_x = min(p[0] for p in occupied_locations)
    max_x = max(p[0] for p in occupied_locations)
    min_y = min(p[1] for p in occupied_locations)
    max_y = max(p[1] for p in occupied_locations)
    return ((min_x, max_x), (min_y, max_y))

  def available_spots(self):
    """ where on the board could a legal tile go?
      returns [(x,y)]
    """
    occupied_tiles = self.board.keys()
    neighbors = lambda x, y: ((x+1, y), (x-1, y), (x, y+1), (y, y-1))
    tiles_near_occupied = set(neighbor for tile in occupied_tiles
                                         for neighbor in neighbors(*tile))
    unnoccupied_titles_near_occupied = tiles_near_occupied - set(occupied_tiles)
    return unnoccupied_titles_near_occupied

def __test__():
  b = Board()
  b.board[(-1, -0)] = 'B'
  b.board[(-1, -1)] = 'C'
  b.board[(-1, 1)] = 'D'
  b.board[(-2, 0)] = 'E'
  for tile in b.available_spots():
    b.board[tile] = '~'
  b.display()

if __name__ == '__main__':
  __test__()
