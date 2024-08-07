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
        'Using Renderer, draw all objects in world space to screen'
        for screenspaceObjectPositions in self.projectWorld():
            for normalizedPoint in screenspaceObjectPositions:
                if normalizedPoint.x >= -1 and normalizedPoint.x <= 1 and normalizedPoint.y >= -1 and normalizedPoint.y <= 1:
                    pointInWindowCoords = self.normalizedPointToWindowCoords(normalizedPoint)
                    self.renderer.draw.point(pointInWindowCoords)

    def projectWorld(self) -> list[list]:
        '''Project all objects in worldspace and save projection coordinates in nested list, 
        format: [ objectPoints[ pos1, pos2, pos3]...]'''

        projectedObjects = []
        for obj in self.world.objects:  # iterate thru all objects
            objectProjectedPositions = []

            for vertexPos in obj.verticies:
                if vertexPos.z > self.camera.position.z:  # check that vertex not behind the camera, if true, just skip this vertex
                    screenspacePosition = self.projectToScreenspace(vertexPos)
                    objectProjectedPositions.append(screenspacePosition)
            
            projectedObjects.append(objectProjectedPositions)  # add projected points of this object to projectedObjects

        return projectedObjects

    def projectToScreenspace(self, position: Vector3d) -> Vector2d:
        'Convert 3d coordinate to 2d normalized screenspace'
        return Vector2d((2 * self.cameraAngleToPosX(position)) / self.camera.fov, (2 * self.cameraAngleToPosY(position)) / self.camera.fov)
    
    def cameraAngleToPosX(self, pointPos: Vector3d) -> float:
        'Find angle along x-z plane from camera to point'
        return tanh((pointPos.x - self.camera.position.x) / (pointPos.z - self.camera.position.z))
    
    def cameraAngleToPosY(self, pointPos: Vector3d) -> float:
        'Find angle along y-z place from camera to point'
        return tanh((pointPos.y - self.camera.position.y) / (pointPos.z - self.camera.position.z))
    
    # convert normalized coords, IE x and y from -1 to 1, (0, 0) = center
    def normalizedPointToWindowCoords(self, pointPos: Vector2d) -> Vector2d:
        return Vector2d(round((pointPos.x + 1) * self.renderer.width / 2), round((pointPos.y + 1) * self.renderer.height / 2))