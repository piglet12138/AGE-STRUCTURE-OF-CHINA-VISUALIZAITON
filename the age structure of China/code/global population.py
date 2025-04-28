import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
from matplotlib.colors import BoundaryNorm
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
import matplotlib as mpl

# Load the population data and shapefile
file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/population.csv"
population_data = pd.read_csv(file_path)

# Filter population data from 1949 onward
filtered_population_data = population_data[population_data['Year'] >= 1949]

# Load the world shapefile
world = gpd.read_file("C:/Users/87975/Desktop/Master Curricular/data virsualization/project/template/happiness/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

# Define population intervals (in millions)
population_bins = [0, 10e6, 30e6, 100e6, 300e6, 1e9]
population_labels = ['0', '10 million', '30 million', '100 million', '300 million', '1 billion']

# Create a colormap and norm based on the defined bins
cmap = plt.get_cmap('OrRd')
norm = BoundaryNorm(population_bins, cmap.N)

# Custom formatter to display population labels
def custom_format(x, pos):
    if x == 0:
        return '0'
    elif x == 10e6:
        return '10 million'
    elif x == 30e6:
        return '30 million'
    elif x == 100e6:
        return '100 million'
    elif x == 300e6:
        return '300 million'
    elif x == 1e9:
        return '1 billion'
    else:
        return f'{int(x):,}'

# Function to plot population distribution for a given year
def plot_population_for_year(year):
    ax.clear()  # Clear the axis to avoid multiple legends and overlapping data
    data_for_year = filtered_population_data[filtered_population_data['Year'] == year]
    merged_data = world.merge(data_for_year, left_on='ISO_A3', right_on='Code', how='left')

    # Plot the data with the custom norm and colormap
    merged_data.plot(column='Population (historical)', cmap=cmap, norm=norm, ax=ax)

    # Set title for each frame
    ax.set_title(f'Global Population Distribution in {year}', fontsize=15)

# List of years for the animation
years = sorted(filtered_population_data['Year'].unique())

# Set up the figure and axis for animation
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the first frame and add the legend only once
data_for_first_year = filtered_population_data[filtered_population_data['Year'] == years[0]]
merged_data = world.merge(data_for_first_year, left_on='ISO_A3', right_on='Code', how='left')

# Add the colorbar manually using `mpl.colorbar.ColorbarBase`
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm._A = []  # Dummy mappable object
cbar = fig.colorbar(sm, ax=ax, orientation="horizontal")
cbar.set_ticks(population_bins)  # Set the ticks
cbar.set_ticklabels(population_labels)  # Custom labels for the ticks

# Create the animation without adding the legend repeatedly
ani = FuncAnimation(fig, plot_population_for_year, frames=years, repeat=False)

# Save the animation as a gif
ani.save('global_population_1949_to_present.gif', writer='pillow', fps=5)

# Close figures to avoid memory overload
plt.close('all')
