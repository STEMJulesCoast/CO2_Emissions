# %% 
# ### Visualization of Global CO2 Emissions
# 
# The EDGAR Database (Emissions Database for Global Atmospheric Research) is a comprehensive source for emissions data.
# 
# Content of the Data: The EDGAR v8.0 dataset offers estimates of emissions for the three main greenhouse gases (CO2, CH4, N2O) and fluorinated gases, categorized by sectors and countries. For CO2 emissions, there are distinct figures for fossil and biogenic components. We utilize the gridmaps of total CO2 emissions with a resolution of 0.1x0.1° on a global level.
# 
# For the global maps, the most recent year included in the dataset (in this case, 2022) is visualized, while the analysis of the top and bottom 10 emitters uses the sum of emissions from 1970-2022.
# 
# Independent Estimates: The data in EDGAR are independent estimates compared to emissions reported by European member states or under the United Nations Framework Convention on Climate Change. They are based on international statistics and a consistent IPCC methodology.
# 
# Source: IEA-EDGAR CO2, a component of the EDGAR (Emissions Database for Global Atmospheric Research) Community Greenhouse Gas database Version 8.0 (2023), includes or is based on data from IEA (2022) Greenhouse Gas Emissions from Energy, www.iea.org/data-and-statistics, as modified by the Joint Research Centre. For download and more information: EDGAR Report 2023 (https://edgar.jrc.ec.europa.eu/report_2023)

# %%


# Necessary imports 
import warnings
warnings.filterwarnings("ignore")

import re
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd
import cartopy.crs as ccrs
import pandas as pd
import os
import zipfile
import tempfile
import requests
from tqdm import tqdm
import matplotlib.colors as mcolors
from matplotlib.colors import LogNorm
import plotly.express as px
import plotly.graph_objects as go
import shutil
import rioxarray


url = "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v80_FT2022_GHG/CO2/TOTALS/TOTALS_emi_nc.zip"
# Define the path to the shapefile for calculating emissions by country
PATH_SHAPEFILE = os.path.abspath(os.path.join('Data', 'ne_10m_admin_0_countries', 'ne_10m_admin_0_countries.shp'))


print("All modules successfully imported!")

local_zip_path = os.path.abspath(os.path.join('Data', 'TOTALS_emi_nc.zip'))
extraction_path = os.path.abspath(os.path.join('Data', 'Temp'))


# Check if the extracted data already exists
nc_files_exist = os.listdir(extraction_path) if os.path.exists(extraction_path) else []

# Only proceed with download and extraction if no extracted .nc files are found
if not nc_files_exist:
    # Ensure the extraction directory exists
    if not os.path.exists(extraction_path):
        os.makedirs(extraction_path)

    # Check if the ZIP file exists locally; if not, download it
    if not os.path.exists(local_zip_path):
        # Make directory if it does not exist
        os.makedirs(os.path.dirname(local_zip_path), exist_ok=True)
        print("Downloading ZIP file...")
        response = requests.get(url)  # Ensure 'url' is defined somewhere above this line
        with open(local_zip_path, 'wb') as f:
            f.write(response.content)
        print("Download completed.")

    # Extract the ZIP file
    with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
        print("Extraction completed.")
else:
    print("Data already exists. Skipping download and extraction.")

 # Extract year from file name and sort files by year
def extract_year_from_filename(filename):
    match = re.search(r"_\d{4}_", filename)
    return int(match.group(0)[1:-1]) if match else None

nc_files = [os.path.join(extraction_path, file) for file in os.listdir(extraction_path) if file.endswith('.nc')]

nc_files_sorted = sorted(nc_files, key=lambda x: extract_year_from_filename(x))

# Load .nc data in chronological order
ds_all = xr.open_mfdataset(nc_files_sorted, combine='nested', concat_dim='time', use_cftime=True)

# Assuming the files cover a continuous range of years, from start_year to end_year
start_year = extract_year_from_filename(nc_files_sorted[0])
end_year = extract_year_from_filename(nc_files_sorted[-1])
time_coord = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='YS')

# Assign time coordinate to dataset
ds_all = ds_all.assign_coords(time=('time', time_coord))

# ### Extract relevant years and calculate difference

# %%
# choose 1990 and 2022
co2_1990 = ds_all.sel(time='1990-01-01')
co2_2022 = ds_all.sel(time='2022-01-01')

# extract emission data
emissions_1990 = co2_1990.variables['emissions'][:]
emissions_2022 = co2_2022.variables['emissions'][:]

# calculate difference most actual year minus base year
emissions_diff = emissions_2022 - emissions_1990

lat = ds_all.lat[:]
lon = ds_all.lon[:]
lon, lat = np.meshgrid(lon, lat)



