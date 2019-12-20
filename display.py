import math
import time
from multiprocessing import Process, Array, Value
import matplotlib.pyplot as plt
import test_1_tank_controls.config as cfg
from matplotlib.animation import FuncAnimation

pltThread = None


def draw_walls(array, wall_count):
    for i in range(wall_count.value):
        plt.plot([array[8 + (i * 4)], array[8 + (i * 4) + 2]],
                 [array[8 + (i * 4) + 1], array[8 + (i * 4) + 3]],
                 color='black',
                 linewidth='2')


def draw_bounding_box(array, collision):
    if collision.value:
        c = 'red'
    else:
        c = 'blue'

    plt.plot([array[0], array[2], array[4], array[6], array[0]],
             [array[1], array[3], array[5], array[7], array[1]],
             color=c, linewidth=2)


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

    plt.tight_layout()


def do_display(x, y, theta, collision, array, wall_count):
    plt.style.use('fivethirtyeight')
    ani = FuncAnimation(plt.gcf(), animate, interval=1, fargs=(1, x, y, theta, collision, array, wall_count))

    plt.tight_layout()
    plt.show()


def start_display():
    x = Value('d', 0.0)
    y = Value('d', 0.0)
    theta = Value('d', 0.0)
    array = Array('d', range(2000))
    collision = Value('b', False)
    wall_count = Value('i', 0)

    p = Process(target=do_display, args=(x, y, theta, collision, array, wall_count))
    p.start()

    time.sleep(2)

    return x, y, theta, collision, array, wall_count


def set_coordinates(new_x, new_y, new_th):
    global x, y, theta
    x = new_x
    y = new_y
    theta = new_th
