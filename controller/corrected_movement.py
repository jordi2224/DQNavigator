import decimal
import math
import pickle
import socket
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.ndimage

from controller.comm_definitions import *

# MAIN

TCP_IP = '192.168.1.177'
TCP_PORT = 420


def drange(x, y, jump):
    """
    Generator used to create a list between x and y
    Similar to range() but allows floats as intervals
    """
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)


def get_socket(TCP_IP, TCP_PORT):
    """
    Get a TCP socket connection to the desired IP and port
    returns None if this process fails
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        return s
    except:
        return None


def wait_for_msg(s, buff):
    """
    Halts execution until a full message is available in the TCP buffer
    """
    while not is_complete(buff):
        try:
            buff += s.recv(4096).decode('utf-8')
        except:
            return -1

    return 0, buff


def request_scan(s, sample_size=5000, max_range_scan=5000):
    """
    Send a LIDAR scan request to the server
    """
    request = START_STR + str(
        {"type": "REQUEST", "request": "GET_SCAN", "SAMPLE_SIZE": sample_size, "MAX_RANGE": max_range_scan}).replace(
        '\'',
        '\"') + END_STR
    s.send(request.encode('utf-8'))


def receive_scan(s, buff):
    """
    Return x and y coordinates of the next scan in the buffer
    Discards all previous messages
    """
    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg, buff = receive_msg(buff)
        msg = parse(msg)
        if msg["type"] == "SCAN_DATA":
            data_length = msg['data_size']
            while not is_complete(buff) or DATA_END_STR not in buff:
                buff += s.recv(4096).decode('utf-8')

            data, buff = fetch_data(buff, data_length)
            if data is not None:
                points = np.array(pickle.loads(data.encode('utf-8')))
                x = np.transpose(points)[0]
                y = np.transpose(points)[1]
        else:
            msg = None

    return x, y, buff


def receive_rotation_report(s, buff):
    """
    Receive a report from the buffer
    Returns the current angle theta
    """
    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg, buff = receive_msg(buff)
        msg = parse(msg)
        if msg["type"] == "MOVEMENT_ORDER_REPORT":
            old_theta = msg["initial_theta"]
            new_theta = msg["current_theta"]
            return old_theta, new_theta
        else:
            msg = None
    return None, None


def receive_linear_report(s, buff):
    # TODO
    msg = None
    while msg is None:
        _, buff = wait_for_msg(s, buff)
        msg, buff = receive_msg(buff)
        msg = parse(msg)
        if msg["type"] == "MOVEMENT_ORDER_REPORT":
            old_theta = msg["initial_theta"]
            new_theta = msg["current_theta"]
            return old_theta, new_theta
        else:
            msg = None
    return None, None


def print_walls(walls, max_distance, points_x=[], points_y=[]):
    """
    Plot wall objects in a space measuring 2*max_distance by 2*max_distance
    Can also plot x,y point data to compare
    """
    fig = plt.figure()
    ax = fig.gca()
    plt.axis([-max_distance, max_distance, -max_distance, max_distance])
    for wall in walls:
        plt.plot([wall.start_x, wall.end_x],
                 [wall.start_y, wall.end_y], 'k-', lw=2, alpha=0.66)

    ax.scatter(points_x, points_y, s=1)
    ax.axis('equal')
    plt.show()


def crush(x, y, resolution_div):
    """
    Discretizes x and y point data
    It returns a binary grid where [x,y] = 255 if at least one point falls in that space
    Uses a resolution division such that one grid space represents a resolution_div * resolution_div space
    resolution_div is in the same unit as x, y data
    """
    offset_x = np.min(x)
    offset_y = np.min(y)

    x_shape = int((np.max(x) - np.min(x)) // resolution_div)
    y_shape = int((np.max(y) - np.min(y)) // resolution_div)

    im = np.zeros((x_shape + 1, y_shape + 1), dtype='int')
    for p in range(len(x)):
        pixel_x = int((x[p] - offset_x) // resolution_div)
        pixel_y = int((y[p] - offset_y) // resolution_div)
        im[pixel_x, pixel_y] = 255

    return im, offset_x, offset_y


def p_crush(x, y, resolution_div, max_range=0):
    """
    Same as crush but respects proportions
    Center of output matrix always represents center of data
    Matrices using the same "max_range" will be square matrices in the same dimension
    Great for translations to avoid deformation
    """
    if not max_range:
        max_range = max(np.max(np.abs(x)), np.max(np.abs(y)))

    offset = max_range // 2

    im = np.zeros((int(2 * offset / resolution_div), int(2 * offset / resolution_div)), dtype='int')
    for p in range(len(x)):
        pixel_x = int((x[p] + offset) // resolution_div)
        pixel_y = int((y[p] + offset) // resolution_div)

        if 0 < pixel_x < (offset * 2) // resolution_div and 0 < pixel_y < (offset * 2) // resolution_div:
            im[pixel_x, pixel_y] = 255

    return np.rot90(im.astype('float32')), None, None


def chop(mat, d):
    """
    Chops the top d rows of a matrix and turns them into 0
    If d is negative this is done to the bottom d rows
    """
    if d > 0:
        mat[0:d, :] = 0
    if d < 0:
        height = mat.shape[0]
        mat[height + d:height, :] = 0

    return mat


def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2]  # image shape has 3 dimensions
    image_center = (
        width / 2,
        height / 2)  # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    # find the new width and height bounds
    #bound_w = int(height * abs_sin + width * abs_cos)
    #bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    #rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    #rotation_mat[1, 2] += bound_h / 2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    #""", (bound_w, bound_h)"""
    rotated_mat = cv2.warpAffine(mat, rotation_mat, mat.shape)
    return rotated_mat


def translate_image(mat, distance):
    """
    Translate an image in the y axis, distance in pixels
    """
    height = mat.shape[0]
    distance = int(distance)

    if distance > 0:
        zeros = np.zeros([distance, mat.shape[1]], dtype='float32')
        mat = mat[distance:height, :].astype('float32')

        return np.concatenate((mat, zeros), axis=0)

    elif distance < 0:
        zeros = np.zeros([-distance, mat.shape[1]], dtype='float32')
        mat = mat[0:height + distance, :].astype('float32')

        return np.concatenate((zeros, mat), axis=0)

    else:
        return mat


def clean_rotated_image(input_image):
    """
    Removes empty columns and rows surrounding the data
    """
    zero_rows = np.where(input_image.any(axis=1))[0]
    top = np.min(zero_rows)
    bot = np.max(zero_rows)
    zero_cols = np.where(input_image.any(axis=0))[0]
    left = np.min(zero_cols)
    right = np.max(zero_cols)

    output_image = input_image[top:bot, left:right]
    return output_image


def find_rotation(reference_image, actual_image, do_gaussian=True):
    if do_gaussian:
        sigma_y = 2
        sigma_x = 2
        sigma = [sigma_y, sigma_x]

        reference_image = sp.ndimage.filters.gaussian_filter(reference_image, sigma, mode='constant')
        actual_image = sp.ndimage.filters.gaussian_filter(actual_image, sigma, mode='constant')

    best_image = None
    best_angle = None
    best_diff = float('Inf')
    for angle in list(drange(0, 45, 0.2)):
        testing_image_1 = rotate_image(actual_image.astype('float32'), angle)

        diff = np.sum(np.absolute(testing_image_1 - reference_image))

        if diff < best_diff:
            best_angle = angle
            best_image = testing_image_1
            best_diff = diff

        testing_image_2 = rotate_image(actual_image.astype('float32'), -angle)

        diff = np.sum(np.absolute(testing_image_2 - reference_image))

        if diff < best_diff:
            best_angle = -angle
            best_image = testing_image_2
            best_diff = diff

    return best_angle, best_image


def find_translation(reference_image, actual_image, do_gaussian=True):
    if do_gaussian:
        sigma_y = 2
        sigma_x = 2
        sigma = [sigma_y, sigma_x]

        reference_image = sp.ndimage.filters.gaussian_filter(reference_image, sigma, mode='constant')
        actual_image = sp.ndimage.filters.gaussian_filter(actual_image, sigma, mode='constant')

    best_image = None
    best_distance = None
    best_diff = float('Inf')
    for distance in range(50):
        testing_image_1 = translate_image(actual_image, distance)
        testing_image_1 = np.array(
            cv2.resize(testing_image_1.astype('float32'), (reference_image.shape[1], reference_image.shape[0])))

        diff = np.sum(np.absolute(testing_image_1 - reference_image))

        if diff < best_diff:
            best_distance = distance
            best_image = testing_image_1
            best_diff = diff

        testing_image_2 = translate_image(actual_image, -distance)
        testing_image_2 = np.array(
            cv2.resize(testing_image_2.astype('float32'), (reference_image.shape[1], reference_image.shape[0])))

        diff = np.sum(np.absolute(testing_image_2 - reference_image))

        if diff < best_diff:
            best_distance = -distance
            best_image = testing_image_2
            best_diff = diff

    return best_distance, best_image


calib_rot = 190.0
calib_lin = 0.65
res_div = 55
max_range = 10000


def do_angle_correction(s, buff, angle, expected_output):
    if angle != 0:
        rot = math.radians(angle) * calib_rot
        rotation_message = START_STR + str(
            {"type": "CONTROLLED_MOVE_ORDER", "movement": "ROTATION",
             "value": rot}).replace('\'', '\"') + END_STR
        s.send(rotation_message.encode('utf-8'))
        old_theta, new_theta = receive_rotation_report(s, buff)
        delta_theta = new_theta - old_theta

    time.sleep(0.5)

    # New scan!
    request_scan(s)
    x, y, buff = receive_scan(s, buff)
    actual_output, _, _ = p_crush(x, y, res_div, max_range=max_range)

    best_angle, match = find_rotation(expected_output.astype('float32'), actual_output)
    print("ROT: I think im off by: ", best_angle)

    rotation_message = START_STR + str(
        {"type": "CONTROLLED_MOVE_ORDER", "movement": "ROTATION",
         "value": math.radians(-best_angle * 0.5) * calib_rot}).replace('\'', '\"') + END_STR
    s.send(rotation_message.encode('utf-8'))


def do_linear_correction(s, buff, distance, expected_output):
    # NOTE: we need to use smaller resolution division for linear
    # NOTE: thankfully it is much much faster to translate than rotate
    lin = distance * calib_lin
    linear_message = START_STR + str(
        {"type": "CONTROLLED_MOVE_ORDER", "movement": "LINEAR",
         "value": lin}).replace('\'', '\"') + END_STR
    s.send(linear_message.encode('utf-8'))

    receive_linear_report(s, buff)
    time.sleep(0.5)

    # New scan!
    request_scan(s)
    scan_x, scan_y, buff = receive_scan(s, buff)
    actual_output, _, _ = p_crush(scan_x, scan_y, res_div, max_range=max_range)

    best_distance, match = find_translation(expected_output.astype('float32'), actual_output)
    print("LIN: I think im off by: ", best_distance)

    linear_message = START_STR + str(
        {"type": "CONTROLLED_MOVE_ORDER", "movement": "LINEAR",
         "value": -best_distance * res_div * calib_lin * 0.6}).replace('\'', '\"') + END_STR
    s.send(linear_message.encode('utf-8'))


def precise_rotation_maneuver(s, angle, buff):
    errors = []
    error = float('Inf')

    print("Starting auto-correcting turn maneuver")
    # Get the expected final output
    # Scan request / Scan process
    request_scan(s)
    x, y = receive_scan(s, buff)
    im, _, _ = crush(x, y, res_div)

    expected_output = rotate_image(im.astype('float32'), -angle)
    expected_output[expected_output >= 127] = 255
    expected_output[expected_output < 127] = 0
    expected_output = clean_rotated_image(expected_output)

    # Try_to_rotate_by_angle(expected_output, angle)
    do_angle_correction(s, angle, expected_output)
    time.sleep(0.5)

    # Get_the_new_angle()
    request_scan(s)
    x, y = receive_scan(s, buff)
    im, _, _ = crush(x, y, res_div)
    error, _ = find_rotation(expected_output.astype('float32'), im.astype('float32'))

    while abs(error) > 5:
        print(error)
        # Try_to_rotate_by_angle(expected_output, angle)
        do_angle_correction(s, -error * 0.8, expected_output)
        time.sleep(0.5)

        request_scan(s)
        x, y = receive_scan(s, buff)
        im, _, _ = crush(x, y, res_div)
        error, _ = find_rotation(expected_output.astype('float32'), im.astype('float32'))

    print("Error is bellow acceptable threshold, turn done. Error: ", error)


def precise_linear_maneuver(s, buff, distance):
    print("Starting auto-correcting linear maneuver")
    # Get the expected final output
    # Scan request / Scan process
    request_scan(s)
    x, y, buff = receive_scan(s, buff)
    im, _, _ = p_crush(x, y, res_div, max_range=max_range)

    expected_output = translate_image(im.astype('float32'), -distance // res_div)

    do_linear_correction(s, buff, distance, expected_output)
    do_angle_correction(s, buff, 0, expected_output)
