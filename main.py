import os
import data_handler
from process_sched import ProcessSched
from page_replacement import PageReplacement
from gen import page_data_generator, process_data_generator
from plots import page_results_plotter, process_results_plotter

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while(True):
        print("\nWhat algorithms you want to launch?\n")
        print("1. FCFS and SJF - Process scheduling")
        print("2. FIFO and LRU - Page replacement")
        print("\nGenerators:")
        print("3: Generate processes")
        print("4: Generate pages")
        print("5. Exit")

        choice = data_handler.get_integer_input("\n(1-5):")
        if choice == 1:
            fcfs = ProcessSched("fcfs")
            sjf = ProcessSched("sjf")
            fcfs.simulate()
            sjf.simulate()
            process_results_plotter.plot_process_results()
        elif choice == 2:
            fifo = PageReplacement("fifo")
            lru = PageReplacement("lru")
            fifo.simulate()
            lru.simulate()
            page_results_plotter.plot_page_results()
        elif choice == 3:
            process_data_generator.generate_processes()
        elif choice == 4:
            page_data_generator.generate_pages()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            clear_console()
            print("Wrong input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
