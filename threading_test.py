import threading
import time


def thread_func():
    counter = 0

    while counter < 10:
        counter += 1
        print(counter)
        time.sleep(0.2)


if __name__ == "__main__":
    th = threading.Thread(target=thread_func)
    th.start()
    print("Still here!")
    time.sleep(0.5)
    print("Still here!")
    print(th.is_alive())
    time.sleep(5)
    print(th.is_alive())