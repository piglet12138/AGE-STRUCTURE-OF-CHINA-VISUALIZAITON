import matplotlib.pyplot as plt

# Define the data for residential housing prices based on the visible image data
years = [
    1998, 2000, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
]

# Residential prices in corresponding years (data extracted from image)
residential_prices = [
    1854, 1948, 2937, 3119, 3645, 3576, 4459, 4733, 5010, 5463,
    5894, 5988, 6543, 7298, 7737, 8694, 9454, 10159, 10590, 10375
]

# Create the line plot for residential housing prices over the years
plt.figure(figsize=(12, 6))

# Adding customizations to enhance the plot appearance
plt.plot(years, residential_prices, marker='o', color='royalblue', linewidth=2, markersize=8)

# Add labels and title with styling
plt.title('Residential Housing Price Trends (1998-2022)', fontsize=20, fontweight='bold')
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Price (RMB per square meter)', fontsize=14, fontweight='bold')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add custom ticks and gridlines
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)

# Add a shaded region to indicate recent years
plt.fill_between(years[-5:], residential_prices[-5:], color='lightblue', alpha=0.3)

# Annotate the latest price point
plt.annotate(f'{residential_prices[-1]} RMB/sq.m', xy=(years[-1], residential_prices[-1]),
             xytext=(years[-1] - 2, residential_prices[-1] + 1000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
