import pandas as pd
import matplotlib.pyplot as plt

# Creating the table with GDP per capita data and ratios from the image
data = {
    'Country': ['Australia', 'Singapore', 'Sweden', 'Switzerland', 'Ireland', 'Germany', 'USA', 'Japan',
                'Canada', 'New Zealand', 'UK', 'Italy', 'China', 'South Korea'],
    'Year': [2018, 2021, 2020, 2020, 2016, 2018, 2015, 2010, 2017, 2018, 2018, 2021, 2022, 2013],
    'GDP per Capita (USD)': [55050, 77710, 52838, 88310, 69334, 48499, 56802, 43069, 44341, 43415, 45751, 35551, 12720, 25920],
    'Cost/GDP Ratio': [2.08, 2.1, 2.91, 3.51, 3.57, 3.64, 4.11, 4.26, 4.34, 4.55, 5.25, 6.28, 6.73, 7.79]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Calculate the child-raising cost
df['Child-Raising Cost (USD)'] = df['GDP per Capita (USD)'] * df['Cost/GDP Ratio']

import matplotlib.pyplot as plt

# Plotting the scatter plot
plt.figure(figsize=(10, 6))

# Use scatter plot with varying size and color for the Cost/GDP Ratio
sc = plt.scatter(df['GDP per Capita (USD)'], df['Child-Raising Cost (USD)'],
                 s=df['Cost/GDP Ratio']*100,  # Size proportional to the Cost/GDP Ratio
                 c=df['Cost/GDP Ratio'],      # Color based on the ratio
                 cmap='coolwarm', alpha=0.7, edgecolor='k')

# Adding labels and title
plt.title('Child-Raising Cost vs GDP per Capita by Country')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Child-Raising Cost (USD)')

# Annotating the countries on the scatter plot
for i in range(len(df)):
    plt.text(df['GDP per Capita (USD)'][i] + 500, df['Child-Raising Cost (USD)'][i], df['Country'][i], fontsize=9)

# Draw a light dashed line from origin (extended to further distance)
china_gdp = df[df['Country'] == 'China']['GDP per Capita (USD)'].values[0]
china_cost = df[df['Country'] == 'China']['Child-Raising Cost (USD)'].values[0]
plt.plot([0, china_gdp * 5], [0, china_cost * 5], color='gray', linestyle='--', linewidth=0.8)

# Adding a color bar for the Cost/GDP Ratio
cbar = plt.colorbar(sc)
cbar.set_label('Cost/GDP Ratio')

# Display the plot
plt.tight_layout()
plt.show()
