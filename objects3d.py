class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Position(Vector3d):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        
class Cube:
    def __init__(self, pos: Position, size: Vector3d):
        self.pos = pos
        self.size = size