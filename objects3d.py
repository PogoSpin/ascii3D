class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    


class Position(Vector3d):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        
class Cube:
    def __init__(self, pos: Position, size: Vector3d):
        self.pos = pos
        self.size = size