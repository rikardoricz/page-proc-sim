import json
import os

def read_data(data_path):
    with open(data_path) as f:
        return json.loads(f)

def write_data(data, name):
    with open("output/" + name + ".json", "w") as f:
        json.dumps(data, f, indent=4)

def generator_data(data, output_name):
    with open(output_name, "w") as file:
        json.dump(data, file, indent=4)
        # json_object = json.dumps(data, file, indent=4)

# generator_data([{"id": 1, "arrival_time": 0, "burst_time": 10},{"id": 2, "arrival_time": 2, "burst_time": 5},{"id": 3, "arrival_time": 4, "burst_time": 8},{"id": 4, "arrival_time": 6, "burst_time": 2}], "dupa")
