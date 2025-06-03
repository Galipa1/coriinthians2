from flask import Flask, request, jsonify
from graph import Graph
from dijkstra import Dijkstra
from utils import Utils

app = Flask(__name__)

@app.post("/move")
def move():
    data = request.get_json()
    ctx = Utils.parse_context(data)

    direction = ctx.find_move()

    return jsonify({"move": direction})


@app.get("/ping")
def ping():
    return "pong"


@app.get("/")
def index():
    return "Vai Corinthians Snake em Python!"


if __name__ == "__main__":
    app.run(port=8080, debug=True)