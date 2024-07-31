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

    def get(self, pos: Vector2d = None) -> any:
        if self._checkCellWithinGrid(pos):
            return self.values[self.getIndexFromVector(pos)]
        raise IndexError
    
    def set(self, value, pos: Vector2d = None):
        if self._checkCellWithinGrid(pos):
            self.values[self.getIndexFromVector(pos)] = value
        else:
            raise IndexError

    def getIndexFromVector(self, pos: Vector2d = None) -> int:
        if self._checkCellWithinGrid(pos):
            return pos.x + (self.width * pos.y)
        raise IndexError
    
    def getVectorFromIndex(self, n: int) -> Vector2d:
        return Vector2d(n % self.width, n // self.width)
    
    def _checkCellWithinGrid(self, pos: Vector2d = None) -> bool:
        if pos.x < self.width and pos.y < self.height:
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