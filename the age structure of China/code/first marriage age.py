# Creating a DataFrame from the manually extracted data
import pandas as pd
import matplotlib.pyplot as plt
marriage_age_data = {
    'Year': list(range(1990, 2021)),
    'Average Age (Both)': [22.87, 22.98, 23.22, 23.42, 23.60, 23.79, 23.99, 24.19, 24.41, 24.60, 24.21, 24.24, 24.33, 24.43, 24.47, 24.52, 24.67, 24.71, 24.77, 24.89, 25.09, 25.09, 25.45, 25.72, 26.04, 26.43, 26.77, 27, 27.3, 27.68, 28.09],
    'Male': [23.59, 23.71, 23.94, 24.12, 24.28, 24.49, 24.69, 24.9, 25.16, 25.33, 25.11, 25.18, 25.23, 25.4, 25.44, 25.48, 25.64, 25.64, 25.7, 25.79, 25.75, 25.93, 26.14, 26.52, 26.86, 27.16, 27.5, 27.8, 28, 28.19, 28.38],
    'Female': [22.15, 22.25, 22.51, 22.71, 22.89, 23.08, 23.28, 23.48, 23.65, 23.88, 23.28, 23.29, 23.41, 23.45, 23.49, 23.52, 23.67, 23.67, 23.82, 23.97, 24, 24.24, 24.52, 24.91, 25.63, 25.63, 26.09, 26.19, 26.5, 26.95, 27.95]
}

df_marriage_age = pd.DataFrame(marriage_age_data)

# Plotting the trends of marriage age for males, females, and overall average
plt.figure(figsize=(10,6))
plt.plot(df_marriage_age['Year'], df_marriage_age['Average Age (Both)'], label='Average Age (Both)', marker='o')
plt.plot(df_marriage_age['Year'], df_marriage_age['Male'], label='Male', marker='o')
plt.plot(df_marriage_age['Year'], df_marriage_age['Female'], label='Female', marker='o')

# Adding labels and title
plt.title('Average First Marriage Age in China (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Age (Years)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
