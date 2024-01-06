from process_sched import ProcessSched
from page_replacement import PageReplacement
from gen import page_data_generator, process_data_generator

def menu():
    print("\nWhat algorith you want to launch?")
    print("Process scheduling:")
    print("1. FCFS")
    print("2. SJF")
    print("Page replacement:")
    print("3. FIFO")
    print("4. LRU")
    print("Generators:")
    print("5: Generate processes")
    print("6: Generate pages")
    print("7. Exit")

    choice = int(input('(1-5):'))
    if choice == 1:
        fcfs = ProcessSched("fcfs")
        fcfs.simulate()
    elif choice == 2:
        sjf = ProcessSched("sjf")
        sjf.simulate()
    elif choice == 3:
        fifo = PageReplacement("fifo")
        fifo.simulate()
    elif choice == 4:
        lru = PageReplacement("lru")
        lru.simulate()
    elif choice == 5:
        process_data_generator.generate_processes()
    elif choice == 6:
        page_data_generator.generate_pages()
    elif choice == 7:
        pass
    else:
        print("Wrong input")
        menu()

if __name__ == "__main__":
    menu()
