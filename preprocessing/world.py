import preprocessing.world_config as cfg
from driver.TSFinalDriver import Driver
from preprocessing.wallsCV import *
import matplotlib.pyplot as plt
import time


class GridEntity:
    def __init__(self, type='empty'):
        self.type = type
        self.type_int = 0


class World:
    grid_size = cfg.grid_size
    grid_resolution = cfg.grid_resolution
    grid_size_count = cfg.grid_size // cfg.grid_resolution

    grid = np.full([grid_size_count, grid_size_count], GridEntity())
    for x in range(grid_size_count):
        for y in range(grid_size_count):
            grid[x, y] = GridEntity()

    def get_grid(self):
        grid_output = np.zeros([self.grid_size_count, self.grid_size_count])
        for x in range(self.grid_size_count):
            for y in range(self.grid_size_count):
                if self.grid[x][y].type != 'empty':
                    grid_output[x][y] = 255

        return grid_output

def print_world(world):
    plt.figure("Current state of world")
    size = world.grid_size_count
    image = np.full([size, size, 3], [255, 255, 255])
    for x in range(size):
        for y in range(size):
            block_type = world.grid[x, y].type
            if block_type != 'empty':
                image[x, y] = [0, 0, 0]
    plt.imshow(np.rot90(image))
    plt.show()


def input_wall(world, wall, offset_x, offset_y):
    start_coordinates = ((wall.start_x + offset_x) // world.grid_resolution + world.grid_size_count // 2,
                         (wall.start_y + offset_y) // world.grid_resolution + world.grid_size_count // 2)
    end_coordinates = ((wall.end_x + offset_x) // world.grid_resolution + world.grid_size_count // 2,
                       (wall.end_y + offset_y) // world.grid_resolution + world.grid_size_count // 2)

    indices = makeline(start_coordinates, end_coordinates)

    for i_x, i_y in indices:
        world.grid[i_x][i_y].type = "wall"


def get_grid(world):
    size = world.grid_size_count
    out = np.zeros([size, size], dtype='int')
    for x in range(size):
        for y in range(size):
            block_type = world.grid[x, y].type
            if block_type != 'empty':
                out[x, y] = 255

    return out.astype('int')

if __name__ == "__main__":
    world = World()

    driver = Driver('COM6')
    dsize = driver.start_scan_express()

    max_distance = 3500
    samples = 500

    points, x, y = driver.get_point_cloud(dsize, samples, max_distance)
    resolution_div = 8

    t = time.time()
    walls, offset_x, offset_y = doHoughTransform(x, y, resolution_div)
    print(time.time() - t)

    walls = translate_walls(walls, offset_x, offset_y, resolution_div)

    for wall in walls:
        coordinates = np.array(makeline((wall.start_x, wall.start_y), (wall.end_x, wall.end_y)))
        coordinates = coordinates // cfg.grid_resolution + (cfg.grid_size // cfg.grid_resolution) // 2
        for coor in coordinates:
            world.grid[coor[0], coor[1]].type = "wall"

    print_world(world)

    fig = plt.figure()
    ax = fig.gca()
    plt.axis([-max_distance, max_distance, -max_distance, max_distance])
    for wall in walls:
        plt.plot([wall.start_x, wall.end_x],
                 [wall.start_y, wall.end_y], 'k-', lw=2, alpha=0.66)
    x, y = remove_wall_points(x, y, walls)
    ax.scatter(x, y, s=1)

    ax.set_aspect('equal')
    plt.ioff()
    plt.show()
