import os
from process import Process
from log import Log
from ticker import Ticker
import data_handler

class ProcessSched:
    def __init__(self, algo_name):
        self.processes = []
        self.algo_name = algo_name
        self.log = Log(algo_name)
        self.ticker = Ticker()
        self.time = 0

    # creates processes list reading processes input data from .json file located in input directory
    def create_processes(self):
       #if data_handler.is_json(some_file):
        #    print(f"{file_path} is a JSON file.")
        if os.path.exists("input/process_data.json"):
            data = data_handler.read_data("input/process_data.json")
        else:
            print("that file doesn't exist in the input/ directory")
            exit(-1)
        #else:
        #    print(f"{file_path} is not a JSON file.")

        for process in data:
            process_id = process['id']
            arrival_time = process['arrival_time']
            burst_time = process['burst_time']
            self.processes.append(Process(process_id, arrival_time, burst_time))

        if self.algo_name == "fcfs":
            self.processes.sort(key=lambda p: p.arrival_time)
        else:
            self.processes.sort(key=lambda p: p.burst_time)

    def calculate_waiting_time(self):
        for i in range(1, len(self.processes)):
            self.processes[i].waiting_time = self.processes[i-1].burst_time + self.processes[i-1].waiting_time

    # maybe change name of method below to turnaround_time instead of finish_time?
    def calculate_finish_time(self):
        for i in range(len(self.processes)):
            self.processes[i].finish_time = self.processes[i].burst_time + self.processes[i].waiting_time
    
    def calculate_average_waiting_time(self):
        total_waiting_time = sum([p.waiting_time for p in self.processes])
        return total_waiting_time / len(self.processes)

    def calculate_total_time(self):
        return sum([p.burst_time for p in self.processes])
        # return max([process.finish_time for process in self.processes])

    #TODO
    #def calculate_total_turnaround_time(self):
    #    return 

    def simulate(self):
        self.create_processes()
        self.calculate_waiting_time()
        self.calculate_finish_time()
        avg_waiting_time = self.calculate_average_waiting_time()
        total_time = self.calculate_total_time()

        print('Process\tWaiting Time\tFinish Time')
        for process in self.processes:
            timer = 0
            while self.ticker.time() < process.arrival():
                self.ticker.tick()
            while timer < process.burst():
                self.ticker.tick()
                timer += 1
            self.time += timer
            print(f'{process.id}\t\t{process.waiting_time}\t\t{process.finish_time}')
            self.log.log_process(process.id, process.waiting_time, process.finish_time)
        self.log.log_process_final(avg_waiting_time, total_time)
        print('Average waiting time: ', avg_waiting_time)
        print('Total time: ', total_time) 

#if __name__ == "__main__":
#    fcfs = ProcessSched("fcfs")
#    sjf = ProcessSched("sjf")
#    fcfs.simulate()
#    sjf.simulate()
