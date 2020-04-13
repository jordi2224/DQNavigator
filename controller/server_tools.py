import json

START_STR = "-----BEGIN TFG MSG-----\n"
END_STR = "-----END TFG MSG-----\n"


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


def receive_msg(msg):
    if is_complete(msg):
        if not is_clean(msg):
            print("Buffer is not clean. Some data might have been lost")
            print(msg)
            msg = clean(msg)
            assert msg != -1

        end_index = msg.find(END_STR)
        return msg[len(START_STR): end_index], msg[end_index + len(END_STR): len(msg)]
    else:
        return -1


def parse(buff):
    return json.loads(buff)
