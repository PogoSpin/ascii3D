from math import sqrt

class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector3d') -> 'Vector3d':
        if isinstance(other, Vector3d):
            return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented
        
    def __sub__(self, other: 'Vector3d') -> 'Vector3d':
        if isinstance(other, Vector3d):
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented
    
    def dot(self, other: 'Vector3d') -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    def cross(self, other: 'Vector3d') -> 'Vector3d':
        return Vector3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    


class Position(Vector3d):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        
class Cube:
    def __init__(self, pos: Position, size: float | Vector3d):
        self.pos = pos

        if type(size) == Vector3d:
            self.size = size
        else:
            self.size = Vector3d(size, size, size)

        self.verticies = [self.pos, self.pos + Vector3d(self.size.x, 0, 0), self.pos + Vector3d(0, self.size.y, 0), 
                          self.pos + Vector3d(self.size.x, self.size.y, 0), self.pos + Vector3d(0, 0, self.size.z), 
                          self.pos + Vector3d(self.size.x, 0, self.size.z), self.pos + Vector3d(0, self.size.y, self.size.z), 
                          self.pos + self.size]
        