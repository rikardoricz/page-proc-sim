import os
import sys
import random
dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent_dir)
import data_handler

def generate_pages():
    seed = 273142
    random.seed(seed)

    output_name = "page_data"
    data = {
        "sizes":[0],
        "pages":[0]
    }
    data["sizes"] = [data_handler.get_integer_input("Enter slot size: ") for _ in range(data_handler.get_integer_input("Enter the number of slots: "))]

    pages_num = data_handler.get_integer_input("How many pages: ")

    sample_range = data_handler.get_integer_input("What should the sample range be: ")


    for x in range(1, int(pages_num)):
        data["pages"].extend([random.randint(1, sample_range)])

    data_handler.generator_data(data, output_name)
