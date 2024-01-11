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

    # tworzenie procesow - odczyt z pliku input/process_data.json i dodanie danych o procesach do listy obiektow procesow
    def create_processes(self):
        if os.path.exists("input/process_data.json"):
            data = data_handler.read_data("input/process_data.json")
        else:
            print("that file doesn't exist in the input/ directory")
            exit(-1)

        for process in data:
            process_id = process['id']
            arrival_time = process['arrival_time']
            burst_time = process['burst_time']
            self.processes.append(Process(process_id, arrival_time, burst_time))

        if self.algo_name == "fcfs":
            self.processes.sort(key=lambda p: p.arrival_time) # sortowanie listy procesow po czasie nadejscia
        else:
            self.processes.sort(key=lambda p: p.burst_time) # sortowanie listy procesow po czasie wykonania

    # liczenie czasu oczekiwania dla kazdego procesu
    def calculate_waiting_time(self):
        for i in range(1, len(self.processes)):
            self.processes[i].waiting_time = self.processes[i-1].burst_time + self.processes[i-1].waiting_time

    # liczenie czasu ukonczenia wykonywania procesu
    def calculate_finish_time(self):
        for i in range(len(self.processes)):
            self.processes[i].finish_time = self.processes[i].burst_time + self.processes[i].waiting_time
    
    # liczenie sredniego czasu oczekiwania procesow
    def calculate_average_waiting_time(self):
        total_waiting_time = sum([p.waiting_time for p in self.processes])
        return total_waiting_time / len(self.processes)

    # liczenie calkowitego czasu 
    def calculate_total_time(self):
        return sum([p.burst_time for p in self.processes])
        # return max([process.finish_time for process in self.processes])

    # liczenie sredniego czasu realizacji procesow
    def calculate_avg_tat(self):
        finish_time_sum = sum([p.finish_time for p in self.processes])
        return finish_time_sum / len(self.processes)


    # symulacja algorytmow planowania czasu procesora
    def simulate(self):
        self.create_processes()
        self.calculate_waiting_time()
        self.calculate_finish_time()
        avg_waiting_time = self.calculate_average_waiting_time()
        avg_tat = self.calculate_avg_tat()
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
        self.log.log_process_final(avg_waiting_time, total_time, avg_tat)
        print('Average waiting time: ', avg_waiting_time)
        print('Average turnaround time: ', avg_tat)
        print('Total time: ', total_time) 

