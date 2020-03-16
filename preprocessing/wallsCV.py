import numpy as np
import cv2
import matplotlib.pyplot as plt
from preprocessing.world import Wall
import math


def fix_line(x1, y1, x2, y2, x_shape, y_shape):
    if x1 < 0:
        y1 = int(y1 - x1 * ((y2 - y1) / (x2 - x1)))
        x1 = 0

    if x2 > y_shape:
        y2 = int(y2 - (x2 - y_shape) * ((y2 - y1) / (x2 - x1)))
        x2 = y_shape

    if y1 > x_shape:
        x1 = int(x1 - (y1 - x_shape) * ((x2 - x1) / (y2 - y1)))
        y1 = x_shape

    if y2 < 0:
        x2 = int(x2 - y2 * ((y2 - y1) / (x2 - x1)))
        y2 = 0

    if y2 > x_shape:
        x2 = int(x2 - (y2 - x_shape) * ((x2 - x1) / (y2 - y1)))
        y2 = x_shape

    return x1, y1, x2, y2


def doHoughTransform(x, y, resolution_div, max_distance):
    walls = []

    x = np.array(x).astype(int)
    y = np.array(y).astype(int)

    offset_x = np.min(x)
    offset_y = np.min(y)

    x_shape = (np.max(x) - np.min(x)) // resolution_div
    y_shape = (np.max(y) - np.min(y)) // resolution_div

    print(x_shape, y_shape)

    im = np.zeros((x_shape + 1, y_shape + 1))
    for p in range(len(x)):
        pixel_x = (x[p] - offset_x) // resolution_div
        pixel_y = (y[p] - offset_y) // resolution_div
        im[pixel_x, pixel_y] = 255

    im = np.uint8(im)

    lines = cv2.HoughLines(np.uint8(im), 1, np.pi / 200, 80)
    print(len(lines))
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
        # cv2.line(z, (x1,y1),(x2,y2), 255)
        # cv2.line(z, (-100,0), (x_shape//3, y_shape//2),  127)

    return walls, offset_x, offset_y


"""fig = plt.figure()
ax = fig.gca()
plt.axis([-max_distance, max_distance, -max_distance, max_distance])
for l in labels:
    x = []
    y = []
    for p in range(len(points)):
        if clustering.labels_[p] == l:
            x.append(points[p][0])
            y.append(points[p][1])

    lg = linear_model.LinearRegression().fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
    if lg.score(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)) < 0.5:
        clustering = OPTICS(min_samples=0.10, max_eps=300, xi=0.01).fit(np.array([x ,y]))


    ax.scatter(x, y, s=1)
    ax.scatter(x, lg.predict(np.array(x).reshape(-1, 1)))

ax.set_aspect('equal')
plt.show()
"""
