from objects2d import Vector2d, Screen
from utils import *

class Renderer:
    def __init__(self, windowSize: Vector2d, backgroundBrightness: float = 0):        
        self.width = windowSize.x
        self.height = windowSize.y

        self.backgroundBrightness = backgroundBrightness

        self.screen = Screen(windowSize)

        self.draw = self.Draw(self.screen)

    def display(self):
        # print to screen
        frameToPrint = ''
        for row in range(self.height):
            rowToPrint = ''
            for column in range(self.width):
                rowToPrint += self.screen.get(Vector2d(column, row)).char
            frameToPrint += f'{rowToPrint}\n'
        Renderer.renderPrint(frameToPrint[:-1])

    def renderPrint(text):
        # clear the terminal screen and move the cursor to topleft corner, ANSI escape code
        print("\033[H\033[J", end="")
        # print the text
        print(text)

    def changeBackgroundBrightness(self, brightness):
        self.backgroundBrightness = brightness
        self.screen = Screen(self.windowSize, defaultBrightnesss = self.backgroundBrightness)

    class Draw:
        def __init__(self, screen: Screen):
            self.screen = screen

            self.changes = []

        def point(self, pos: Vector2d):
            try:
                self.screen.get(pos).setBrightness(1)
                self.changes.append(pos)
            except:
                pass

        def erase(self, pos: Vector2d):
            self.screen.get(pos).setBrightness(self.screen.defaultPixelBrightness)

        def line(self, pos1: Vector2d, pos2: Vector2d):
            pixelsOn = bresenhamLine(pos1, pos2)
            for pixelPos in pixelsOn:
                self.point(pixelPos)

        def triangle(self, trianglePairings):
            for pair in trianglePairings:
                self.line(pair[0], pair[1])

        def undoDrawings(self):
            for change in self.changes:
                self.erase(change)