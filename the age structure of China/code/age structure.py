import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating a DataFrame for the extracted data
population_data = {
    'Age Group': ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                  '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95+'],
    'Male Population (One Hundred Thousands)': [30910, 48010, 48790, 42687, 39146, 36682, 35013, 36972, 50422, 52930,
                                                47916, 46749, 35813, 39343, 28355, 16985, 8751, 3811, 1654, 311],
    'Female Population (One Hundred Thousands)': [31049, 42783, 42873, 36873, 34363, 32915, 31868, 31792, 47957, 51025,
                                                  44029, 41618, 36151, 40621, 30427, 19073, 12351, 7031, 2644, 618]
}

df_population = pd.DataFrame(population_data)

# Define generation groups in English
generation_colors = {
    'Post-10s': '#1f77b4',  # 10后
    'Post-00s': '#ff7f0e',  # 00后
    'Post-90s': '#2ca02c',  # 90后
    'Post-80s': '#d62728',  # 80后
    'Post-70s': '#9467bd',  # 70后
    'Post-60s': '#8c564b',  # 60后
    'Post-50s': '#e377c2',  # 50后及更早
}

# Map each age group to a generation based on 2022
generation_labels = ['Post-10s', 'Post-10s', 'Post-00s', 'Post-00s', 'Post-90s', 'Post-90s',
                     'Post-80s', 'Post-80s', 'Post-70s', 'Post-70s', 'Post-60s', 'Post-60s',
                     'Post-50s', 'Post-50s', 'Post-50s', 'Post-50s', 'Post-50s', 'Post-50s', 'Post-50s', 'Post-50s']

# Adjust the data values by dividing by 100000 and multiplying by 100 to convert to percentages
df_population['Male Population (Percentage)'] = df_population['Male Population (One Hundred Thousands)'] / 1000000 * 100
df_population['Female Population (Percentage)'] = df_population[
                                                      'Female Population (One Hundred Thousands)'] / 1000000 * 100

# Create the plot
plt.figure(figsize=(10, 8))

# Plot each age group with the corresponding generation color
for i, age_group in enumerate(df_population['Age Group']):
    generation = generation_labels[i]
    color = generation_colors[generation]

    # Plot male and female bars with the same color for each generation
    plt.barh(age_group, df_population['Male Population (Percentage)'][i],
             color=color, label=generation if i == 0 else "", align='center')
    plt.barh(age_group, -df_population['Female Population (Percentage)'][i],
             color=color, align='center')

# Add title and remove x-axis
plt.title('Population Pyramid of China (2022)', fontsize=16)
plt.gca().axes.get_xaxis().set_visible(False)

# Add vertical line at x = 0
plt.axvline(x=0, color='black', linewidth=0.8)

# Add generation legend
handles = [plt.Rectangle((0, 0), 1, 1, color=generation_colors[label]) for label in generation_colors]
plt.legend(handles, generation_colors.keys(), loc='upper right')

# Add text labels inside the bars
for i, (male_pop, female_pop) in enumerate(zip(df_population['Male Population (Percentage)'],
                                               df_population['Female Population (Percentage)'])):
    plt.text(male_pop + 0.5, i, f"{male_pop:.2f}%", va='center', ha='left', fontsize=10)
    plt.text(-female_pop - 0.5, i, f"{female_pop:.2f}%", va='center', ha='right', fontsize=10)

# Adjust layout
plt.tight_layout()
plt.show()

