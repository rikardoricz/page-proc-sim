import sys
import os
import data_handler

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.finish_time = 0

def simulate_fcfs(processes):
    current_time = 0
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.finish_time = current_time + process.burst_time
        current_time = process.finish_time

def calculate_metrics(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_finish_time = sum(process.finish_time for process in processes)
    average_waiting_time = total_waiting_time / len(processes)
    average_finish_time = total_finish_time / len(processes)
    return average_waiting_time, average_finish_time


if os.path.exists("input/process_data.json"):
    data = data_handler.read_data("input/process_data.json")
    print(data)
else:
    print("that file doesn't exist in the input/ directory")
    exit(-1)

processes = []

for process in data:
    process_id = process['id']
    arrival_time = process['arrival_time']
    burst_time = process['burst_time']
    process_obj = Process(process_id, arrival_time, burst_time)
    processes.append(process_obj)


# Symulacja dla FCFS
simulate_fcfs(processes)
fcfs_avg_waiting_time, fcfs_avg_finish_time = calculate_metrics(processes)
print("FCFS Metrics:")
print(f"Average Waiting Time: {fcfs_avg_waiting_time:.2f}")
print(f"Average Finish Time: {fcfs_avg_finish_time:.2f}")
