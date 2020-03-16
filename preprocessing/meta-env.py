from collision import Wall
import pygame
import config as cfg
import numpy as np

MAX_DISTANCE = cfg.SLS
GRID_SIZE = int(MAX_DISTANCE / 100)
PIXEL_RESOLUTION_W = cfg.win_W // GRID_SIZE
PIXEL_RESOLUTION_H = cfg.win_H // GRID_SIZE

grid = np.ones((GRID_SIZE, GRID_SIZE), dtype=np.bool)
pygame.init()
window = pygame.display.set_mode((cfg.win_W, cfg.win_H))
window.fill((255, 255, 255))


for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        if x == y:
            grid[x][y] = 0
        if grid[x][y]:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)

        pygame.draw.rect(window, color,
                         (PIXEL_RESOLUTION_W * x, PIXEL_RESOLUTION_H * y,
                          PIXEL_RESOLUTION_W,
                          PIXEL_RESOLUTION_H))

pygame.display.update()
while True:
    pass
