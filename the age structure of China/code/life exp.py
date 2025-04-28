import pandas as pd

# Load the uploaded life expectancy data
file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/life-expectancy.csv"
life_expectancy_data = pd.read_csv(file_path)
# Reimport plotly express to resolve the name error
import plotly.express as px
# Correcting the column renaming with the full name
life_expectancy_data.rename(columns={'Period life expectancy at birth - Sex: all - Age: 0': 'Life Expectancy'}, inplace=True)

# Convert the 'Life Expectancy' column to numeric
life_expectancy_data['Life Expectancy'] = pd.to_numeric(life_expectancy_data['Life Expectancy'], errors='coerce')

# Filter the data for China only
china_life_expectancy = life_expectancy_data[life_expectancy_data['Entity'] == 'China']

# Create the interactive line plot for life expectancy in China
fig = px.line(china_life_expectancy,
              x='Year',
              y='Life Expectancy',
              title='Life Expectancy in China (1950 - Present)',
              labels={'Life Expectancy': 'Life Expectancy (Years)', 'Year': 'Year'},
              markers=True)

# Customize the layout
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Life Expectancy (Years)',
    template="plotly_white",  # Clean white background template
)

# Show the interactive plot
fig.show()
