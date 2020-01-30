import math

import numpy as np

import config as cfg
import collision
from collision import Wall
import pygame


class Tank:

    def __init__(self):
        self.x = 0
        self.y = 0
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
        self.theta += angle
        self.update_bb()

    def advance(self, distance):
        self.x += math.cos(self.theta) * distance
        self.y += math.sin(self.theta) * distance
        self.update_bb()

INITIAL_WALLS = []

'''INITAL BOUNDARIES'''
INITIAL_WALLS.append(Wall((0, 0), (100, 100)))


class Environment:
    STATE_SIZE = 13
    ACTION_SIZE = 5
    max_steps = 200

    window = None

    def __init__(self):
        self.WALLS = INITIAL_WALLS
        self.tank = Tank()

    def step(self, action):
        self.max_steps -= 1
        done = False
        reward = 0

        if action == 0:  # Positive rotation
            self.tank.rotate(cfg.lat_speed)
        elif action == 1:  # Negative rotation
            self.tank.rotate(- cfg.lat_speed)
        elif action == 2:  # Move forward
            self.tank.advance(cfg.speed)
        elif action == 3:  # Move backwards
            self.tank.advance(-cfg.speed)

    def render(self):
        if not self.window:
            pygame.init()

            self.window = pygame.display.set_mode((650,650))

        self.window.fill((255, 255, 255))
        for wall in env.tank.bounding_box:
            s_wall_p1 = np.array(wall.p1) * cfg.scale
            s_wall_p2 = np.array(wall.p2) * cfg.scale
            pygame.draw.line(self.window, wall.color, s_wall_p1, s_wall_p2)

        pygame.display.update()



if __name__ == "__main__":

    env = Environment()
    env.render()

    done = False
    while not done:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        action = 5
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            action = 2
        elif pressed_keys[pygame.K_s]:
            action = 3
        elif pressed_keys[pygame.K_a]:
            action = 0
        elif pressed_keys[pygame.K_d]:
            action = 1

        env.step(action)
        env.render()