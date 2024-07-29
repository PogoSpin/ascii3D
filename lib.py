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

class Pixel:
    def __init__(self, brightness: float = 0, charSet = None):
        self.brightness = brightness

        # TODO Add charSet var for each pixel which stores current char to represent brightness
        # TODO This is decided by dividing 1 by the amount of chars in charSet
        # TODO Basically partitioning 1 into each char
        # TODO Then the pixel's char is determined by it's brightness and corresponding char

class Matrix:
    def __init__(self, size: Vector2d, values: list = None, initialValues = None):
        self.width = size.x
        self.height = size.y

        self.initializeValues = initialValues

        self.values = []

        if not values:
            self.initializeValues(self.initialValues)
        

    def initializeValues(self, valueToInitialize = None):
            for _ in range(self.width * self.height):
                self.values.append(valueToInitialize)

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
    

class Grid(Matrix):
    def __init__(self, size: Vector2d, values: list = None):
        super().__init__(size, initialValues = Pixel())