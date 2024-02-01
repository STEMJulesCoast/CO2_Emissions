# CO2 Emission Visualization with EDGAR Data

### About This Project

This repository offers a detailed visualization of CO2 emissions based on data from the EDGAR (Emissions Database for Global Atmospheric Research) Community Greenhouse Gas database Version 8.0 (2023), including or based on data from IEA (2022) Greenhouse Gas Emissions from Energy.

### Source

The data used comes from the IEA-EDGAR CO2 database. Further information and data can be found here: https://edgar.jrc.ec.europa.eu/report_2023

### Interactive Visualizations Created with Plotly:

    Top 10 CO2 Emitters: https://chart-studio.plotly.com/~julia_koehler_nat/1.embed
    Yearly Top 10 CO2 Emitters: https://chart-studio.plotly.com/~julia_koehler_nat/5.embed
    CO2 Emissions in Germany and Global Annual Average: https://chart-studio.plotly.com/~julia_koehler_nat/3.embed

### Repository Contents

    ne_10m_admin_0_countries: Contains the shapefile for spatial mapping of emissions.
    CO2_emission_visualization.ipynb: A Python script for visualizing CO2 data from the EDGAR database.

### Installation and Usage

To use the visualization script, certain libraries need to be installed and imported. The script includes functions for installing missing libraries, loading and processing emission data, spatially aggregating emissions at the country level, and creating various visualizations.
Step-by-Step Guide

    Clone the repository.
    Run the visualization script in a Python environment.
    Check the generated plots and data.
