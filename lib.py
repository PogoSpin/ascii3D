class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Position(Vector3d):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Matrix:
    def __init__(self, size: Vector2d, values: list = None):
        self.width = size.x
        self.height = size.y

        self.values = []

        if not values:
            self.initializeEmptyValues()
        

    def initializeEmptyValues(self):
            for _ in range(self.width * self.height):
                self.values.append(None)

    def get(self, row: int = None, column: int = None, pos: Vector2d = None):
        if pos:
            row = pos.x
            column = pos.y

        return self.values[row + (self.width * column)]
    
    def set(self, value, row: int = None, column: int = None, pos: Vector2d = None):
        if pos:
            row = pos.x
            column = pos.y

        self.values[row + (self.width * column)] = value
    
    def getVectorFromIndex(self, n):
        return Vector2d(n % self.width, n // self.width)