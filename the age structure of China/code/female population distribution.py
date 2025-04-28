import pandas as pd
import matplotlib.pyplot as plt

# Define color based on age groups in ranges of 20 years
age_colors = []
for age_group in df_population['Age Group']:
    age = int(age_group.split('-')[0].replace('+', ''))  # Get the lower age limit of the age group
    if age < 20:
        age_colors.append('lightblue')  # 0-19
    elif age < 40:
        age_colors.append('lightgreen')  # 20-39
    elif age < 60:
        age_colors.append('orange')  # 40-59
    else:
        age_colors.append('lightcoral')  # 60+

# Create a bar plot for female population distribution with color representing different age groups
plt.figure(figsize=(10, 6))

# Plot the female population data with the assigned colors
plt.bar(df_population['Age Group'], df_population['Female Population (One Hundred Thousands)'], color=age_colors)

# Add title and labels
plt.title('Age Distribution of Female Population in China (2022)', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Female Population (Hundred Thousands)', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Create a custom legend for the age groups
handles = [plt.Rectangle((0,0),1,1, color='lightblue', label='0-19'),
           plt.Rectangle((0,0),1,1, color='lightgreen', label='20-39'),
           plt.Rectangle((0,0),1,1, color='orange', label='40-59'),
           plt.Rectangle((0,0),1,1, color='lightcoral', label='60+')]

plt.legend(handles=handles, title="Age Range")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