# %% [markdown]
# ### Plot CO2 emissions 2022

# %%
emissions_2022 = emissions_2022.compute()

fig, ax = plt.subplots(figsize=(8, 5.6),
    subplot_kw={'projection': ccrs.Robinson()},
    dpi=300
)
ax.patch.set_facecolor('black')
fig.patch.set_alpha(0) 
#logarithmic normalization

norm = LogNorm(vmin=max(emissions_2022.min(), 1e-1), vmax=emissions_2022.max())



# plot
mesh = ax.pcolormesh(lon, lat, emissions_2022, cmap='afmhot', norm=norm, transform=ccrs.PlateCarree())

# colorbar
cbar = fig.colorbar(mesh, ax=ax, orientation='vertical', extend='both', 
                    shrink=0.5, aspect=20,  
                    extendfrac='auto') 
cbar.set_label('[Tonnen/Jahr]', fontsize=10, color='black')


# coastlines
ax.coastlines(color='dimgray', linewidth=0.5)

plt.savefig('CO2_2022.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show(block=False)
plt.pause(5) 


# %% [markdown]
# ### Plot difference 2022 - 1990

# %%
def make_colormap(seq):
    seq = [(None, *s) if len(s) == 2 else s for s in seq]
    cdict = {'red': [], 'green': [], 'blue': [], 'alpha': []}
    for pos, color, alpha in seq:
        r, g, b = mcolors.to_rgb(color)
        cdict['red'].append((pos, r, r))
        cdict['green'].append((pos, g, g))
        cdict['blue'].append((pos, b, b))
        cdict['alpha'].append((pos, alpha, alpha))
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

# define colormap
seq = [(0, 'blue', 1), (0.4, 'blue', 0.5), (0.49, 'black', 1), 
       (0.5, 'black', 1), (0.51, 'black', 1), (0.6, 'red', 0.5), 
       (1, 'red', 1)]

custom_cmap = make_colormap(seq)

# normalization
norm = mcolors.TwoSlopeNorm(vmin=-8000, vcenter=0, vmax=8000)


fig, ax = plt.subplots(figsize=(8, 5.6), subplot_kw={'projection': ccrs.Robinson()}, dpi=300)
fig.patch.set_alpha(0) 
# plot
mesh = ax.pcolormesh(lon, lat, emissions_diff, cmap=custom_cmap, norm=norm, transform=ccrs.PlateCarree())

# colorbar
cbar = fig.colorbar(mesh, ax=ax, orientation='vertical', extend='both', shrink=0.5)
cbar.set_label('[Tonnen/Jahr]', fontsize=10)

# coastlines and title
ax.coastlines(color='dimgray', linewidth=0.5)
#plt.title('CO2 Emissionen Differenz 2022 - 1990', fontsize=10)

#
plt.savefig('Diff_2022_1990.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show(block=False)
plt.pause(5) 


# %% [markdown]
# ### Load shapefile and aggregate data by country

# %%
#read shapefile
countries_gdf = gpd.read_file(PATH_SHAPEFILE)

# convert in rioxarray-object
emissions_rio = ds_all['emissions'].rio.set_spatial_dims(x_dim='lon', y_dim='lat', inplace=True)
emissions_rio.rio.write_crs("epsg:4326", inplace=True)

# spatial aggregation
country_emissions = {}
for index, row in countries_gdf.iterrows():
    country_name = row['NAME']
    country_geom = row['geometry']
    try:
        clipped = emissions_rio.rio.clip([country_geom], countries_gdf.crs)
        country_emissions[country_name] = clipped.sum(dim=['lat', 'lon'])
    except rioxarray.exceptions.NoDataInBounds:
        print(f"No data for {country_name}.")
 
print('Data successfully aggregated')

data = []
for country, emissions in country_emissions.items():
    # extract yearly emissions by country
    annual_emissions = emissions.values
    for year, emission in zip(range(1970, 2023), annual_emissions):
        data.append({'country': country, 'year': year, 'emission': emission})

# get dataframe
df_emissions = pd.DataFrame(data)

print('Created DataFrame from emission data')
# %%

# sort data
top_10_emitters = df_emissions.groupby('country')['emission'].sum().nlargest(10)
bottom_10_emitters = df_emissions.groupby('country')['emission'].sum().nsmallest(10)

top_10_emitters = top_10_emitters.reset_index()
bottom_10_emitters = bottom_10_emitters.reset_index()

# plotly diagram for top 10 emittents
fig_top = px.bar(top_10_emitters, x='country', y='emission')
fig_top.update_yaxes(exponentformat='e')
fig_top.update_layout(
    title='Top 10 CO2-Emittenten (Summe 1970-2022)',
    xaxis_title='Jahr',
    yaxis_title='CO2-Emissionen (Tonnen)',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    xaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5),
    yaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5, tickformat='.0e')
)
fig_top.update_xaxes(showline=True, linewidth=1, linecolor='grey')
fig_top.update_yaxes(showline=True, linewidth=1, linecolor='grey')

