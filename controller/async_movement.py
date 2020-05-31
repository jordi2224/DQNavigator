from controller.GPIOdefinitions import *
import threading
import controller.async_counter_interrupt as pos
import math

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


def execute_rotation(value, connection):
    global current_X, current_Y, current_theta
    print("Starting a rotation maneuver")
    initial_theta = current_theta
    print("Starting theta is: ", current_theta, math.degrees(current_theta))
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    end_pos_L = starting_pos_L + value
    end_pos_R = starting_pos_R - value

    pos.set_halt_target(end_pos_L, end_pos_R)

    L_done = False
    R_done = False
    print("Executing loop now")
    current_pos_L, current_pos_R = pos.get_track_pos()

    total_lin = 0
    total_rot = 0
    while not L_done or not R_done and not self_destruct():
        new_pos_L, new_pos_R = pos.get_track_pos()
        # Calculating displacement
        sub_deltas = (new_pos_L - current_pos_L, new_pos_R - current_pos_R)
        linear_delta = (sub_deltas[0] + sub_deltas[1]) / 2
        rot_delta = (sub_deltas[0] - sub_deltas[1]) / 2
        current_theta += rot_delta / pos.rotational_calibration
        # TODO: calculate linear movement in this case. Should be a simple sin cos with theta

        total_lin += linear_delta
        total_rot += rot_delta

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

    print("Movement loop is done")
    print((current_pos_L - starting_pos_L, current_pos_R - starting_pos_R))
    report = {"type": "MOVEMENT_ORDER_REPORT", "initial_theta": initial_theta, "current_theta": current_theta,
              "x": current_X, "y": current_Y}
    report_message = START_STR + str(report).replace('\'', '\"') + END_STR
    connection.send(report_message.encode('utf-8'))


def movement_execution_thread(value, movement_type, connection):
    if movement_type == "ROTATION":
        execute_rotation(value, connection)


def override_halt():
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        self_destruct_flag = True


def execute_move(value, movement_type, connection):
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        print("Seems to be a legal move: ", value, movement_type)
        self_destruct_flag = False
        current_move_thread = threading.Thread(target=movement_execution_thread,
                                               args=(value, movement_type, connection,))
        current_move_thread.start()
        return 0
