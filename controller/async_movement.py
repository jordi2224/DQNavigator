from controller.GPIOdefinitions import *
import threading
import controller.async_counter_interrupt as pos

current_move_thread = None
debug = True


def movement_execution_thread(L_offset, R_offset):
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    if debug:
        print(starting_pos_L, starting_pos_R)
    end_pos_L = starting_pos_L + L_offset
    end_pos_R = starting_pos_R + R_offset

    current_pos_L, current_pos_R = pos.get_track_pos()
    while current_pos_R < end_pos_R or current_pos_L < end_pos_L:
        current_pos_L, current_pos_R = pos.get_track_pos()

        if current_pos_L < end_pos_L:
            forward_left()
        else:
            halt_left()

        if current_pos_R < end_pos_R:
            forward_right()
        else:
            halt_right()

    if debug:
        print("Started at: ", starting_pos_L, starting_pos_R)
        print("Now at:     ", pos.get_track_pos())

    halt()


def execute_move(L_offset, R_offset):
    global current_move_thread
    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        current_move_thread = threading.Thread(target=movement_execution_thread, args=(L_offset, R_offset,))
        current_move_thread.start()
        return 0
