import pandas as pd
import plotly.express as px

# Load the population data
file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/population.csv"
population_data = pd.read_csv(file_path)

# Filter population data from 1949 onward for both China and India
filtered_population_data = population_data[(population_data['Year'] >= 1949) &
                                           (population_data['Entity'].isin(['China', 'India']))]

# Create the interactive line plot using Plotly
fig = px.line(filtered_population_data,
              x='Year',
              y='Population (historical)',
              color='Entity',  # Differentiate between China and India
              title='Population Growth of China and India (1949 - Present)',
              labels={'Population (historical)': 'Population', 'Year': 'Year', 'Entity': 'Country'},
              markers=True)

# Customize the layout
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Population',
    yaxis_tickformat=',',  # Format the y-axis to show commas
    template="plotly_white",  # A clean white background template
)

# Show the interactive plot
fig.show()
