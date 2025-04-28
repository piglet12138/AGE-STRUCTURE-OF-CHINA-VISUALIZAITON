import matplotlib.pyplot as plt

# Estimated data points from the image
years = list(range(1998, 2022))
price_to_income_ratio = [7.0, 6.8, 6.7, 6.6, 6.7, 6.8, 7.3, 7.5, 7.7, 8.2, 7.2, 7.5, 7.5, 7.3, 7.2, 7.0, 7.1, 7.0, 7.3, 7.7, 8.2, 8.7, 9.2, 9.1]

# Create the plot with enhanced focus on the specified ranges
plt.figure(figsize=(12, 6))

# Define colors based on the ranges (below 7.0 = blue, 7.0-7.5 = green, above 7.5 = red)
colors = ['lightblue' if y < 7.0 else 'lightgreen' if 7.0 <= y <= 7.5 else 'lightcoral' for y in price_to_income_ratio]

# Plot the data points with different colors based on the ratio range
for i in range(len(years)-1):
    plt.plot(years[i:i+2], price_to_income_ratio[i:i+2], color=colors[i], marker='o', linewidth=2)

# Add labels and title in English
plt.title('Price-to-Income Ratio of New Residential Buildings in China (1998-2021)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Price-to-Income Ratio', fontsize=12, fontweight='bold')

# Highlight the range for 7.0-7.5 as reasonable
plt.axhspan(7.0, 7.5, facecolor='lightgreen', alpha=0.3, label='Reasonable Range (7.0-7.5)')

# Mark areas below 7.0 as low and above 7.5 as high
plt.axhspan(6.5, 7.0, facecolor='lightblue', alpha=0.3, label='Low Range (Below 7.0)')
plt.axhspan(7.5, 9.5, facecolor='lightcoral', alpha=0.3, label='High Range (Above 7.5)')

# Add grid and custom ticks
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(fontsize=12)

# Add legend
plt.legend(fontsize=12)

# Tight layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()
