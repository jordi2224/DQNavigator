import numpy as np
import cv2
from sklearn.cluster import DBSCAN
from preprocessing.world import Wall
import math


def fix_line(x1, y1, x2, y2, x_shape, y_shape):
    tan = (y2 - y1) / (x2 - x1)
    i_tan = (x2 - x1) / (y2 - y1)
    if x1 < 0:
        y1 = int(y1 - x1 * tan)
        x1 = 0

    if x1 > y_shape:
        y1 = int(y1 - (x1 - y_shape) * i_tan)
        x1 = y_shape

    if x2 < 0:
        y2 = int(y2 - x2 * tan)
        x2 = 0

    if x2 > y_shape:
        y2 = int(y2 - (x2 - y_shape) * tan)
        x2 = y_shape

    if y1 < 0:
        x1 = int(x1 - y1 * i_tan)
        y1 = 0

    if y1 > x_shape:
        x1 = int(x1 - (y1 - x_shape) * i_tan)
        y1 = x_shape

    if y2 < 0:
        x2 = int(x2 - y2 * i_tan)
        y2 = 0

    if y2 > x_shape:
        x2 = int(x2 - (y2 - x_shape) * i_tan)
        y2 = x_shape

    return x1, y1, x2, y2


def remove_redundant_lines(lines):
    lines_inner = np.array([x[0] for x in lines])
    clustering = DBSCAN(eps=12, min_samples=1).fit(lines_inner)

    n_clusters = len(set(clustering.labels_))
    clusters = [lines_inner[clustering.labels_ == i] for i in range(n_clusters)]

    clean_lines = []
    for cluster in clusters:
        rho = np.average(np.transpose(cluster)[0])
        theta = np.average(np.transpose(cluster)[1])

        clean_lines.append([[rho, theta]])

    return clean_lines


def distance_point_line(lp1, lp2, p):
    x1 = lp1[0]
    y1 = lp1[1]
    x2 = lp2[0]
    y2 = lp2[1]

    x0 = p[0]
    y0 = p[1]

    delta_l = math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))
    delta_p = math.fabs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)

    return delta_p / delta_l


def remove_wall_points(x, y, walls):
    non_walls_x = []
    non_walls_y = []

    for p_i in range(len(x)):
        dmin = 99999
        for wall in walls:

            d = distance_point_line((wall.start_x, wall.start_y),
                                    (wall.end_x, wall.end_y),
                                    (x[p_i], y[p_i]))
            if d < dmin:
                dmin = d
        if dmin > 70:
            non_walls_x.append(x[p_i])
            non_walls_y.append(y[p_i])

    return non_walls_x, non_walls_y


def doHoughTransform(x, y, resolution_div):
    walls = []

    x = np.array(x).astype(int)
    y = np.array(y).astype(int)

    offset_x = np.min(x)
    offset_y = np.min(y)

    x_shape = (np.max(x) - np.min(x)) // resolution_div
    y_shape = (np.max(y) - np.min(y)) // resolution_div

    im = np.zeros((x_shape + 1, y_shape + 1))
    for p in range(len(x)):
        pixel_x = (x[p] - offset_x) // resolution_div
        pixel_y = (y[p] - offset_y) // resolution_div
        im[pixel_x, pixel_y] = 255

    im = np.uint8(im)

    lines = cv2.HoughLines(np.uint8(im), 1, np.pi / 600, 30)
    lines = remove_redundant_lines(lines)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)

        x1, y1, x2, y2 = fix_line(x1, y1, x2, y2, x_shape, y_shape)

        walls.append(Wall((y1, x1), (y2, x2)))

    return walls, offset_x, offset_y


def makeline(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    steps = dx if (dx > dy) else dy
    xinc = dx / float(steps)
    yinc = dy / float(steps)

    out = np.zeros([steps + 1, 2], dtype='int')
    x = point1[0]
    y = point1[1]
    for i in range(steps + 1):
        out[i] = (x, y)
        x += xinc
        y += yinc

    return out
