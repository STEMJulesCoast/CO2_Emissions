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

- `ne_10m_admin_0_countries`: Contains the shapefile for spatial mapping of emissions.
- `CO2_emission_visualization.ipynb`: A Python script for visualizing CO2 data from the EDGAR database.
- `Übungen`: (in german) Includes a set of notebooks that introduce modular programming concepts. It features a separate notebook for loading and processing data, as well as modules for plotting functions, to enhance code readability and facilitate learning programming through the adjustment of code snippets. A `requirements.txt` file is provided to install the necessary libraries. The main notebook executes this separate notebook for data loading and processing within its execution, making the code more organized and offering a practical introduction to the concepts of code reuse and modularity.


### Installation and Use

To use the visualization script, certain libraries need to be installed and imported. The script includes functions for installing missing libraries, loading and processing emission data, spatially aggregating emissions at the country level, and creating various visualizations.

### Instructions

1. **Clone the Repository:** Clone the entire repository to your local computer. This gives you access to all files and folders in the project.

2. **Prepare Your Environment:** Ensure Python and Jupyter (Lab or Notebook) are installed on your system to run the `.ipynb` files.

3. **Install the Required Packages:** The notebook includes a function that installs missing libraries. If this does not work, navigate to the project directory containing the `requirements.txt` file and run `pip install -r requirements.txt` to install all needed libraries and adjust the import in the notebook accordingly.

4. **Execution of Scripts:** Open the visualization script in Jupyter Lab or Jupyter Notebook. Note that adjustments may be required if using a different environment.
