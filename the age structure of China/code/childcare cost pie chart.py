import matplotlib.pyplot as plt

# Total cost
total_cost = 538312  # Total cost from the provided data

# Data and labels
labels = ['Other', '0-2 years old', '3-5 years old', '6-14 years old', '15-17 years old']
cost_proportions = [1.86 + 2.79, 13.67, 20.36, 45.15, 16.17]

# Sorting the values in descending order for the pie chart
sorted_data = sorted(zip(cost_proportions, labels), reverse=True)
cost_proportions_sorted, labels_sorted = zip(*sorted_data)

# Create a more visually appealing donut chart
plt.figure(figsize=(8, 6))
colors = ['#FF6F61', '#F7CAC9', '#92A8D1', '#034F84', '#B565A7']
wedges, texts, autotexts = plt.pie(
    cost_proportions_sorted,
    labels=labels_sorted,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'width': 0.4},
    pctdistance=0.85  # Bring the percentage labels closer to the center
)

# Customize the font size and color of the labels
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')

# Customize the font size of the percentages
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('white')

# Add a circle at the center to turn the pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Add text in the center showing the total cost
plt.text(0, 0, f'Total\n{total_cost:,} Yuan', horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold')

# Adding title
plt.title('Proportion of Total Child-Raising Costs (0-17 years old)', fontsize=16, fontweight='bold')

# Display the chart
plt.tight_layout()
plt.show()
