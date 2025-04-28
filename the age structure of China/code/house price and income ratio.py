import matplotlib.pyplot as plt

# Estimated data points from the image
years = list(range(1998, 2022))
price_to_income_ratio = [7.0, 6.8, 6.7, 6.6, 6.7, 6.8, 7.3, 7.5, 7.7, 8.2, 7.2, 7.5, 7.5, 7.3, 7.2, 7.0, 7.1, 7.0, 7.3, 7.7, 8.2, 8.7, 9.2, 9.1]

# Create the plot emphasizing post-2015 growth
plt.figure(figsize=(12, 6))
plt.plot(years, price_to_income_ratio, marker='o', color='red', linestyle='-', linewidth=2, label='Price-to-Income Ratio')

# Emphasize the years after 2015
plt.plot(years[17:], price_to_income_ratio[17:], marker='o', color='orange', linewidth=3, linestyle='-', label='Growth After 2015')

# Adding labels and title in English
plt.title('Price-to-Income Ratio of New Residential Buildings in China (1998-2021)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Price-to-Income Ratio', fontsize=12, fontweight='bold')

# Highlight the y-axis range with specific limits
plt.ylim(6.5, 9.5)

# Shade the region after 2015 to visually emphasize the growth
plt.fill_between(years[17:], price_to_income_ratio[17:], color='orange', alpha=0.1)

# Add grid, custom ticks, and a legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

# Add an annotation to highlight 2015 transition
plt.axvline(x=2015, color='blue', linestyle='--', linewidth=1.5)
plt.text(2015.5, 7.8, '2015 Growth', color='blue', fontsize=12)

# Tight layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()
