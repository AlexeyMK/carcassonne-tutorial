from collections import namedtuple

# clockwise order
TileEdges = namedtuple('TileEdges', 'north east south west')

class Tile:
  def __init__(self, edges):
    """ edges = namedtuple w/ four keys: {north, east, south, west}
        w/ values of: R (road), C ('city'), F (field)
        (+ A (available) and ' '(blank)
    """
    self.edges = edges

  def __str__(self):
    """initial implementation, in 3 rows"""
    return " {north} \n{west} {east}\n {south} ".format(**self.edges._asdict())

  @classmethod
  def empty(self):
    return Tile.new('    ')

  @classmethod
  def new(cls, edge_str):
    """ cleaner shorthand for a new tile - give 4 characters for neighbors
        in clockwise order (N, E, S, W)
        For example, the starting piece is Tile.new("CRFR")"""
    return Tile(TileEdges(*edge_str))

STARTING_PIECE = Tile.new('CRFR')

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
      # since we have three rows and we're still relying on print,
      # displaying gets a bit dirty
      # will get cleaner once we move to something like HTML
      row_tiles = [self.board.get((x, y), Tile.empty())
        for x in xrange(min_x, max_x + 1)]

      # now we have to print each of the three rows together.
      # zip to aggregate each of the top, middle, bottom rows
      row_lines = zip(*[str(tile).split("\n") for tile in row_tiles])
      for line in row_lines:
        print "".join(line)

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
  b.board[(1, 0)] = Tile.new('RFFF')
  b.board[(1, 1)] = Tile.new('FFFF')
  for tile in b.available_spots():
    b.board[tile] = Tile.new('AAAA') # available tile
  b.display()

if __name__ == '__main__':
  __test__()
