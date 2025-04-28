import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame again
data_dict = {
    'Year': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Unmarried Ratio (%)': [20.69, 25.84, 25.17, 25.52, 31.43, 25.80, 27.45, 26.43, 26.46, 25.62, 25.12, 26.49, 29.06],
    'Married Ratio (%)': [77.93, 72.65, 73.49, 73.13, 67.06, 72.06, 70.92, 71.71, 71.61, 72.35, 72.72, 70.87, 68.78]
}

df = pd.DataFrame(data_dict)


# Visualize the data using matplotlib
plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Unmarried Ratio (%)'], label='Unmarried Ratio (%)', marker='o')
plt.plot(df['Year'], df['Married Ratio (%)'], label='Married Ratio (%)', marker='o')

plt.title('Unmarried and Married Ratios of 20-39 female Over the Years')
plt.xlabel('Year')
plt.ylabel('Ratio (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

