import data_handler

class Log:
    def __init__(self, algorithm):
        self.filename = algorithm
        self.logs = []

    def log_process(self, id, waiting_time, finish_time):
        process_log = {
            'id': id,
            'waiting_time': waiting_time,
            'finish_time': finish_time
        }
        self.logs.append(process_log)

    def log_process_final(self, avg_waiting_time, total_time):
        self.logs.append({
            'average_waiting_time': avg_waiting_time,
            'total_time': total_time
        })
        data_handler.write_data(self.logs, self.filename+"_out")

    #def log_pages(self, pages_part):
        #TODO: write processed data to json

