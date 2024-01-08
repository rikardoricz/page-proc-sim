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
    What algorithms you want to launch?

    1. FCFS and SJF - Process scheduling
    2. FIFO and LRU - Page replacement

    Generators:
    3: Generate processes
    4: Generate pages
    5. Exit

    (1-5):
    ```

## Project structure
- `main.py`: The main script to run the simulation.
- `data_handler.py`: Module containing data hander (read from input json and write to output json)
- `process_scheduling.py`: Module containing implementations for process scheduling algorithms (FCFS, SJF).
- `page_replacement.py`: Module containing implementations for page replacement algorithms (FIFO, LRU).
- `gen/process_data_generator.py`: Module containing data generators for processes.
- `gen/page_data_generator.py`: Module containing data generator for pages.
- `plots/process_results_plotter.py`: Module containing results plotter for process scheduling algorithms.
- `gen/page_results_plotter.py`: Module containing results plotter for page replacement algorithms.
- `log.py`: Module containing logger
- `page.py`: Page class
- `process.py`: Process class
- `ticker.py`: Ticker class
- `input/`: Directory containing input json with generated data for processes and pages
- `output/`: Directory containing results of process scheduling and page replacement algorithms (raw data in json and plots)

# License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.
