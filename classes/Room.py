class Room:
    size: int
    times: dict[int, bool]

    def __init__(self, size: int):
        self.size = size
        self.times = {}
        for time in range(9, 21):
            self.times[time] = True

    def get_size(self):
        return self.size

    def book(self, interval: tuple(int, int)) -> str:
        for i in range(interval[0], interval[1]):
            if self.times[i] != True:
                return "Time is not available"
        for i in range(interval[0], interval[1]):
            self.times[i] = False
            return "Successfully booked"



