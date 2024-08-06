from objects3d import Vector3d
from objects2d import Vector2d, Screen
from render import Renderer

# camera fov
# camera distance
# screen size = 1

class Camera:
    def __init__(self, position: Vector3d, orientation: Vector3d, fov: float):
        self.position = position
        self.orientation = orientation
        
        self.fov = fov

class World:
    def __init__(self, objects: set = set(), backgroundBrightness: float = 0):
        self.objects = objects
        self.backgroundBrightness = backgroundBrightness

        # other atributes of the world

class Graphics:
    def __init__(self, world: World, renderer: Renderer):
        self.world = world
        self.renderer = renderer

        self.renderer.changeBackgroundBrightness(self.world.backgroundBrightness)

    def renderWorld(self):
        for screenspaceObjectPositions in self.projectWorld():
            for point in screenspaceObjectPositions:
                self.renderer.draw.point(point)

    def projectWorld(self) -> list[list]:
        projectedObjects = []
        for obj in self.world.objects:
            objectProjectedPositions = []

            for vertexPos in obj.verticies:
                screenspacePosition = self.projectToScreenspace(vertexPos)
                objectProjectedPositions.append(screenspacePosition)
            
            projectedObjects.append(objectProjectedPositions)

        return projectedObjects

    def projectToScreenspace(self, position: Vector3d) -> Vector2d:
        # code to project 3d position to 2d screenspace point
        # for now, just passing through 3d position and ignoring z component
        return Vector2d(position.x, position.y)