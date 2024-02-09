import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import cartopy.crs as ccrs
import numpy as np  # Ensure NumPy is imported for meshgrid
import plotly.express as px
import os

def plot_map(ds, year, projection=ccrs.Robinson(), colormap='afmhot', clabel='[Tonnes/Year]', save_plot = 'no'):
    """
    Plot global CO2 emissions for a specified year using cartopy for map projections.
    
    Parameters:
    - ds: xarray.Dataset containing emissions data with dimensions ('time', 'lat', 'lon').
    - year: Integer specifying the year to plot.
    - projection: cartopy.crs projection instance.
    - colormap: String specifying the matplotlib colormap.
    - clabel: String for the colorbar label.
    - save_plot: Save Figure if set to Yes
    """
    # Select emissions for the specified year
    emissions_year = ds.sel(time=str(year)).emissions.compute().squeeze()

    # Determine coordinates
    lon, lat = np.meshgrid(ds.lon, ds.lat)

    # Create plot figure
   
    fig, ax = plt.subplots(figsize=(8, 5.6), subplot_kw={'projection': projection}, dpi=300)
    ax.patch.set_facecolor('black')
    fig.patch.set_alpha(0)

    # Logarithmic normalization
    norm = LogNorm(vmin=max(emissions_year.min(), 1e-1), vmax=emissions_year.max())

    # Create mesh plot
    mesh = ax.pcolormesh(lon, lat, emissions_year, cmap=colormap, norm=norm, transform=ccrs.PlateCarree())

    # Add color bar
    cbar = fig.colorbar(mesh, ax=ax, orientation='vertical', extend='both', shrink=0.5, aspect=20, extendfrac='auto')
    cbar.set_label(clabel, fontsize=10, color='black')

    # Add coastlines
    ax.coastlines(color='dimgray', linewidth=0.5)

    # Save the graphic
    if save_plot == 'yes':
        plt.savefig(f'CO2_{year}.png', dpi=300, bbox_inches='tight', pad_inches=0)
        print(f'Plot saved as CO2_{year}.png')
    
    plt.show()


def plot_emissions(df, chart_type='top', start_year=1970, end_year=2022, country=None):
    """
    Plot a time series or aggregated bar chart of CO2 emissions based on the input parameters.
    If a country is specified, it plots a time series for that country. Otherwise, it plots 
    the top or bottom 10 emitting countries based on the total emissions over the specified period.
    
    Parameters:
    - df: pandas.DataFrame containing emissions data with columns ['year', 'country', 'emission'].
    - chart_type: String specifying chart type ('top', 'bottom') for aggregate view.
    - start_year: Integer specifying the start year of the period.
    - end_year: Integer specifying the end year of the period.
    - country: String specifying a single country to filter the data. If None, plot top or bottom countries.
    """
    if country:
        # Filter data for the specified country and year range
        filtered_df = df[(df['country'] == country) & 
                         (df['year'] >= start_year) & 
                         (df['year'] <= end_year)]
        fig = px.bar(filtered_df, x='year', y='emission', 
                     title=f'CO2 Emissions for {country} ({start_year}-{end_year})',
                     labels={'emission': 'CO2 Emissions (Tonnes)', 'year': 'Year'})
    else:
        # Aggregate emissions data for all countries
        aggregated_emissions = df[(df['year'] >= start_year) & 
                                  (df['year'] <= end_year)].groupby('country')['emission'].sum()

        if chart_type == 'top':
            selected_emitters = aggregated_emissions.nlargest(10)
            title = f'Top 10 CO2 Emitters ({start_year}-{end_year})'
        else:
            selected_emitters = aggregated_emissions.nsmallest(10)
            title = f'Bottom 10 CO2 Emitters ({start_year}-{end_year})'
        
        fig = px.bar(selected_emitters.reset_index(), x='country', y='emission', 
                     title=title,
                     labels={'emission': 'CO2 Emissions (Tonnes)', 'country': 'Country'})

    # Common styling for both plots
    fig.update_layout(
        plot_bgcolor='black',  # Black background for the chart area
        paper_bgcolor='black',  # Black background for the entire figure
        font_color='white',  # White font color
        xaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5),  # Settings for the X-axis
        yaxis=dict(showgrid=True, gridcolor='grey', gridwidth=0.5, tickformat='.0e')  # Settings for the Y-axis
    )

    fig.update_traces(marker_color='blue')  # Update traces for specific styling

    fig.show()

