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


def bresenhamLine(pos1: Vector2d, pos2: Vector2d) -> list[Vector2d]:
    # Calculate differences
    dx = abs(pos2.x - pos1.x)
    dy = abs(pos2.y - pos1.y)
    
    # Determine the direction of the increment
    sx = 1 if pos1.x < pos2.x else -1
    sy = 1 if pos1.y < pos2.y else -1
    
    # Initialize the error term
    err = dx - dy
    
    # List to store the points of the line as Vector2d
    linePoints = []

    while True:
        # Add the current point to the line
        linePoints.append(Vector2d(pos1.x, pos1.y))
        
        # Check if the end point is reached
        if pos1.x == pos2.x and pos1.y == pos2.y:
            break
        
        # Calculate the error terms
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            pos1.x += sx
        if e2 < dx:
            err += dx
            pos1.y += sy
    
    return linePoints