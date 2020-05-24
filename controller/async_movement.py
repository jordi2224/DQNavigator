from controller.GPIOdefinitions import *
import threading
from controller.async_counter_proto import get_track_pos

current_move_thread = None


def movement_execution_thread(L_offset, R_offset):
    starting_pos_L, starting_pos_R = get_track_pos()

    end_pos_L = starting_pos_L + L_offset
    end_pos_R = starting_pos_R + R_offset

    current_pos_L, current_pos_R = get_track_pos()
    while current_pos_R < end_pos_R or current_pos_L < end_pos_L:
        current_pos_L, current_pos_R = get_track_pos()

        if current_pos_L < end_pos_L:
            forward_left()
        else:
            halt_left()

        if current_pos_R < end_pos_R:
            forward_right()
        else:
            halt_right()
    halt()


def execute_move(L_offset, R_offset):
    global current_move_thread
    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        current_move_thread = threading.Thread(target=movement_execution_thread, args=(L_offset, R_offset,))
        current_move_thread.start()
        return 0
