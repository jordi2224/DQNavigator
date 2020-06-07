import json

"""
Definitions and tools for TCP communication with controller
Recommend using these functions instead of repeating code to avoid conflicts between client and server logics
"""

# Headers and footers for messages
START_STR = "-----BEGIN TFG MSG-----\n"
END_STR = "-----END TFG MSG-----\n"

# Headers and footers for data
DATA_START_STR = "-----BEGIN TFG DATA-----\n"
DATA_END_STR = "-----END TFG DATA-----\n"


def is_complete(buff):
    """Check if buffer contains at least one package; message or data"""
    return (START_STR in buff and END_STR in buff) or (DATA_START_STR in buff and DATA_END_STR in buff)


def is_clean(buff):
    """Check if buffer is clean. Clean means there is no data before the first header"""
    return buff[0:len(START_STR)] == START_STR


def clean(buff):
    """
    Eliminates any data before the first header
    Return -1 if no header is present
    Check that buffer is in fact not clean and contains a packet somewhere
    Otherwise it will not return the buffer
    """
    index = buff.find(START_STR)
    if index > 0:
        return buff[index: len(buff)]
    else:
        return -1


def flush_stale(buff):
    """Eliminate all messages except the last one; Ignores data"""
    last_end_index = buff.rfind(END_STR)
    last_start_index = buff.rfind(START_STR, 0, last_end_index)

    return buff[last_start_index:len(buff)]


def fetch_data(buff, data_length):
    """
    Fetches next data packet in buffer; verifies data has expected length
    All messages before the first data packet are discarded
    """
    # Find where data starts
    start_index = buff.find(DATA_START_STR)
    if start_index > 0:
        buff = buff[start_index: len(buff)]
    # Find where data ends
    end_index = buff.find(DATA_END_STR)

    # Check the size of this packet
    recv = end_index - (start_index + len(DATA_START_STR))
    if recv != data_length:
        print(end_index, start_index)
        print("\nFound: ", recv, "\nWas expecting: ", data_length)
        raise ConnectionError("DATA LENGTH MISMATCH!")
    else:
        return buff[(start_index + len(DATA_START_STR)): end_index], buff[(end_index + len(DATA_END_STR)):len(buff)]


def receive_msg(msg):
    """
    Return the next message in the buffer
    Makes sure that a message actually exists
    """
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
    """Turn message string into an usable dict"""
    return json.loads(buff)
