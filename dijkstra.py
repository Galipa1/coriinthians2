import heapq

class Dijkstra:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.distances, self.previous = self._compute()

    def _compute(self):
        queue = []
        heapq.heappush(queue, (0, self.start))
        distances = {self.start: 0}
        previous = {self.start: None}

        while queue:
            current_distance, current = heapq.heappop(queue)

            for neighbor in self.graph.edges.get(current, []):
                distance = current_distance + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(queue, (distance, neighbor))

        return distances, previous

    def find_distance(self, target):
        return self.distances.get(target, float("inf"))

    def find_path(self, target):
        path = []
        current = target
        while current != self.start:
            path.append(current)
            current = self.previous.get(current)
            if current is None:
                return []
        path.reverse()
        return path