from objects3d import Vector3d
from objects2d import Vector2d, Screen
from render import Renderer
from math import tanh, radians

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

        self.camera = Camera(Vector3d(0, 0, 0), None, radians(90))

    def renderWorld(self):
        for screenspaceObjectPositions in self.projectWorld():
            for point in screenspaceObjectPositions:
                new = Vector2d(round((point.x + 1) * self.renderer.width / 2), round((point.y + 1) * self.renderer.height / 2))
                self.renderer.draw.point(new)

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
        return Vector2d((2 * self.cameraAngleToPosX(position)) / self.camera.fov, (2 * self.cameraAngleToPosY(position)) / self.camera.fov)
    
    def cameraAngleToPosX(self, pointPos):
        return tanh((pointPos.x - self.camera.position.x) / (pointPos.z - self.camera.position.z))
    
    def cameraAngleToPosY(self, pointPos):
        return tanh((pointPos.y - self.camera.position.y) / (pointPos.z - self.camera.position.z))