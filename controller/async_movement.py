from controller.GPIOdefinitions import *
import threading
import controller.async_counter_interrupt as pos

current_move_thread = None
debug = True
self_destruct_flag = False


def self_destruct():
    return self_destruct_flag


def movement_execution_thread(L_offset, R_offset):
    starting_pos_L, starting_pos_R = pos.get_track_pos()
    if debug:
        print(starting_pos_L, starting_pos_R)
    end_pos_L = starting_pos_L + L_offset
    end_pos_R = starting_pos_R + R_offset

    current_pos_L, current_pos_R = pos.get_track_pos()
    while current_pos_R < end_pos_R or current_pos_L < end_pos_L and not self_destruct():
        current_pos_L, current_pos_R = pos.get_track_pos()

        if L_offset > 0:
            if current_pos_L < end_pos_L:
                forward_left()
            else:
                halt_left()
        else:
            if current_pos_L > end_pos_L:
                reverse_left()
            else:
                halt_left()

        if R_offset > 0:
            if current_pos_R < end_pos_R:
                forward_right()
            else:
                halt_right()
        else:
            if current_pos_R > end_pos_R:
                reverse_right()
            else:
                halt_right()

    if self_destruct():
        halt()
        print("A move order was halted")
        return
    elif debug:
        print("Started at: ", starting_pos_L, starting_pos_R)
        print("Now at:     ", pos.get_track_pos())

    halt()


def override_halt():
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        self_destruct_flag = True


def execute_move(L_offset, R_offset):
    global current_move_thread, self_destruct_flag
    if current_move_thread is not None and current_move_thread.is_alive():
        return -1

    else:
        self_destruct_flag = False
        current_move_thread = threading.Thread(target=movement_execution_thread, args=(L_offset, R_offset,))
        current_move_thread.start()
        return 0
