from flask import Flask
from game import Board, Tile, TileBag
app = Flask(__name__)

@app.route("/")
def hello():
  b = Board()
  b.board[(1, 1)] = Tile.new('FFFF')
  return display_text(b)

@app.route("/all-tiles")
def all_tiles():
  board = Board()
  bag = TileBag("tiles.csv")
  tile_count = len(list(bag.bag.elements()))
  tiles_per_side = int(tile_count ** .5) + 1  #sqrt round up
  for y in xrange(tiles_per_side):
    for x in xrange(tiles_per_side):
      tile = bag.draw()
      if tile:
        board.board[(x,y)] = tile

  return display_text(board)


def display_text(board):
  return "<pre>{}</pre>".format(board.display())

if __name__ == "__main__":
  app.run(debug=True)
