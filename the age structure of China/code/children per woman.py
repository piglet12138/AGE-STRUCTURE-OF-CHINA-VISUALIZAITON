import pandas as pd
import matplotlib.pyplot as plt

# Load the fertility rate data
file_path_fertility = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/children-per-woman-un.csv"
df_fertility = pd.read_csv(file_path_fertility)

# Renaming the fertility rate column for better readability
df_fertility.rename(columns={'Fertility rate - Sex: all - Age: all - Variant: estimates': 'Fertility Rate'}, inplace=True)

# Filtering data for China, Singapore, and World since 2000
filtered_df = df_fertility[(df_fertility['Entity'].isin(['China', 'Singapore', 'World'])) & (df_fertility['Year'] >= 2000)]
# Pivoting the data for easier plotting
pivot_df = filtered_df.pivot(index='Year', columns='Entity', values='Fertility Rate')

# Create the plot
plt.figure(figsize=(12, 6))

# Plotting the fertility rates
plt.plot(pivot_df.index, pivot_df['China'], label='China', marker='o', color='royalblue', linewidth=2)
plt.plot(pivot_df.index, pivot_df['Singapore'], label='Singapore', marker='o', color='orange', linewidth=2)
plt.plot(pivot_df.index, pivot_df['World'], label='World', marker='o', color='green', linewidth=2)

# Highlighting the trend after 2017 for China
plt.plot(pivot_df.index[pivot_df.index >= 2017], pivot_df['China'][pivot_df.index >= 2017],
         color='red', linewidth=3, label='China (After 2017)')


# Adding labels and titles
plt.title('Fertility Rate Comparison: China, Singapore, and World (2000-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Fertility Rate (Children per Woman)', fontsize=12, fontweight='bold')


# Adding grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
