import keyboard
import time
import math
import test_1_tank_controls.config as cfg
from test_1_tank_controls.displayV2 import Display
from test_1_tank_controls.collision import is_colliding, ray_projection, bounding_collision, distance
from test_1_tank_controls.fps_counter import FPSCounter

INITIAL_WALLS = [(-1500, 500), (1500, 500),
                 (1500, 500), (1500, -500),
                 (1500, -500), (-1500, -500),
                 (-1500, -500), (-1500, 500)]

RAY_COUNT = 8
RAYS_MAX_RANGE = 10000


def calculate_bounding_box(x, y, theta, W, L):
    x1 = x + math.cos(theta) * L / 2.0 - math.sin(theta) * W / 2.0
    y1 = y + math.sin(theta) * L / 2.0 + math.cos(theta) * W / 2.0

    x2 = x + math.cos(theta) * L / 2.0 + math.sin(theta) * W / 2.0
    y2 = y + math.sin(theta) * L / 2.0 - math.cos(theta) * W / 2.0

    x4 = x - math.cos(theta) * L / 2.0 - math.sin(theta) * W / 2.0
    y4 = y - math.sin(theta) * L / 2.0 + math.cos(theta) * W / 2.0

    x3 = x - math.cos(theta) * L / 2.0 + math.sin(theta) * W / 2.0
    y3 = y - math.sin(theta) * L / 2.0 - math.cos(theta) * W / 2.0

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


def get_rays_thetas(theta0):
    rays_thetas = []
    for i in range(RAY_COUNT):
        rays_thetas.append(theta0 + (math.pi / 4.) * i)

    return rays_thetas


def get_rays_coords(x, y, theta0):
    thetas = get_rays_thetas(theta0)
    coords = []
    for theta in thetas:
        coords.append(x)
        coords.append(y)
        end_x = x + math.cos(theta) * RAYS_MAX_RANGE
        end_y = y + math.sin(theta) * RAYS_MAX_RANGE
        coords.append(end_x)
        coords.append(end_y)

    return coords


def get_rays_array(x, y, theta0):
    thetas = get_rays_thetas(theta0)
    rays = []
    for theta in thetas:
        ray = [(x, y)]
        end_x = round(x + math.cos(theta) * RAYS_MAX_RANGE, 2)
        end_y = round(y + math.sin(theta) * RAYS_MAX_RANGE, 2)
        ray.append((end_x, end_y))
        rays.append(ray)

    return rays


def get_ray_projections(x, y, theta0, walls):
    rays = get_rays_array(x, y, theta0)
    projections = []
    distances = []

    for ray in rays:
        projection, distance = ray_projection(ray, get_walls_array(walls), len(walls) // 2)

        projections.append(projection[0])
        projections.append(projection[1])

        distances.append(distance)

    return projections, distances


def get_walls_array(walls):
    array = []
    for i in range(len(walls) // 2):
        array.append(walls[i * 2][0])
        array.append(walls[i * 2][1])
        array.append(walls[i * 2 + 1][0])
        array.append(walls[i * 2 + 1][1])

    return array


def get_bounding_array(rectangle_points):
    array = [0] * 8
    for i in range(4):
        array[i * 2] = rectangle_points[i][0]
        array[(i * 2) + 1] = rectangle_points[i][1]

    return array


class Tank:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0

        self.bounding_box = calculate_bounding_box(self.x, self.y, self.theta, cfg.bounding_box_width,
                                                   cfg.bounding_box_length)

    def get_coor(self):
        return self.x, self.y, self.theta

    def get_bounding_box(self):
        self.bounding_box = calculate_bounding_box(self.x, self.y, self.theta, cfg.bounding_box_width,
                                                   cfg.bounding_box_length)
        return self.bounding_box

    def rotate(self, angle):
        self.theta += angle

    def advance(self, distance):
        self.x += math.cos(self.theta) * distance
        self.y += math.sin(self.theta) * distance


class Waypoint:

    def __init__(self, x, y, s=100):
        self.x = x
        self.y = y
        self.s = s

        self.bounding_box = calculate_bounding_box(x, y, 0, s, s)


class Environment:

    state_size = 13
    action_size = 4
    max_steps = 1_000

    ACTION_SPACE_SIZE = 4

    def __init__(self):
        self.walls = INITIAL_WALLS
        self.tank = Tank()
        self.display = Display()
        self.tank.x = -1000
        self.update_coords()
        self.goal = Waypoint(0, 0)

    def reset(self):
        env2 = Environment()
        reward, state, done = env2.step(2)
        return env2, reward, state, done

    def update_coords(self):
        self.x, self.y, self.t = self.tank.get_coor()

    def render(self):
        self.display.start_display()
        self.update_display()

    def update_display(self):

        self.update_coords()
        self.display.set_coor(self.x, self.y, self.t)
        projections, distances = get_ray_projections(self.x, self.y, self.t, self.walls)
        wall_point_array = get_bounding_array(self.tank.get_bounding_box()) + \
                           get_walls_array(self.walls) + \
                           get_rays_coords(self.x, self.y, self.t) + \
                           projections + get_bounding_array(self.goal.bounding_box)

        self.display.set_wall_count(len(self.walls) // 2)
        self.display.set_array(wall_point_array)

    def check_collision(self):
        return is_colliding(self.tank.get_bounding_box(), get_walls_array(self.walls), len(self.walls) // 2)

    def check_goal(self):
        return bounding_collision(self.tank.get_bounding_box(), self.goal.bounding_box)

    def to_goal(self):

        diff_x = self.goal.x - self.tank.x
        diff_y = self.goal.y - self.tank.y

        return [distance((self.goal.x, self.goal.y),
                         (self.tank.x, self.tank.y)),
                (self.tank.theta % (math.pi * 2)) - math.atan2(diff_y, diff_x)
                ]

    def step(self, action):

        self.max_steps -= 1
        done = False
        reward = -15

        if action == 0:
            self.tank.rotate(0.2)
        elif action == 1:
            self.tank.rotate(-0.2)
        elif action == 2:
            self.tank.advance(80)
        elif action == 3:
            self.tank.advance(80)

        self.update_coords()
        projections, distances = get_ray_projections(self.x, self.y, self.t, self.walls)

        self.update_display()
        if self.check_collision() or self.max_steps == 0:
            self.display.shared_collision.value = 1
            done = True
            reward = -1000
        if self.check_goal():
            self.display.shared_collision.value = 2
            done = True
            reward = 5000

        n_distances = [x / 1000 for x in distances]
        state = [self.x, self.y, self.t] + n_distances + [self.to_goal()[0]/1500, self.to_goal()[1]]
        assert len(state) == self.state_size
        return reward, state, done

