class Room:
    size: int
    times: dict[int, bool]

    def __init__(self, size: int):
        self.size = size
        self.times = {}
        for time in range(9, 18):
            self.times[time] = True

    def book(self, interval: tuple(int, int)):
        if self.is_available(interval):
            for i in range(interval[0], interval[1]):
                self.times[i] = False
        else:
            return "Time is not available"

    def is_available(self, interval: tuple(int, int)):





