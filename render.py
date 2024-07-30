from lib import Vector2d, Screen, bresenhamLine

class Renderer:
    def __init__(self, windowSize: Vector2d):
        self.width = windowSize.x
        self.height = windowSize.y

        self.screen = Screen(windowSize)

        self.draw = self.Draw(self.screen)

    def display(self):
        # print to screen
        for row in range(self.height):
            printString = ''
            for column in range(self.width):
                printString += self.screen.get(column, row).char
            print(printString)

    class Draw:
        def __init__(self, screen: Screen):
            self.screen = screen

            self.changes = []

        def point(self, pos: Vector2d):
            self.screen.get(pos = pos).setBrightness(1)
            self.changes.append(pos)

        def erase(self, pos: Vector2d):
            self.screen.get(pos = pos).setBrightness(0)

        def line(self, pos1: Vector2d, pos2: Vector2d):
            pixelsOn = bresenhamLine(pos1, pos2)
            for pixelPos in pixelsOn:
                self.point(pixelPos)

        def undoDrawings(self):
            for change in self.changes:
                self.erase(change)