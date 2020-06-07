from controller.corrected_movement import *
from preprocessing.world import World, print_world

if __name__ == "__main__":
    s = get_socket('192.168.1.177', 420)
    buff = ''
    position_x = 0
    position_y = 0
    position_theta = 0

    world = World()

    request_scan(s)
    _, buff = wait_for_msg(s, buff)
    data_x, data_y, buff = receive_scan(s, buff)

    data_x = data_x + position_x
    data_y = data_y + position_y

    for p in range(len(data_x)):
        coordinate_x = int(data_x[p] // world.grid_resolution + world.grid_size_count // 2)
        coordinate_y = int(data_y[p] // world.grid_resolution + world.grid_size_count // 2)
        world.grid[coordinate_x, coordinate_y].type = "wall"

    print_world(world)

    distance_1 = 2200
    precise_linear_maneuver(s, buff, distance_1)
    position_y += distance_1

    request_scan(s)
    _, buff = wait_for_msg(s, buff)
    data_x, data_y, buff = receive_scan(s, buff)

    data_x = data_x + position_x
    data_y = data_y + position_y

    for p in range(len(data_x)):
        coordinate_x = int(data_x[p] // world.grid_resolution + world.grid_size_count // 2)
        coordinate_y = int(data_y[p] // world.grid_resolution + world.grid_size_count // 2)
        world.grid[coordinate_x, coordinate_y].type = "wall"

    print_world(world)
    input()
    # TODO: UPDATE WORLD WITH DATA
    # TODO: DISPLAY THE WORLD
