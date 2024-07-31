class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

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

        return self.values[self.getIndexFromVector(column, row)]
    
    def set(self, value, column: int = None, row: int = None, pos: Vector2d = None):
        if pos:
            column = pos.x
            row = pos.y

        self.values[self.getIndexFromVector(column, row)] = value

    def getIndexFromVector(self, column: int = None, row: int = None, pos: Vector2d = None) -> int:
        if pos:
            column = pos.x
            row = pos.y

        return column + (self.width * row)
    
    def getVectorFromIndex(self, n: int) -> Vector2d:
        return Vector2d(n % self.width, n // self.width)
    

class Screen(Grid):
    def __init__(self, size: Vector2d, values: list = None):
        values = [Pixel(0) for _ in range(size.x * size.y)]
        super().__init__(size, values)

class Triangle:
    def __init__(self, points: tuple[Vector2d]):
        self.points = points
        self.pairings = ((self.points[0], self.points[1]), (self.points[1], self.points[2]), (self.points[2], self.points[0]))


def bresenhamLine(pos1: Vector2d, pos2: Vector2d) -> list[Vector2d]:
    x0, y0 = pos1.x, pos1.y
    x1, y1 = pos2.x, pos2.y

    # Calculate differences
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Determine the direction of the increment
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    
    # Initialize the error term
    err = dx - dy
    
    # List to store the points of the line as Vector2d
    linePoints = []

    while True:
        # Add the current point to the line
        linePoints.append(Vector2d(x0, y0))
        
        # Check if the end point is reached
        if x0 == x1 and y0 == y1:
            break
        
        # Calculate the error terms
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return linePoints