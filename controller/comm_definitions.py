import json

START_STR = "-----BEGIN TFG MSG-----\n"
END_STR = "-----END TFG MSG-----\n"

DATA_START_STR = "-----BEGIN TFG DATA-----\n"
DATA_END_STR = "-----END TFG DATA-----\n"

TYPE_STR = "{\"type\":"


def is_complete(buff):
    return START_STR in buff and END_STR in buff


def is_clean(buff):
    return buff[0:len(START_STR)] == START_STR


def clean(buff):
    index = buff.find(START_STR)
    if index > 0:
        return buff[index: len(buff)]
    else:
        return -1


def fetch_data(buff, data_length):
    start_index = buff.find(DATA_START_STR)
    if start_index > 0:
        buff = buff[start_index: len(buff)]

    end_index = buff.find(DATA_END_STR)

    recv = end_index - (start_index + len(DATA_START_STR))
    if recv != data_length:
        print("DATA LENGTH MISMATCH!!!")
        print("Found: ", recv)
        print("Was expecting: ", data_length)

    return buff[(start_index + len(DATA_START_STR)): end_index], buff[(end_index + len(DATA_END_STR)):len(buff)]


def receive_msg(msg):
    if is_complete(msg):
        if not is_clean(msg):
            print("Buffer is not clean. Some data might have been lost")
            msg = clean(msg)
            assert msg != -1

        end_index = msg.find(END_STR)
        return msg[len(START_STR): end_index], msg[end_index + len(END_STR): len(msg)]
    else:
        return -1


def parse(buff):
    return json.loads(buff)
