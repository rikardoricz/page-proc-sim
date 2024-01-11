import json
import os

# funkcja zwraca wartosc jezeli podany argument jest dodatnia liczba calkowita, w przeciwnym wypadku wyrzuca blad
def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                raise ValueError("Input must be a positive integer.")
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}")

# zapis do pliku json po podaniu w argumencie sciezki, nazwy pliku i danych
def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), "w") as f:
        json.dump(data, f, indent=4)

# sprawdzenie czy plik jest plikiem z rozszerzeniem .json
def is_json_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == ".json"

# funkcja zwraca odczytane dane z pliku do ktorego sciezka jest podana jako argument
def read_data(data_path):
    with open(data_path) as f:
        return json.load(f)

# zapis pliku json do katalogu output/
def write_data(data, name):
    write_json("output/", name + ".json", data)

# zapis pliku json do katalogu input/
def generator_data(data, name):
    write_json("input/", name + ".json", data)