fig_top.show()

# plotly diagram for bottom 10 emittents
fig_bottom = px.bar(bottom_10_emitters, x='country', y='emission')
fig_bottom.update_layout(
    title='Bottom 10 CO2 Emittenten (Summe 1970 - 2022)',
    xaxis_title='Jahr',
    yaxis_title='CO2-Emissionen (Tonnen)',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    xaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5),
    yaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5, tickformat='.0e')
)
fig_bottom.update_xaxes(showline=True, linewidth=1, linecolor='grey')
fig_bottom.update_yaxes(showline=True, linewidth=1, linecolor='grey')

fig_bottom.show()

print('Next: Calculate most emissions')
# %%
def most_emissions(df):
    # Create an empty container for dropdown menu options
    item_list = []

    # Iterate over the rows (years) in the DataFrame
    for year in df.index:
        # Sort the DataFrame for the current year and select the top 10 countries
        df_sorted = df.loc[year].sort_values(ascending=False).head(10)

        # Create an entry for the dropdown menu
        item = dict(args=[{"y": [df_sorted.values], "x": [df_sorted.index]},
                          {"title": f"Top 10 CO2 Emitters in {year}"}],
                    label=str(year), method="update")
        item_list.append(item)

    # Create the initial chart
    first_year = df.index[0]
    first_viz = df.loc[first_year].sort_values(ascending=False).head(10)
    fig = px.bar(first_viz, y=first_viz.values, x=first_viz.index,
                 title=f"Top 10 CO2 Emitters in {first_year}")

    # Add the dropdown menu to the chart
    fig.update_layout(
        updatemenus=[
            dict(buttons=list(item_list),
                 direction="down", showactive=True, x=0.005,
                 xanchor="left", y=1.15, yanchor="top")
        ]
    )

    # Adjust the layout
    fig.update_layout(
        plot_bgcolor='black',  # Black background for the chart area
        paper_bgcolor='black',  # Black background for the entire figure
        font_color='white',  # White font color
        xaxis=dict(showgrid=True, gridcolor='darkgrey', gridwidth=0.5),  # Settings for the X-axis
        yaxis=dict(showgrid=True, gridcolor='darkgrey', gridwidth=0.5, tickformat='.0e', range=[0, 6e9])  # Settings for the Y-axis
    )

    fig.update_xaxes(showline=True, linewidth=1, linecolor='darkgrey')  # Lines for the X-axis
    fig.update_yaxes(showline=True, linewidth=1, linecolor='darkgrey')  # Lines for the Y-axis
    fig.update_xaxes(title_text='Country')  # Label for the X-axis
    fig.update_yaxes(title_text='CO2 Emissions (Tons)')  # Label for the Y-axis

    return fig

# %%
#create a dataframe
print('Creating a dataframe for the interactive plot - this may take some time. Grab a coffee/tea, or have a little chat.')

data = {}
for country, emissions in country_emissions.items():
    data[country] = emissions.to_pandas()

df_most = pd.DataFrame(data)
df_most
df_most.index = pd.to_datetime(df_most.index).year


# %% [markdown]
# ### Plot Top 10 CO2 emittents per year 
print('Plot')
# %%
fig = most_emissions(df_most.tail(25))
fig.show()

print('Done')

# %% [markdown]
# ### Calculate and plot timeseries of yearly global mean emissions and yearly sum of Germany emissions

# %%
# global yearly mean
df_global_mean = df_emissions.groupby('year')['emission'].mean().reset_index()

# rename column
df_global_mean.rename(columns={'emission': 'global_mean_emission'}, inplace=True)

# %%
#choose  country
df_germany = df_emissions[df_emissions['country'] == 'Germany']
df_germany

# %%
#plot yearly emissions
fig = go.Figure()

fig.add_trace(go.Bar(x=df_germany['year'], y=df_germany['emission'], name='Emissionen Deutschland'))
fig.add_trace(go.Scatter(x=df_global_mean['year'], y=df_global_mean['global_mean_emission'], name='Globales Mittel'))
fig.update_yaxes(exponentformat='e')
fig.update_layout(
    title='CO2-Emissionen Deutschlands und globales Mittel',
    xaxis_title='Jahr',
    yaxis_title='CO2-Emissionen (Tonnen)',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    xaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5),
    yaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5, tickformat='.0e')
)
fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')
fig.update_yaxes(showline=True, linewidth=1, linecolor='grey')

fig.show()

ds_all.close()
