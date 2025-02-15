from queue import PriorityQueue


class Enemy:
    def __init__(self, start_position, goal, map_matrix, enemy_speed=3):
        self.position = start_position
        self.goal = goal
        self.map_matrix = map_matrix
        self.enemy_speed = enemy_speed
        self.path = []
        self.index = 0
        self.move_counter = 0
        self.find_path()

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self):
        open_set = PriorityQueue()
        open_set.put((0, self.position))
        came_from = {}
        g_score = {self.position: 0}
        f_score = {self.position: self.heuristic(self.position, self.goal)}

        while not open_set.empty():
            _, current = open_set.get()

            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                self.path = path
                return

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if (
                    0 <= neighbor[1] < len(self.map_matrix)
                    and 0 <= neighbor[0] < len(self.map_matrix[0])
                    and self.map_matrix[neighbor[1]][neighbor[0]] != "M"
                ):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + self.heuristic(
                            neighbor, self.goal
                        )
                        open_set.put((f_score[neighbor], neighbor))

    def move(self):
        self.move_counter += 1
        if self.move_counter >= self.enemy_speed:
            self.move_counter = 0
            if self.index < len(self.path) - 1:
                self.index += 1
                self.position = self.path[self.index]

    def get_position(self):
        return self.position

    def find_path(self):
        self.astar()
