from controller.GPIOdefinitions import *
import threading
import controller.async_counter_interrupt as pos

current_move_thread = None
debug = True
self_destruct_flag = False

current_X = 0
current_Y = 0
current_theta = 0


def self_destruct():
    return self_destruct_flag


def execute_rotation(value):
    print("Starting a rotation maneuver")
    print("Attempting to rotate by: ", value)
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    print("Tracks are at: ", (starting_pos_L, starting_pos_R))
    end_pos_L = starting_pos_L + value
    end_pos_R = starting_pos_R - value
    print("Target is at: ", (end_pos_L, end_pos_R))

    L_done = False
    R_done = False
    print("Executing loop now")
    while not L_done or not R_done and not self_destruct():
        current_pos_L, current_pos_R = pos.get_track_pos()

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
    current_pos_L, current_pos_R = pos.get_track_pos()
    print("Tracks are now at: ", (current_pos_L, current_pos_R))
    deltas = (current_pos_L-starting_pos_L, current_pos_R-starting_pos_L)
    print("Deltas are:  ", deltas)
    print("Error: ", sum(deltas))


def movement_execution_thread(value, movement_type):
    if movement_type == "ROTATION":
        execute_rotation(value)
    """starting_pos_L, starting_pos_R = pos.get_track_pos()
    if debug:
        print(starting_pos_L, starting_pos_R)
    end_pos_L = starting_pos_L + L_offset
    end_pos_R = starting_pos_R + R_offset

    L_done = False
    R_done = False
    while not L_done or not R_done and not self_destruct():
        current_pos_L, current_pos_R = pos.get_track_pos()

        if L_offset > 0:
            if current_pos_L < end_pos_L:
                forward_left()
            else:
                halt_left()
                L_done = True
        else:
            if current_pos_L > end_pos_L:
                reverse_left()
            else:
                halt_left()
                L_done = True

        if R_offset > 0:
            if current_pos_R < end_pos_R:
                forward_right()
            else:
                halt_right()
                R_done = True
        else:
            if current_pos_R > end_pos_R:
                reverse_right()
            else:
                halt_right()
                R_done = True

    if self_destruct():
        halt()
        print("A move order was halted")
        return
    elif debug:
        print("Started at: ", starting_pos_L, starting_pos_R)
        print("Now at:     ", pos.get_track_pos())

    halt()"""


def override_halt():
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        self_destruct_flag = True


def execute_move(value, movement_type):
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        print("Seems to be a legal move: ", value, movement_type)
        self_destruct_flag = False
        current_move_thread = threading.Thread(target=movement_execution_thread, args=(value, movement_type,))
        current_move_thread.start()
        return 0
