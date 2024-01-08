import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
import data_handler

def get_output_json(filename):
    output_file_path = "output/" + filename + ".json"
    if os.path.exists(output_file_path):
        json_data = data_handler.read_data(output_file_path)
        return json_data
    else:
        print("That file doesn't exist in the output/ directory")
        exit(-1)

def plot_process_results():
    json_data_fcfs = get_output_json("fcfs_out")
    json_data_sjf = get_output_json("sjf_out")

    avg_waiting_fcfs = json_data_fcfs[-1]["results"]["average_waiting_time"]
    avg_waiting_sjf = json_data_sjf[-1]["results"]["average_waiting_time"]

    data_frame = pd.DataFrame({"Algorithm": ["FCFS", "SJF"], "Average Waiting Time": [avg_waiting_fcfs, avg_waiting_sjf]})

    plt.figure(figsize=(8, 6))
    plt.bar(data_frame["Algorithm"], data_frame["Average Waiting Time"], color=['blue', 'orange'])
    plt.title('Average waiting time comparison')
    plt.xlabel('Algorithm')
    plt.ylabel('Average Waiting Time')

    plt.savefig('output/process_sched_plots.png', bbox_inches='tight')
    plt.show()

#plot_process_results()
