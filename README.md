# Simulation project for page replacement and process scheduling algorithms

This repo features a simulation project for page replacement algorithms (FIFO and LRU) and process scheduling algorithms (FCFS and SJF).

## Requirements

- Python 3

## Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/rikardoricz/page-proc-sim.git
   ```
2. Navigate to the project directory:
    ```bash
    cd page-proc-sim
    ```
3. Run the project:
    ```bash
    python main.py
    ```
4. Follow the on-screen menu to choose the algorithm or generator you want to launch:
    ```bash
    What algorithm do you want to launch?

    Process scheduling:
    1. FCFS
    2. SJF
    Page replacement:
    3. FIFO
    4. LRU
    Generators:
    5: Generate processes
    6: Generate pages
    7. Exit

    (1-7):
    ```

## Project structure
- `main.py`: The main script to run the simulation.
- `data_handler.py`: Module containing data hander (read from input json and write to output json)
- `process_scheduling.py`: Module containing implementations for process scheduling algorithms (FCFS, SJF).
- `page_replacement.py`: Module containing implementations for page replacement algorithms (FIFO, LRU).
- `gen/process_data_generator.py`: Module containing data generators for processes.
- `gen/page_data_generator.py`: Module containing data generator for pages.
- `log.py`: Module containing logger
- `page.py`: Page class
- `process.py`: Process class
- `ticker.py`: Ticker class
- `input/`: Directory containing input json with generated data for processes and pages
- `output/`: Directory containing results of process scheduling and page replacement algorithms

# License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.
