from flask import Flask
from game import Board, Tile
app = Flask(__name__)

@app.route("/")
def hello():
  b = Board()
  b.board[(1, 1)] = Tile.new('FFFF')
  return "<pre>{}</pre>".format(b.display())

if __name__ == "__main__":
  app.run()
