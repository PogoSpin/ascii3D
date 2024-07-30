from lib import Vector2d, Screen

class Renderer:
    def __init__(self, windowSize: Vector2d):
        self.width = windowSize.x
        self.height = windowSize.y

        self.screen = Screen(windowSize)

        self.draw = self.Draw(self.screen)

    def display(self):
        # print to screen
        for row in range(self.width):
            printString = ''
            for column in range(self.height):
                printString += self.screen.get(row, column).char
            print(printString)

    class Draw:
        def __init__(self, screen: Screen):
            self.screen = screen

        def point(self, pos: Vector2d):
            self.screen.get(pos = pos).setBrightness(1)

        def line(self, pos1: Vector2d, pos2: Vector2d):
            # algorithm to draw line
            pass