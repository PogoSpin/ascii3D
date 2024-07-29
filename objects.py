from lib import Position, Vector3d

class Cube:
    def __init__(self, pos: Position, size: Vector3d):
        self.pos = pos
        self.size = size