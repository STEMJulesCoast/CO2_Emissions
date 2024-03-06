# Visualizing CO2 Emissions with EDGAR Data

### About This Project

This repository offers detailed visualization of CO2 emissions based on data from the EDGAR (Emission Database for Global Atmospheric Research) Community Greenhouse Gas database Version 8.0 (2023), including or based on data from IEA (2022) greenhouse gas emissions from energy.

### Source

The data used comes from the IEA-EDGAR CO2 database. For more information and data, visit: https://edgar.jrc.ec.europa.eu/report_2023

### Interactive Visualizations Created with Plotly:

- Top 10 CO2 Emitters: https://chart-studio.plotly.com/~julia_koehler_nat/1.embed
- Annual Top 10 CO2 Emitters: https://chart-studio.plotly.com/~julia_koehler_nat/5.embed
- CO2 Emissions in Germany and Global Annual Average: https://chart-studio.plotly.com/~julia_koehler_nat/3.embed

### Repository Content

- `Data\ne_10m_admin_0_countries`: Contains the shapefile for spatial mapping of emissions.
- `CO2_emission_visualization.ipynb`: A Notebook for visualizing CO2 data from the EDGAR database.
- `CO2_emission_visualization.py`: A Python script for visualizing CO2 data from the EDGAR database.
- `requirements.txt`: file to install the necessary libraries.
- `Übungen`: (in german) Includes a set of notebooks that introduce modular programming concepts. It features a separate notebook for loading and processing data, as well as modules for plotting functions, to enhance code readability and facilitate learning programming through the adjustment of code snippets. The main notebook executes this separate notebook for data loading and processing within its execution, making the code more organized and offering a practical introduction to the concepts of code reuse and modularity.


### Installation and Use

## Installation

### With Anaconda (Recommended)

Running the Jupyter Notebooks is best done by installing Anaconda, with at least Python 3.11 recommended. Anaconda simplifies package management and the setup of virtual environments. You can download and install Anaconda from [here](https://www.anaconda.com/products/individual).

### Without Anaconda

If Anaconda is not installed or you prefer not to use Anaconda, Python 3.10 is required. Additionally, the packages listed in the `requirements.txt` file need to be installed. The use of a virtual environment (`venv`) is recommended to isolate package dependencies and avoid conflicts.


### Instructions

1. **Clone the Repository:** Clone the entire repository to your local computer. This gives you access to all files and folders in the project.

2. **Prepare Your Environment:** Ensure Python and Jupyter (Lab or Notebook) are installed on your system to run the `.ipynb` files.

3. **Install the Required Packages:** Navigate to the project directory containing the `requirements.txt` file and run 

 ```
    pip install -r requirements.txt
 ```

to install all needed libraries.

4. **Execution of Scripts:** Open the visualization script in Jupyter Lab or Jupyter Notebook. Note that adjustments may be required if using a different environment.
