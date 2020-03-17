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
    samples = 500

    points, x, y = driver.get_point_cloud(dsize, samples, max_distance)
    resolution_div = 8

    t = time.time()
    walls, offset_x, offset_y = doHoughTransform(x, y, resolution_div)
    print(time.time() - t)

    fig = plt.figure()
    ax = fig.gca()
    plt.axis([-max_distance, max_distance, -max_distance, max_distance])


    for wall in walls:
        y1 = wall.start_y * resolution_div + offset_y
        y2 = wall.end_y * resolution_div + offset_y
        x1 = wall.start_x * resolution_div + offset_x
        x2 = wall.end_x * resolution_div + offset_x

        wall.start_x = x1
        wall.start_y = y1
        wall.end_x = x2
        wall.end_y = y2

    for wall in walls:
        plt.plot([wall.start_x, wall.end_x],
                 [wall.start_y, wall.end_y], 'k-', lw=2, alpha=0.66)


    x,y = remove_wall_points(x, y, walls)
    ax.scatter(x, y, s=1)

    ax.set_aspect('equal')
    plt.ioff()
    plt.show()