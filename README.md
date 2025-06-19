
# Reservoir Optimization Model using Particle Swarm Optimization (PSO)

## Overview
This project implements a reservoir operation optimization model using the Particle Swarm Optimization (PSO) algorithm. The model aims to optimize water release schedules to maximize energy production while satisfying constraints such as storage limits, environmental flow requirements, and turbine discharge capacities. The simulation is designed for a 12-month period, accounting for seasonal variations (dry and wet seasons), and includes visualization of power generation and reservoir storage.

## Features
- **PSO Algorithm**: Optimizes water release schedules to maximize energy production.
- **Energy Production**: Calculates dry and wet season energy output in GWh.
- **Constraints Handling**: Enforces minimum and maximum storage, environmental flows, and turbine discharge limits.
- **Visualization**: Plots power generation and reservoir storage over time using Matplotlib.
- **Monthly Reporting**: Provides detailed monthly reports for simulations up to 12 months.

## Prerequisites
To run this project, you need the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`

You can install these dependencies using pip:
```bash
pip install numpy pandas matplotlib
```

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repository-name
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (Note: Create a `requirements.txt` file with the dependencies listed above if not already present.)

## Usage
1. Ensure all Python scripts (`main_june.py`, `utils_june.py`, `fitness_june.py`, `psocheck.py`, `process_june.py`) are in the same directory.
2. Run the main script:
   ```bash
   python main_june.py
   ```
3. The program will:
   - Optimize water releases using PSO.
   - Calculate energy production and storage dynamics.
   - Display a summary of energy production (dry, wet, and total).
   - Generate plots for power generation and reservoir storage.
   - Print a detailed monthly report for the 12-month simulation.

## File Structure
- **`main_june.py`**: Entry point of the program. Runs PSO optimization and processes results.
- **`utils_june.py`**: Contains utility functions, constants, and data (e.g., inflows, storage limits, power calculations).
- **`fitness_june.py`**: Defines the fitness function for PSO, evaluating release schedules based on deficits and constraint violations.
- **`psocheck.py`**: Implements the PSO algorithm to find the optimal release schedule.
- **`process_june.py`**: Processes the optimized release schedule, calculates energy production, and generates plots and reports.
- **`README.md`**: Project documentation (this file).

## Key Parameters
- **Simulation Period**: 12 months (T = 12).
- **Inflows**: Monthly inflow data (Nov-Oct) in m³/s, converted to million m³.
- **Storage Limits**: Minimum (2242 million m³) and maximum (4467 million m³) reservoir storage.
- **Demand**: Minimum (112 m³/s) and maximum (672 m³/s) turbine discharge.
- **Dry Months**: December to May (indices 1 to 6).
- **Operation Hours**: 12 hours per day (H = 12).
- **PSO Parameters**:
  - Number of particles: 500
  - Iterations: 200
  - Inertia weight: 0.9 to 0.4
  - Cognitive and social parameters: Adaptive (c1: 2.5 to 0.5, c2: 0.5 to 2.5)

## Outputs
- **Console Output**:
  - Energy production summary (dry, wet, and total in GWh).
  - Detailed monthly report (inflows, releases, storage, power).
  - Average annual release in million m³.
- **Plots**:
  - Power generation over time (MW).
  - Reservoir storage over time (million m³) with min/max storage lines.

## Notes
- The model assumes no evapotranspiration (`pet = 0`) and no environmental flow requirements (`env_flow = 0`).
- Unit conversions are handled using `conv` (for inflows) and `cnv_` (for releases and power calculations).
- The fitness function penalizes violations of storage limits, environmental flows, and demand deficits.
- The PSO algorithm uses adaptive inertia weight and cognitive/social parameters to improve convergence.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure your code follows the existing style and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or issues, please open an issue on GitHub or contact the repository owner.
