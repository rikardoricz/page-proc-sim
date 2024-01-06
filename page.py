import time

class Page:
    def __init__(self, id):
        self.id = id
        self.timestamp = time.time()
        self.last_used = 0

    def use(self, time):
        self.last_used = time
