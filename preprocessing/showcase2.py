import cv2
import numpy as np

from driver.TSFinalDriver import Driver
import matplotlib.pyplot as plt
import pandas as pd
from preprocessing.world import World, input_wall, print_world, get_grid
from preprocessing.wallsCV import doHoughTransform, translate_walls, exp_doHoughTransformP, lines_to_walls
from easy_comms import *
from os import listdir
from os.path import isfile, join
from navigation.astart_test import do_Astar
from PIL import Image
import png

def get_filename():
    files = [f for f in listdir('./grids/') if isfile(join('./grids', f))]
    base = "grid"
    i = 0
    grid_name = base + str(i) + ".csv"
    while grid_name in files:
        grid_name = base + str(i) + ".csv"
        i += 1

    return grid_name


def perform_map_scan(s, buff, world, current_x, current_y, resolution_div):
    x, y, buff = do_scan(s, buff, 1000, 10000)

    lines, offset_x, offset_y = exp_doHoughTransformP(x, y, resolution_div)

    walls = lines_to_walls(lines)
    walls = translate_walls(walls, offset_x, offset_y, resolution_div)

    for wall in walls:
        input_wall(world, wall, current_x, current_y)

def show_and_path(grid, start, end):
    path = do_Astar(grid, start, end)
    image = np.full((grid.shape[0],grid.shape[1],3), (255,255,255))
    image[grid != 0] = (0,0,0)
    for p in path:
        image[p] = (0,255,0)
    plt.imshow(np.rot90(image))
    plt.show()
    input("paused")


s = get_def_connection()
buff = ''
resolution_div = 40
x = 0
y = 0
world = World()

start = (world.grid_size_count//2, world.grid_size_count//2)
end = (200, 400)

perform_map_scan(s, buff, world, x, y, resolution_div)

while True:
    str_in = input("Direction: ")
    opt = str_in[0] if len(str_in) > 0 else ''
    try:
        d = int(str_in[2:])
    except:
        d = 0
    print(d)
    if opt == 'w':
        y += d
    elif opt == 's':
        y -= d
    elif opt == 'a':
        x -= d
    elif opt == 'd':
        x += d
    elif opt == 'q':
        break

    perform_map_scan(s, buff, world, x, y, resolution_div)
    #grid = world.get_grid()
    #show_and_path(grid, start, end)


grid = world.get_grid()
image = np.full((grid.shape[0],grid.shape[1],3), (255,255,255))
image[grid != 0] = (0,0,0)

filename = get_filename()
im_fn = './grids/' + filename[:-3] + 'png'

cv2.imwrite(im_fn, np.rot90(image))


pd.DataFrame(get_grid(world)).to_csv('./grids/' + filename, sep=',')

plt.ioff()
plt.show()
