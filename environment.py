import math
import random
import numpy as np
import config as cfg
import collision
from collision import Wall
import pygame

INITIAL_WALLS = []

'''INITAL BOUNDARIES'''
INITIAL_WALLS.append(Wall((0, 0), (0, cfg.SLS)))
INITIAL_WALLS.append(Wall((0, cfg.SLS), (cfg.SLS, cfg.SLS)))
INITIAL_WALLS.append(Wall((cfg.SLS, cfg.SLS), (cfg.SLS, 0)))
INITIAL_WALLS.append(Wall((cfg.SLS, 0), (0, 0)))

'''VISION RAYS THETAS'''
RAY_THETAS = [math.pi / 6, -math.pi / 6]


class Tank:

    def __init__(self):
        self.x = cfg.SLS // 2
        self.y = cfg.SLS // 2
        self.theta = 0

        self.bounding_box = collision.calculate_bounding_box(self.x, self.y, self.theta, cfg.bounding_box_width,
                                                             cfg.bounding_box_length)

    def get_coor(self):
        return self.x, self.y, self.theta

    def get_bounding_box(self):
        self.bounding_box = collision.calculate_bounding_box(self.x, self.y, self.theta, cfg.bounding_box_width,
                                                             cfg.bounding_box_length)
        return self.bounding_box

    def update_bb(self):
        self.bounding_box = collision.calculate_bounding_box(self.x, self.y, self.theta, cfg.bounding_box_width,
                                                             cfg.bounding_box_length)

    def rotate(self, angle):
        self.theta = (self.theta + angle)
        if self.theta > math.pi:
            self.theta -= math.pi * 2.
        elif self.theta < -math.pi:
            self.theta += math.pi * 2.
        self.update_bb()

    def advance(self, distance):
        self.x += math.cos(self.theta) * distance
        self.y += math.sin(self.theta) * distance
        self.update_bb()

    def get_rays(self):

        ray_array = []
        for ray_theta in RAY_THETAS:
            theta = self.theta + ray_theta
            end_x = self.x + math.cos(theta) * cfg.MAX_RAY_DIST
            end_y = self.y + math.sin(theta) * cfg.MAX_RAY_DIST

            ray = Wall((self.x, self.y), (end_x, end_y), color=(255, 0, 0))
            ray_array.append(ray)

        return ray_array


class Waypoint:

    def __init__(self, x, y, s=100, type='goal'):
        self.x = x
        self.y = y
        self.s = s
        self.bounding_box = collision.calculate_bounding_box(x, y, 0, s, s)
        for wall in self.bounding_box:
            if type == 'goal':
                wall.color = (0, 255, 0)
            elif type == 'hazard':
                wall.color = (255, 0, 0)


def draw(window, line_array):
    for wall in line_array:
        s_wall_p1 = np.array(wall.p1) * cfg.scale
        s_wall_p2 = np.array(wall.p2) * cfg.scale
        pygame.draw.aaline(window, wall.color, s_wall_p1, s_wall_p2)


