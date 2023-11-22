import math

def point_in_triangle(point, vertices):
    """
    Check if a point is inside a triangle.

    Parameters:
    - point: Tuple (x, y) representing the point
    - vertices: List of three tuples [(x1, y1), (x2, y2), (x3, y3)] representing the vertices of the triangle

    Returns:
    - True if the point is inside the triangle, False otherwise.
    """
    x, y = point
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]

    # Calculate barycentric coordinates
    detT = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / detT
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / detT
    gamma = 1 - alpha - beta

    # Check if the point is inside the triangle
    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1

def circle_triangle_collision(circle_center, circle_radius, triangle_vertices):
    """
    Check if a circle and a triangle collide.

    Parameters:
    - circle_center: Tuple (x, y) representing the center of the circle
    - circle_radius: Radius of the circle
    - triangle_vertices: List of three tuples [(x1, y1), (x2, y2), (x3, y3)] representing the vertices of the triangle

    Returns:
    - True if the circle and triangle collide, False otherwise.
    """
    # Check if the circle center is inside the triangle
    if point_in_triangle(circle_center, triangle_vertices):
        return True

    # Check if any triangle edge intersects with the circle
    for i in range(3):
        p1 = triangle_vertices[i]
        p2 = triangle_vertices[(i + 1) % 3]
        if segment_circle_collision(p1, p2, circle_center, circle_radius):
            return True

    return False

def segment_circle_collision(segment_start, segment_end, circle_center, circle_radius):
    """
    Check if a circle and a line segment collide.

    Parameters:
    - segment_start: Tuple (x1, y1) representing the start point of the line segment
    - segment_end: Tuple (x2, y2) representing the end point of the line segment
    - circle_center: Tuple (x, y) representing the center of the circle
    - circle_radius: Radius of the circle

    Returns:
    - True if the circle and line segment collide, False otherwise.
    """
    x1, y1 = segment_start
    x2, y2 = segment_end
    cx, cy = circle_center

    # Find the point on the segment closest to the circle center
    closest_x, closest_y = closest_point_on_segment(x1, y1, x2, y2, cx, cy)

    # Check if the closest point is inside the circle
    distance_squared = (closest_x - cx) ** 2 + (closest_y - cy) ** 2
    return distance_squared <= circle_radius ** 2

def closest_point_on_segment(x1, y1, x2, y2, px, py):
    """
    Find the closest point on a line segment to a given point.

    Parameters:
    - x1, y1: Coordinates of the start point of the line segment
    - x2, y2: Coordinates of the end point of the line segment
    - px, py: Coordinates of the point

    Returns:
    - Tuple (x, y) representing the closest point on the line segment to the given point.
    """
    dx = x2 - x1
    dy = y2 - y1
    t = ((px - x1) * dx + (py - y1) * dy) / (dx ** 2 + dy ** 2)

    t = max(0, min(1, t))  # Clamp t to the range [0, 1]
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    return closest_x, closest_y

# Example usage:
circle_center = (200, 200)
circle_radius = 30
triangle_vertices = [(0, 0), (25, 10), (20, 20)]

if circle_triangle_collision(circle_center, circle_radius, triangle_vertices):
    print("Circle and triangle collide!")
else:
    print("Circle and triangle do not collide.")
