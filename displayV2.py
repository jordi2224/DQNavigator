import math
import time
from multiprocessing import Process, Array, Value
import matplotlib.pyplot as plt
import test_1_tank_controls.config as cfg
from matplotlib.animation import FuncAnimation


def draw_walls(array, wall_count):
    for i in range(wall_count.value):
        plt.plot([array[8 + (i * 4)], array[8 + (i * 4) + 2]],
                 [array[8 + (i * 4) + 1], array[8 + (i * 4) + 3]],
                 color='black',
                 linewidth='2')


def draw_bounding_box(array, collision):
    if collision.value == 1:
        c = 'red'
    elif collision.value == 2:
        c = 'green'
    else:
        c = 'blue'

    plt.plot([array[0], array[2], array[4], array[6], array[0]],
             [array[1], array[3], array[5], array[7], array[1]],
             color=c, linewidth=2)


def draw_rays(array, wall_count, ray_count):
    offset = 8 + wall_count.value * 4
    for i in range(ray_count):
        plt.plot([array[offset + (i * 4)], array[offset + (i * 4) + 2]],
                 [array[offset + (i * 4) + 1], array[offset + (i * 4) + 3]],
                 color='red',
                 linewidth=1)


def draw_projections(array, wall_count, ray_count, x, y):
    offset = 8 + wall_count.value * 4 + ray_count * 4
    for i in range(8):
        plt.scatter([array[offset + (i * 2)]],
                    [array[offset + (i * 2) + 1]],
                    marker='x', color='red', s=100)

def draw_goal(array, wall_count, ray_count):
    offset = 8 + wall_count.value * 4 + ray_count * 4 + ray_count * 2
    plt.plot([array[offset + 0], array[offset + 2], array[offset + 4], array[offset + 6], array[offset + 0]],
             [array[offset + 1], array[offset + 3], array[offset + 5], array[offset + 7], array[offset + 1]],
             color='green', linewidth=2)


def animate(i, n, xM, yM, thM, collision, array, wall_count):
    try:
        x = xM.value
        y = yM.value
        theta = thM.value

    except:
        pass
    plt.clf()
    axes = plt.gca()
    axes.set_xlim([-cfg.map_size, cfg.map_size])
    axes.set_ylim([-cfg.map_size, cfg.map_size])
    axes.set_aspect('equal')
    plt.scatter(x, y)
    plt.plot([x, x + math.cos(theta) * cfg.bounding_box_length],
             [y, y + math.sin(theta) * cfg.bounding_box_length],
             linewidth=1)

    draw_bounding_box(array, collision)
    draw_walls(array, wall_count)
    draw_rays(array, wall_count, 8)
    draw_projections(array, wall_count, 8, xM, yM)
    draw_goal(array, wall_count, 8)

    plt.tight_layout()


def do_display(x, y, theta, collision, array, wall_count):
    plt.style.use('fivethirtyeight')
    ani = FuncAnimation(plt.gcf(), animate, interval=1, fargs=(1, x, y, theta, collision, array, wall_count))

    plt.tight_layout()
    plt.show()


class Display:
    display_process = None

    def __init__(self):
        self.shared_x = Value('d', 0.0)
        self.shared_y = Value('d', 0.0)
        self.shared_t = Value('d', 0.0)
        self.shared_array = Array('d', range(2000))
        self.shared_collision = Value('i', 0)
        self.shared_wall_count = Value('i', 0)

    def start_display(self):
        self.display_process = Process(target=do_display, args=(
            self.shared_x,
            self.shared_y,
            self.shared_t,
            self.shared_collision,
            self.shared_array,
            self.shared_wall_count))
        self.display_process.start()

    def stop_display(self):
        self.display_process.close()
        plt.close(plt.gca())

    def set_coor(self, x, y, t):
        self.shared_x.value = x
        self.shared_y.value = y
        self.shared_t.value = t

    def set_array(self, array):
        for i in range(len(array)):
            self.shared_array[i] = array[i]

    def set_wall_count(self, count):
        self.shared_wall_count.value = count
