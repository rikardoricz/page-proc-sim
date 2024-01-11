import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
import data_handler

# funkcja zwraca dane json korzystajac z modulu data_handler, a przed tym sprawdza czy plik istnieje w katalogu output
def get_output_json(filename):
    output_file_path = "output/" + filename + ".json"
    if os.path.exists(output_file_path):
        json_data = data_handler.read_data(output_file_path)
        return json_data
    else:
        print("That file doesn't exist in the output/ directory")
        exit(-1)

# funkcja rysujaca wykres dla rezultatow wykonania algorytmow zastepowania stron. Wykres jest eksportowany do katalogu output/
def plot_page_results():
    json_data_fifo = get_output_json("fifo_out")
    json_data_lru = get_output_json("lru_out")

    data_frame_fifo = pd.DataFrame(json_data_fifo)
    data_frame_lru = pd.DataFrame(json_data_lru)

    data_frame = pd.merge(data_frame_fifo, data_frame_lru, on='frame_size', suffixes=('_FIFO', '_LRU'))

    plt.figure(figsize=(20, 6))

    bar_width = 0.35
    bar_positions = range(len(data_frame['frame_size']))

    plt.bar(bar_positions, data_frame['page_faults_FIFO'], width=bar_width, label='FIFO', align='center', color='blue')
    plt.bar([p + bar_width for p in bar_positions], data_frame['page_faults_LRU'], width=bar_width, label='LRU', align='center', color='orange')

    plt.title('Page Faults comparison')
    plt.xlabel('Frame Size')
    plt.ylabel('Page Faults')
    plt.xticks([p + bar_width / 2 for p in bar_positions], data_frame['frame_size'])
    plt.legend()
    plt.grid(True)

    plt.savefig('output/page_replacement_plots.png', bbox_inches='tight')
    plt.show()

#plot_page_results()
