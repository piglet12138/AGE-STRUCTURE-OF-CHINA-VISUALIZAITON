import matplotlib.pyplot as plt
import seaborn as sns

# Data for national average and provinces/cities above the national average
regions_en = [
    'National Average', 'Shanghai', 'Beijing', 'Zhejiang', 'Jiangsu', 'Guangdong', 'Tianjin', 'Fujian',
    'Chongqing', 'Hubei'
]

costs_en = [
    538312, 1010130, 936375, 854912, 839367, 705702, 687183, 631503, 611645, 607206
]

# Sorting the data in descending order
sorted_data = sorted(zip(costs_en, regions_en), reverse=False)
costs_sorted, regions_sorted = zip(*sorted_data)

# Create a color palette based on the cost values
palette = sns.color_palette("coolwarm", len(costs_sorted))

# Creating the vertical bar chart with a color palette
plt.figure(figsize=(10, 6))
bars = plt.barh(regions_sorted, costs_sorted, color=palette)

# Title without the xlabel
plt.title('Average Child-Raising Cost (Above National Average)')

# Highlight the regions above the national average with their specific data
for i in range(len(costs_sorted)):
    plt.text(costs_sorted[i] + 5000, i, f'{costs_sorted[i]:,} Yuan', va='center', fontsize=10, color='black')
plt.xticks ([])
# Display the chart without the xlabel
plt.tight_layout()
plt.show()
