from lib import Position, Vector2d

class Triangle:
    def __init__(self, points: tuple[Vector2d]):
        self.points = points
        self.pairings = ((self.points[0], self.points[1]), (self.points[1], self.points[2]), (self.points[2], self.points[0]))