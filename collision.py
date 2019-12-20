import math

from shapely.geometry import LineString, Point


def segments_intersect(segment1, segment2):
    return LineString(segment1).crosses(LineString(segment2))


def get_segments(rectangle_points):
    segments = [(rectangle_points[0], rectangle_points[1]),
                (rectangle_points[1], rectangle_points[2]),
                (rectangle_points[2], rectangle_points[3]),
                (rectangle_points[3], rectangle_points[0])]

    return segments


def rectangle_collides(rectangle_points, point1, point2):
    segments = get_segments(rectangle_points)

    for segment in segments:
        if segments_intersect(segment, (point1, point2)): return True

    return False


def is_colliding(bounding_box, walls, wall_count):
    for i in range(wall_count):
        if rectangle_collides(bounding_box,
                              (walls[(i * 4) + 0], walls[(i * 4) + 1]),
                              (walls[(i * 4) + 2], walls[(i * 4) + 3])):
            return True

    return False


def bounding_collision(bounding_box1, bounding_box2):
    segments1 = get_segments(bounding_box1)
    segments2 = get_segments(bounding_box2)

    for s1 in segments1:
        for s2 in segments2:
            if (segments_intersect(s1, s2)):
                return True

    return False


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div >= 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


def ray_projection(ray, walls, wall_count):
    intersections = []
    distances = []

    for i in range(wall_count):
        wall = [(walls[(i * 4) + 0], walls[(i * 4) + 1]), (walls[(i * 4) + 2], walls[(i * 4) + 3])]
        inter = line_intersection(ray, wall)
        if inter is not None:
            intersections.append(inter)

    for inter in intersections:
        distances.append(distance(ray[0], inter))

    return intersections[distances.index(min(distances))], min(distances)
