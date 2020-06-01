import math
import threading

import controller.async_counter_interrupt as pos
from controller.GPIOdefinitions import *
from controller.comm_definitions import START_STR, END_STR

current_move_thread = None
debug = True
self_destruct_flag = False

current_X = 0
current_Y = 0
current_theta = 0

pos.setup()


def self_destruct():
    return self_destruct_flag


def __execute_rotation(value, connection, quiet=True):
    """
    PRIVATE
    Execute a rotation maneuver
    This function is meant to be ran asynchronously by 'execute_move()'
    :param value:       step count for maneuver
    :param connection:  connection object to send report back to controller
    """
    global current_X, current_Y, current_theta

    # Get the initial position of drone and tracks
    initial_theta = current_theta
    if not quiet:
        print("Starting a rotation maneuver")
        print("Starting theta is: ", current_theta, math.degrees(current_theta))
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    end_pos_L = starting_pos_L + value
    end_pos_R = starting_pos_R - value

    # Set a halt target for interrupt based halting
    pos.set_halt_target(end_pos_L, end_pos_R)

    # Set individual track flags down
    L_done = False
    R_done = False
    if not quiet:
        print("Executing loop now")
    current_pos_L, current_pos_R = pos.get_track_pos()

    # Set displacement counter to 0
    total_lin = 0
    total_rot = 0
    # Loop can also be halted by self destruct flag (manual emergency halt)
    while not L_done or not R_done and not self_destruct():
        # Get the most up to date position
        new_pos_L, new_pos_R = pos.get_track_pos()

        # Calculating displacement
        sub_deltas = (new_pos_L - current_pos_L, new_pos_R - current_pos_R)
        linear_delta = (sub_deltas[0] + sub_deltas[1]) / 2
        rot_delta = (sub_deltas[0] - sub_deltas[1]) / 2
        current_theta += rot_delta / pos.rotational_calibration
        # TODO: calculate linear movement in this case. Should be a simple sin cos with theta

        # Update displacement counters
        total_lin += linear_delta
        total_rot += rot_delta

        # Check if tracks have reached the final position
        current_pos_L = new_pos_L
        current_pos_R = new_pos_R
        if value > 0:
            if current_pos_L < end_pos_L:
                forward_left()
            else:
                halt_left()
                L_done = True
            if current_pos_R > end_pos_R:
                reverse_right()
            else:
                halt_right()
                R_done = True
        else:
            if current_pos_L > end_pos_L:
                reverse_left()
            else:
                halt_left()
                L_done = True
            if current_pos_R < end_pos_R:
                forward_right()
            else:
                halt_right()
                R_done = True

    if not quiet:
        print("Movement loop is done")
        print((current_pos_L - starting_pos_L, current_pos_R - starting_pos_R))

    # Report the new current position to the controller
    report = {"type": "MOVEMENT_ORDER_REPORT", "initial_theta": initial_theta, "current_theta": current_theta,
              "x": current_X, "y": current_Y}
    report_message = START_STR + str(report).replace('\'', '\"') + END_STR
    try:
        connection.send(report_message.encode('utf-8'))
    except BrokenPipeError:
        if not quiet:
            print("Pipe was broken when attempting to send a report")


def __execute_linear(value, connection, quiet=True):
    """
    PRIVATE
    Execute a linear maneuver
    This function is meant to be ran asynchronously by 'execute_move()'
    :param value:       step count for maneuver
    :param connection:  connection object to send report back to controller
    """
    if not quiet:
        print("Starting a rotation maneuver")
        print("Starting theta is: ", current_theta, math.degrees(current_theta))
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    end_pos_L = starting_pos_L + value
    end_pos_R = starting_pos_R + value

    # Set a halt target for interrupt based halting
    pos.set_halt_target(end_pos_L, end_pos_R)

    # Set individual track flags down
    L_done = False
    R_done = False
    if not quiet:
        print("Executing loop now")
    current_pos_L, current_pos_R = pos.get_track_pos()
    # Set displacement counter to 0
    total_lin = 0
    total_rot = 0
    # Loop can also be halted by self destruct flag (manual emergency halt)
    while not L_done or not R_done and not self_destruct():
        # Get the most up to date position
        new_pos_L, new_pos_R = pos.get_track_pos()

        # Calculating displacement
        sub_deltas = (new_pos_L - current_pos_L, new_pos_R - current_pos_R)
        linear_delta = (sub_deltas[0] + sub_deltas[1]) / 2
        rot_delta = (sub_deltas[0] - sub_deltas[1]) / 2
        current_theta += rot_delta / pos.rotational_calibration
        # TODO: calculate linear movement in this case. Should be a simple sin cos with theta

        # Update displacement counters
        total_lin += linear_delta
        total_rot += rot_delta

        # Check if tracks have reached the final position
        current_pos_L = new_pos_L
        current_pos_R = new_pos_R
        if value > 0:
            if current_pos_L < end_pos_L:
                forward_left()
            else:
                halt_left()
                L_done = True
            if current_pos_R > end_pos_R:
                reverse_right()
            else:
                halt_right()
                R_done = True
        else:
            if current_pos_L > end_pos_L:
                reverse_left()
            else:
                halt_left()
                L_done = True
            if current_pos_R < end_pos_R:
                forward_right()
            else:
                halt_right()
                R_done = True

    if not quiet:
        print("Movement loop is done")
        print((current_pos_L - starting_pos_L, current_pos_R - starting_pos_R))


def __movement_execution_target(value, movement_type, connection):
    """
    PRIVATE
    Select the right function for this movement thread
    Only two possible movements: rotation or linear
    """
    if movement_type == "ROTATION":
        __execute_rotation(value, connection)
    elif movement_type == "LINAR":
        __execute_linear(value, connection)


def override_halt():
    """
    Halt the current movement thread regarding the position
    """
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        self_destruct_flag = True


def execute_move(value, movement_type, connection):
    """
    Creates a movement execution thread, only one can run simultaneously
    If a movement execution thread is already running the movement order is ignored
    """
    # NOTE: Singleton thread
    global current_move_thread, self_destruct_flag

    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        print("Seems to be a legal move: ", value, movement_type)
        self_destruct_flag = False
        current_move_thread = threading.Thread(target=__movement_execution_target,
                                               args=(value, movement_type, connection,))
        current_move_thread.start()
        return 0
