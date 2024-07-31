from objects2d import Vector2d

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