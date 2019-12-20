import keyboard
import time
import math
import test_1_tank_controls.config as cfg
import test_1_tank_controls.display as display
from test_1_tank_controls.collision import is_colliding
from test_1_tank_controls.fps_counter import FPSCounter

MAX_FPS = 60
MIN_FRAME_TIME = 1. / MAX_FPS

LATERAL_SENSITIVITY = cfg.lat_speed
SPEED = cfg.speed
inputs = ['w', 'a', 's', 'd']

x = 0.
y = 0.
theta = 0
lastframetime = time.time()


def get_keys():
    pressed_keys = []
    for key in inputs:
        if keyboard.is_pressed(key): pressed_keys.append(key)
    return pressed_keys


def calculate_bounding_box(x, y, theta):
    x1 = x + math.cos(theta) * cfg.bounding_box_length / 2.0 - math.sin(theta) * cfg.bounding_box_width / 2.0
    y1 = y + math.sin(theta) * cfg.bounding_box_length / 2.0 + math.cos(theta) * cfg.bounding_box_width / 2.0

    x2 = x + math.cos(theta) * cfg.bounding_box_length / 2.0 + math.sin(theta) * cfg.bounding_box_width / 2.0
    y2 = y + math.sin(theta) * cfg.bounding_box_length / 2.0 - math.cos(theta) * cfg.bounding_box_width / 2.0

    x4 = x - math.cos(theta) * cfg.bounding_box_length / 2.0 - math.sin(theta) * cfg.bounding_box_width / 2.0
    y4 = y - math.sin(theta) * cfg.bounding_box_length / 2.0 + math.cos(theta) * cfg.bounding_box_width / 2.0

    x3 = x - math.cos(theta) * cfg.bounding_box_length / 2.0 + math.sin(theta) * cfg.bounding_box_width / 2.0
    y3 = y - math.sin(theta) * cfg.bounding_box_length / 2.0 - math.cos(theta) * cfg.bounding_box_width / 2.0

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


def send_bb(rectangle_points, array):
    for i in range(4):
        array[i * 2] = rectangle_points[i][0]
        array[(i * 2) + 1] = rectangle_points[i][1]


def calculate_wall_points():
    return [(-1000, -1000), (1000, -1000), (1000, -1000), (1000, 1000), (1000, 1000), (-1000, 1000)]


def send_walls(walls, wall_count):
    assert len(walls) % 2 == 0

    wall_count.value = len(walls) // 2

    print(walls[:])
    for i in range(len(walls) // 2):
        array[8 + (i * 4)] = walls[i*2][0]
        array[8 + (i * 4) + 1] = walls[i*2][1]
        array[8 + (i * 4) + 2] = walls[i*2 + 1][0]
        array[8 + (i * 4) + 3] = walls[i*2 + 1][1]


if __name__ == "__main__":
    done = False
    fps_counter = FPSCounter(5)
    xM, yM, thM, collision, array, wall_count = display.start_display()

    wall_points = calculate_wall_points()
    send_walls(wall_points, wall_count)

    print("done ", wall_count.value, " walls")
    while True:
        keys = get_keys()
        if 'a' in keys and 'd' not in keys:
            theta += LATERAL_SENSITIVITY
        elif 'd' in keys and 'a' not in keys:
            theta -= LATERAL_SENSITIVITY

        if 'w' in keys and 's' not in keys:
            x += math.cos(theta) * SPEED
            y += math.sin(theta) * SPEED
        elif 's' in keys and 'w' not in keys:
            x -= math.cos(theta) * SPEED
            y -= math.sin(theta) * SPEED

        bounding_box = calculate_bounding_box(x, y, theta)
        send_bb(bounding_box, array)

        xM.value = x
        yM.value = y
        thM.value = theta
        collision.value = is_colliding(bounding_box, array, wall_count.value)

        while (time.time() - lastframetime) < MIN_FRAME_TIME: pass
        fps_counter.add_frame_time(time.time() - lastframetime)
        print(fps_counter.getAvgFPS())
        lastframetime = time.time()
