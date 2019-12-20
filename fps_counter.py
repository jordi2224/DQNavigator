import numpy

def __init__(): pass

class FPSCounter:
    array = []
    array_index = -1
    array_size = 0

    def __init__(self, size):
        assert size > 0
        self.array_size = size
        self.array = [100] * size

    def add_frame_time(self, value):
        self.array_index = (self.array_index + 1) % self.array_size
        self.array[self.array_index] = value

    def getAvgTime(self):
        return numpy.mean(self.array)

    def getAvgFPS(self):
        return 1/numpy.mean(self.array)