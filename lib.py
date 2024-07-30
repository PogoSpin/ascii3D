class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Position(Vector3d):
    def __init__(self, x: float, y: float, z: float):
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
        return Pixel.charset[round(brightness * (len(Pixel.charset) - 1))]

class Grid:
    def __init__(self, size: Vector2d, values: list = None, initialValues = None):
        self.width = size.x
        self.height = size.y

        self.initialValues = initialValues

        if values:
            self.values = values
        else:
            self.initializeValues(self.initialValues)
        

    def initializeValues(self, valueToInitialize: any = None):
            self.values = []
            for _ in range(self.width * self.height):
                self.values.append(valueToInitialize)

    def get(self, row: int = None, column: int = None, pos: Vector2d = None) -> any:
        if pos:
            row = pos.x
            column = pos.y

        return self.values[self.getIndexFromVector(row, column)]
    
    def set(self, value, row: int = None, column: int = None, pos: Vector2d = None):
        if pos:
            row = pos.x
            column = pos.y

        self.values[self.getIndexFromVector(row, column)] = value

    def getIndexFromVector(self, row: int = None, column: int = None, pos: Vector2d = None) -> int:
        if pos:
            row = pos.x
            column = pos.y

        return row + (self.width * column)
    
    def getVectorFromIndex(self, n: int) -> Vector2d:
        return Vector2d(n % self.width, n // self.width)
    

class Screen(Grid):
    def __init__(self, size: Vector2d, values: list = None):
        values = [Pixel() for _ in range(size.x * size.y)]
        super().__init__(size, values)