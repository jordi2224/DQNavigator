import preprocessing.world_config as cfg
import preprocessing.wallsCV as wallsCV
from driver.TSFinalDriver import Driver
import matplotlib.pyplot as plt
from preprocessing.wallsCV import *
import time


class Entity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Actor(Entity):
    def __init__(self, x, y, theta):
        super(Actor, self).__init__(x=x, y=y)
        self.theta = theta


class Wall(Entity):
    def __init__(self, start, end):
        self.start_x = start[0]
        self.start_y = start[1]
        self.end_x = end[0]
        self.end_y = end[1]

        super(Wall, self).__init__(x=self.start_x, y=self.start_y)


class World:
    walls = []


if __name__ == "__main__":
    driver = Driver('COM6')
    dsize = driver.start_scan_express()

    max_distance = 3500

    points, x, y = driver.get_point_cloud(dsize, 900, max_distance)
    resolution_div = 8
    t = time.time()
    walls, offset_x, offset_y = doHoughTransform(x, y, resolution_div, max_distance)
    print(time.time()-t)

    fig = plt.figure()
    ax = fig.gca()
    plt.axis([-max_distance, max_distance, -max_distance, max_distance])

    ax.scatter(x, y, s=1)
    for wall in walls:
        y1 = wall.start_y * resolution_div + offset_y
        y2 = wall.end_y * resolution_div + offset_y
        x1 = wall.start_x * resolution_div + offset_x
        x2 = wall.end_x * resolution_div + offset_x
        plt.plot([x1, x2],
                 [y1, y2], 'k-', lw=2)

    ax.set_aspect('equal')
    plt.ioff()
    plt.show()
