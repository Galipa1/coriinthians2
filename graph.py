from collections import defaultdict

class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.edges = defaultdict(list)

    def in_bounds(self, point):
        x, y = point
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, point):
        x, y = point
        results = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [p for p in results if self.in_bounds(p)]

    def add_block(self, point):
        self.edges[point] = []

    def build(self, snakes, food):
        for x in range(self.width):
            for y in range(self.height):
                p = (x, y)
                self.edges[p] = self.neighbors(p)

        for snake in snakes:
            for segment in snake:
                self.add_block(segment)