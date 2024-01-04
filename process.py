class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.finish_time = 0

    def id(self):
        return self.id

    def burst(self):
        return int(self.burst_time)

    def arrival(self):
        return int(self.arrival_time)

    def print(self):
        print('{} {} {}'.format(self.id, (int(self.arrival_time)-1), self.burst_time))
