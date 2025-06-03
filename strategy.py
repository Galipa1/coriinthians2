from graph import Graph
from dijkstra import Dijkstra

class Cycle:
    def __init__(self, data):
        self.data = data
        self.width = data["board"]["width"]
        self.height = data["board"]["height"]
        self.you = data["you"]
        self.board = data["board"]
        self.head = (self.you["head"]["x"], self.you["head"]["y"])
        self.snakes = [[(p["x"], p["y"]) for p in s["body"]] for s in self.board["snakes"]]

    def find_move(self):
        graph = Graph(self.width, self.height)
        graph.build(self.snakes, self.board["food"])

        dijkstra = Dijkstra(graph, self.head)

        food = [(f["x"], f["y"]) for f in self.board["food"]]
        closest_food = None
        min_dist = float("inf")
        for f in food:
            if dijkstra.find_distance(f) < min_dist:
                closest_food = f
                min_dist = dijkstra.find_distance(f)

        if closest_food:
            path = dijkstra.find_path(closest_food)
            if path:
                next_pos = path[0]
                return self.move_to(next_pos)

        safe_moves = self.valid_moves()
        return safe_moves[0] if safe_moves else "up"

    def move_to(self, next_pos):
        x, y = self.head
        nx, ny = next_pos
        if nx == x + 1:
            return "right"
        if nx == x - 1:
            return "left"
        if ny == y + 1:
            return "up"
        if ny == y - 1:
            return "down"
        return "up"

    def valid_moves(self):
        x, y = self.head
        candidates = {
            "up": (x, y + 1),
            "down": (x, y - 1),
            "left": (x - 1, y),
            "right": (x + 1, y)
        }
        moves = []
        occupied = set(p for snake in self.snakes for p in snake)

        for move, (nx, ny) in candidates.items():
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in occupied:
                moves.append(move)
        return moves