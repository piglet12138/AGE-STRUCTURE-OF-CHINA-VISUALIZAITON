import pandas as pd
import plotly.express as px
# Load the uploaded birth rate data
birth_rate_file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/crude-birth-rate.csv"
birth_rate_data = pd.read_csv(birth_rate_file_path)
# Clean and rename the birth rate column for better usability
birth_rate_data.rename(columns={'Birth rate - Sex: all - Age: all - Variant: estimates': 'Birth Rate'}, inplace=True)

# Convert the 'Birth Rate' column to numeric
birth_rate_data['Birth Rate'] = pd.to_numeric(birth_rate_data['Birth Rate'], errors='coerce')

# Filter the data for China only
china_birth_rate = birth_rate_data[birth_rate_data['Entity'] == 'China']

# Create the interactive line plot for birth rate in China
fig = px.line(china_birth_rate,
              x='Year',
              y='Birth Rate',
              title='Crude Birth Rate in China (1950 - Present)',
              labels={'Birth Rate': 'Birth Rate (per 1000 people)', 'Year': 'Year'},
              markers=True)

# Customize the layout
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Birth Rate (per 1000 people)',
    template="plotly_white",  # Clean white background template
)

# Show the interactive plot
fig.show()


