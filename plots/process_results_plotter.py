import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
import data_handler

# funkcja tworzaca latwiejsza do odczytania strukture danych na podstawie danych json i nazwy algorytmu do pozniejszego narysowania wykresu
def process_algorithm_data(json_data, algorithm_name):
    results = json_data[-1]["results"]
    data = {
        "Algorithm": algorithm_name,
        "Avg Waiting Time": results["average_waiting_time"],
        "Avg Turnaround Time": results["average_turnaround_time"]
    }
    return data

# funkcja zwraca dane json korzystajac z modulu data_handler, a przed tym sprawdza czy plik istnieje w katalogu output
def get_output_json(filename):
    output_file_path = "output/" + filename + ".json"
    if os.path.exists(output_file_path):
        json_data = data_handler.read_data(output_file_path)
        return json_data
    else:
        print("That file doesn't exist in the output/ directory")
        exit(-1)

# funkcja rysujaca wykres dla rezultatow wykonania algorytmow planowania czasu procesora. Wykres jest eksportowany do katalogu output/
def plot_process_results():
    json_data_fcfs = get_output_json("fcfs_out")
    json_data_sjf = get_output_json("sjf_out")

    fcfs_data = process_algorithm_data(json_data_fcfs, "FCFS")
    sjf_data = process_algorithm_data(json_data_sjf, "SJF")

    df_fcfs = pd.DataFrame([fcfs_data])
    df_sjf = pd.DataFrame([sjf_data])

    df_combined = pd.concat([df_fcfs, df_sjf], ignore_index=True)

    plt.figure(figsize=(10, 6))

    bar_width = 0.35
    bar_positions_waiting = range(len(df_combined['Algorithm']))
    bar_positions_turnaround = [p + bar_width for p in bar_positions_waiting]

    plt.bar(bar_positions_waiting, df_combined['Avg Waiting Time'], width=bar_width, label='Avg Waiting Time', align='center', color='blue')
    plt.bar(bar_positions_turnaround, df_combined['Avg Turnaround Time'], width=bar_width, label='Avg Turnaround Time', align='center', color='orange')

    plt.xlabel('Algorithm')
    plt.ylabel('Time')
    plt.title('Average waiting time and average turnaround time comparison')
    plt.xticks([p + bar_width / 2 for p in bar_positions_waiting], df_combined['Algorithm'])
    plt.legend()
    plt.grid(True)

    plt.savefig('output/process_sched_plots.png', bbox_inches='tight')
    plt.show()
