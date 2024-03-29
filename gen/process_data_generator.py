import os
import sys
import random
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
import data_handler

# generowanie losowo czasu nadejscia procesu oraz dlugosci trwania procesu dla zadanej ilosci procesow, maksymalnego czasu wykonania i nadejscia
def generate_processes():

    seed = 273142
    random.seed(seed)

    data = []

    output_name = "process_data"

    processes_num = data_handler.get_integer_input("Give the number of processes to generate: ")
    max_proc_arrival = data_handler.get_integer_input("Give the max arrival time for the process: ")
    max_proc_length = data_handler.get_integer_input("Give the max length of the process: ")

    for i in range(int(processes_num)):
        proc_id = i+1
        proc_arrival = random.randint(1, max_proc_arrival)
        proc_length = random.randint(1, max_proc_length)
        data.append({"id": proc_id, "arrival_time": proc_arrival, "burst_time": proc_length})

    data_handler.generator_data(data, output_name)
