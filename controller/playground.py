from controller.corrected_movement import *
from preprocessing.world import World, print_world
import matplotlib.pyplot as plt

if __name__ == "__main__":
    s = get_socket('192.168.1.177', 420)
    buff = ''

    request_scan(s, sample_size=900)
    _, buff = wait_for_msg(s, buff)
    # Default max range 5m
    data_x, data_y, buff = receive_scan(s, buff)
    resolution_div = 80
    max_distance = 3500
    im, _, _ = p_crush(data_x, data_y, resolution_div, max_range=max_distance * 2)
    im = sp.ndimage.filters.gaussian_filter(im, [1, 1])
    if True:
        prediction = translate_image(im, -500 / resolution_div)
        prediction = sp.ndimage.filters.gaussian_filter(prediction, [1, 1])

        error = []
        delta = []

        for i in range(-12, 12):
            test = translate_image(im, i)
            diff = np.sum(np.absolute(test - prediction))
            error.append(diff)
            delta.append(i)

        plt.plot(delta, error)
        plt.show()

    else:
        print("Original size: " + str(im.shape))
        prediction = rotate_image(im, 45)
        print("Rotated size: " + str(prediction.shape))
        diff = np.array(prediction.shape) - np.array(im.shape)
        print(diff)
        prediction = prediction[diff[0]//2:prediction.shape[0]-diff[0]//2, diff[1]//2:prediction.shape[1]-diff[1]//2]
        prediction[prediction > 127] = 255
        prediction[prediction <= 127] = 0
        sigma = [2, 2]
        blurred = sp.ndimage.filters.gaussian_filter(prediction, sigma, mode='constant')

        f, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, sharex=False, sharey=False)
        ax1.imshow(im)
        ax1.title.set_text("Original scan grid")
        ax1.axis('off')
        ax2.imshow(blurred)
        ax2.title.set_text("Filtered prediction")
        ax2.axis('off')

        input()

        request_scan(s, sample_size=900)
        _, buff = wait_for_msg(s, buff)
        # Default max range 5m
        data_x, data_y, buff = receive_scan(s, buff)
        resolution_div = 80
        max_distance = 3500
        new_scan, _, _ = p_crush(data_x, data_y, resolution_div, max_range=max_distance * 2)

        ax3.imshow(new_scan)
        ax3.title.set_text("Actual scan")
        ax3.axis('off')

        angle, best_match = find_rotation(prediction, new_scan)
        title_str = "Best Match\nrotation = " + "{:.1f}".format(angle) + "\nerror = 14845.9"
        plt.rcParams.update({'font.size': 10})
        ax4.imshow(best_match)
        ax4.title.set_text(title_str)
        ax4.axis('off')
        #input()

        plt.show()

        """request_scan(s, sample_size=900)
        _, buff = wait_for_msg(s, buff)
        # Default max range 5m
        data_x, data_y, buff = receive_scan(s, buff)
        actual, _, _ = p_crush(data_x, data_y, resolution_div, max_range=max_distance * 2)

        ax3.imshow(actual)"""

        plt.show()


    """s = get_socket('192.168.1.177', 420)
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
"""