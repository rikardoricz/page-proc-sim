import data_handler
import os
from page import Page
from log import Log
from collections import deque

# klasa odpowiedzialna za algorytmy zastepowania stron
class PageReplacement:
    def __init__(self, algo_name):
        self.algo_name = algo_name
        self.log = Log(algo_name)
        self.pages = []
        self.frame_sizes = []

    # tworzenie stron - odczyt z pliku input/page_data.json i dodanie dnaych do strukur (pól klasy) pages i frame_sizes
    def create_pages(self):
        if os.path.exists("input/page_data.json"):
            data = data_handler.read_data("input/page_data.json")
        else:
            print("that file doesn't exist in the input/ directory")
            exit(-1)

        for frame_size in data['sizes']:
            self.frame_sizes.append(frame_size)

        for page in data['pages']:
            self.pages.append(Page(page))

    # symulacja algorytmu fifo. Zwraca page_faults (ilosc zastapien stron) i page_hits
    def fifo(self, capacity):
        queue = deque()
        page_faults = 0
        page_hits = 0
        for page in self.pages:
            if page.id not in queue:
                page_faults += 1
                if len(queue) == capacity:
                    queue.popleft()
                queue.append(page.id)
            else:
                page_hits += 1
        return page_faults, page_hits

    # symulacja algorytmu lru. Zwraca page_faults (ilosc zastapien stron) i page_hits
    def lru(self, capacity):
        queue = []
        page_faults = 0
        page_hits = 0
        for page in self.pages:
            if page.id not in queue:
                if(len(queue) == capacity):
                    queue.remove(queue[0])
                    queue.append(page.id)
                else:
                    queue.append(page.id)
                page_faults += 1
            else:
                queue.remove(page.id)
                queue.append(page.id)
                page_hits += 1
        return page_faults, page_hits


    # symulacja obu algorytmow - fifo i lru i zapisywanie za pomoca loggera
    def simulate(self):
        self.create_pages()

        for capacity in self.frame_sizes:
            print('\nFRAME SIZE ', capacity)
            if self.algo_name == "fifo":
                page_faults, page_hits = self.fifo(capacity)
                self.log.log_page_faults(capacity, page_faults)
                print('FIFO faults:', page_faults)
                print('FIFO hits:', page_hits)
            else:
                page_faults, page_hits = self.lru(capacity)
                self.log.log_page_faults(capacity, page_faults)
                print('LRU faults:', page_faults)
                print('LRU hits:', page_hits)

