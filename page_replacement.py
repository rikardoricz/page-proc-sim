import data_handler
import os
from page import Page
from log import Log
from collections import deque

class PageReplacement:
    def __init__(self, algo_name):
        self.algo_name = algo_name
        self.log = Log(algo_name)
        self.pages = []
        self.frame_sizes = []
        self.faults = 0

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

    def fifo(self, capacity):
        print("FIFO function")
        queue = deque()
        page_faults = 0
        page_hits = 0
        for page in self.pages:
            if page.id not in queue:
                page_faults += 1
                #print("page id fault: ", page.id, page_faults)
                if len(queue) == capacity:
                    #print("pop")
                    queue.popleft()
                queue.append(page.id)
                #print("append")
            else:
                page_hits += 1
        print("faults:", page_faults)
        print("hits:", page_hits)
        return page_faults

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
        print("faults:", page_faults)
        print("hits:", page_hits)
        return page_faults


    def simulate(self):
        self.create_pages()

        for capacity in self.frame_sizes:
            if self.algo_name == "fifo":
                page_faults = self.fifo(capacity)
                self.log.log_page_faults(capacity, page_faults)
                print('FIFO faults:', page_faults)
            else:
                page_faults = self.lru(capacity)
                self.log.log_page_faults(capacity, page_faults)
                print('LRU faults:', page_faults)

#if __name__ == "__main__":
#    fifo = PageReplacement("fifo")
#    lru = PageReplacement("lru")
#    fifo.simulate()
#    lru.simulate()
