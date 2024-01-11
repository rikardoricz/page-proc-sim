# klasa ticker - do obslugi licznika czasu
class Ticker:
    def __init__(self):
        self.time_elapsed = 0

    def time(self):
        return self.time_elapsed

    def tick(self):
        self.time_elapsed += 1
