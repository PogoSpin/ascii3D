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
    charset = [' ', '.', ':', '-', '=', '+', '#', '@']

    def __init__(self, brightness: float = 0):
        self.brightness = brightness  # 0-1
        self.char = Pixel.getCharFromBrightness(self.brightness)

    def setBrightness(self, value: float):
        self.brightness = value
        self.updateChar()

    def updateChar(self):
        self.char = Pixel.getCharFromBrightness(self.brightness)
    
    def getCharFromBrightness(brightness: float) -> str:
        return Pixel.charset[round(brightness * len(Pixel.charset))]

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

    def get(self, row: int = None, column: int = None, pos: Vector2d = None) -> any:
        if pos:
            row = pos.x
            column = pos.y

        return self.values[row + (self.width * column)]
    
    def set(self, value, row: int = None, column: int = None, pos: Vector2d = None):
        if pos:
            row = pos.x
            column = pos.y

        self.values[row + (self.width * column)] = value
    
    def getVectorFromIndex(self, n: int) -> Vector2d:
        return Vector2d(n % self.width, n // self.width)
    

class Grid(Matrix):
    def __init__(self, size: Vector2d, values: list = None):
        super().__init__(size, initialValues = Pixel())