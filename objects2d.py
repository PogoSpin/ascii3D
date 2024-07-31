class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x + other.x, self.y + other.y)
        return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

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

    def get(self, column: int = None, row: int = None, pos: Vector2d = None) -> any:
        if pos:
            column = pos.x
            row = pos.y

        if self._checkCellWithinGrid(column, row):
            return self.values[self.getIndexFromVector(column, row)]
        raise IndexError
    
    def set(self, value, column: int = None, row: int = None, pos: Vector2d = None):
        if pos:
            column = pos.x
            row = pos.y

        if self._checkCellWithinGrid(column, row):
            self.values[self.getIndexFromVector(column, row)] = value
        else:
            raise IndexError

    def getIndexFromVector(self, column: int = None, row: int = None, pos: Vector2d = None) -> int:
        if pos:
            column = pos.x
            row = pos.y

        if self._checkCellWithinGrid(column, row):
            return column + (self.width * row)
        raise IndexError
    
    def getVectorFromIndex(self, n: int) -> Vector2d:
        return Vector2d(n % self.width, n // self.width)
    
    def _checkCellWithinGrid(self, column: int = None, row: int = None, pos: Vector2d = None):
        if pos:
            column = pos.x
            row = pos.y

        if column < self.width and row < self.height:
            return True
        return False

class Screen(Grid):
    def __init__(self, size: Vector2d, values: list = None):
        values = [Pixel(0) for _ in range(size.x * size.y)]
        super().__init__(size, values)

class Triangle:
    def __init__(self, points: tuple[Vector2d]):
        self.points = points
        self.pairings = ((self.points[0], self.points[1]), (self.points[1], self.points[2]), (self.points[2], self.points[0]))