def draw_projections(window, projections):
    s = cfg.collision_marker_size

    for projection in projections:
        projection = np.array(projection) * cfg.scale
        pygame.draw.rect(window, (255, 0, 0), (projection[0] - s // 2, projection[1] - s // 2, s, s))


class Environment:
    STATE_SIZE = 4
    ACTION_SIZE = 4
    steps = cfg.MAX_STEPS
    last_delta_abs = 0

    window = None

    def __init__(self, diff="easy"):
        self.projections = []
        self.distances = []
        self.WALLS = INITIAL_WALLS
        self.tank = Tank()

        self.diff = diff
        if diff == "easy":
            self.place_goal_easy()
        else:
            self.place_goal_ran()

        self.hazard = Waypoint(cfg.SLS // 2, cfg.SLS * 3 // 4, type='hazard')

        self.calculate_projections()

        self.last_delta_abs = math.fabs(self.to_goal()[1])

    def place_goal_ran(self):
        alpha = random.random()
        if random.random() < 0.5:
            if alpha < 0.01:
                self.goal = Waypoint(cfg.SLS * 3 // 4, cfg.SLS // 2)
            elif alpha < 0.5:
                self.goal = Waypoint(cfg.SLS * 3 // 4, cfg.SLS * 2 // 6)
            else:
                self.goal = Waypoint(cfg.SLS * 3 // 4, cfg.SLS * 4 // 6)
        else:
            if alpha < 0.01:
                self.goal = Waypoint(cfg.SLS * 1 // 4, cfg.SLS // 2)
            elif alpha < 0.5:
                self.goal = Waypoint(cfg.SLS * 1 // 4, cfg.SLS * 2 // 6)
            else:
                self.goal = Waypoint(cfg.SLS * 1 // 4, cfg.SLS * 4 // 6)


    def place_goal_easy(self):
        self.goal = Waypoint(cfg.SLS * 5 // 6, cfg.SLS // 2)

    def reset(self):
        self.tank = Tank()
        self.steps = cfg.MAX_STEPS
        if self.diff == 'easy':
            self.place_goal_easy()
        else:
            self.place_goal_ran()

        self.last_delta_abs = math.fabs(self.to_goal()[1])

        # No reward, new state, not done
        return 0, self.get_state(), False

    def to_goal(self):

        diff_x = self.goal.x - self.tank.x
        diff_y = self.goal.y - self.tank.y
        diff_th = math.atan2(diff_y, diff_x)

        return [collision.distance((self.goal.x, self.goal.y),
                                   (self.tank.x, self.tank.y)) / cfg.SLS,
                (self.tank.theta - diff_th) / 3.1]

    def to_hazard(self):

        diff_x = self.hazard.x - self.tank.x
        diff_y = self.hazard.y - self.tank.y
        diff_th = math.atan2(diff_y, diff_x)

        return [collision.distance((self.hazard.x, self.hazard.y),
                                   (self.tank.x, self.tank.y)) / cfg.SLS,
                (self.tank.theta - diff_th) / 3.1]

    def calculate_projections(self):
        self.projections = []
        self.distances = []
        for ray in self.tank.get_rays():
            projection = collision.ray_projection(ray, self.WALLS)
            self.projections.append(projection[0])
            self.distances.append(projection[1])

    def get_state(self):
        return (np.array(self.distances) / cfg.SLS).tolist() + self.to_goal() # + self.to_hazard()

    def calculate_reward(self):
        distance_reward = 1 - math.pow(self.to_goal()[0], 0.4)
        angle_reward = 1 - math.pow(math.fabs(self.to_goal()[1]), 0.4)
        return distance_reward + angle_reward*2

    def calculate_movement_reward(self, action):
        pass

    def step(self, action):
        self.steps -= 1
        done = False
        reward = cfg.STEP_REWARD

        new_delta_abs = math.fabs(self.to_goal()[1])
        if action == 0:  # Positive rotation
            self.tank.rotate(cfg.lat_speed)
        elif action == 1:  # Negative rotation
            self.tank.rotate(- cfg.lat_speed)
        elif action == 2:  # Move forward
            self.tank.advance(cfg.speed)
        elif action == 3:  # Move backwards
            self.tank.advance(-cfg.speed)
        elif action == 4:  # No movement
            pass

        self.last_delta_abs = new_delta_abs

        reward += self.calculate_reward()

        if (collision.bounding_collision(self.tank.bounding_box, self.WALLS) or
                collision.bounding_collision(self.tank.bounding_box, self.hazard.bounding_box)):
            done = True
            reward += cfg.WALL_HIT_REWARD
            for w in self.tank.bounding_box:
                w.color = (255, 0, 0)

        if (self.to_goal()[0]*cfg.SLS) < cfg.bounding_box_width*0.6:
            done = True
            reward += cfg.GOAL_REWARD
            for w in self.tank.bounding_box:
                w.color = (0, 255, 0)
        elif self.steps == 0:
            done = True
            reward += cfg.NO_STEPS_REWARD
            for w in self.tank.bounding_box:
                w.color = (255, 0, 0)

        self.calculate_projections()

        return reward, self.get_state(), done

    def render(self):
        if not self.window:
            pygame.init()

            self.window = pygame.display.set_mode((cfg.win_W, cfg.win_H))

        self.window.fill((255, 255, 255))

        draw(self.window, self.tank.bounding_box)
        draw(self.window, self.goal.bounding_box)
        draw(self.window, self.WALLS)
        draw(self.window, self.tank.get_rays())
        draw(self.window, self.hazard.bounding_box)

        draw_projections(self.window, self.projections)
        pygame.display.flip()
        pygame.display.update()
