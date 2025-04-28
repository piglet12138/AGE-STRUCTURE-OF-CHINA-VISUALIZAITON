import pandas as pd
import plotly.graph_objects as go

# Load the data
file_path ="C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/annual-population-growth.csv"
population_growth_data = pd.read_csv(file_path)

# Filter the data for China
china_population_growth = population_growth_data[
    (population_growth_data['Entity'] == 'China') &
    (population_growth_data['Year'] >= 1949)
]

# Separate actual (estimates) and projected (medium variant) data
china_actual_growth = china_population_growth[
    (china_population_growth['Year'] <= 2023) &
    ~china_population_growth['Population change - Sex: all - Age: all - Variant: estimates'].isna()
][['Year', 'Population change - Sex: all - Age: all - Variant: estimates']]

china_projected_growth = china_population_growth[
    (china_population_growth['Year'] > 2023) &
    ~china_population_growth['Population change - Sex: all - Age: all - Variant: medium'].isna()
][['Year', 'Population change - Sex: all - Age: all - Variant: medium']]

# Rename columns for easier handling
china_actual_growth.columns = ['Year', 'Population Change Estimate']
china_projected_growth.columns = ['Year', 'Population Change Projection']

# Create the plot using Plotly's graph_objects for more control over styling
fig = go.Figure()

# Add the actual population growth (solid line)
fig.add_trace(go.Scatter(
    x=china_actual_growth['Year'],
    y=china_actual_growth['Population Change Estimate'],
    mode='lines+markers',
    name='Actual Population Change',
    line=dict(color='blue', width=2),
    marker=dict(size=6)
))

# Add the projected population growth (dashed line)
fig.add_trace(go.Scatter(
    x=china_projected_growth['Year'],
    y=china_projected_growth['Population Change Projection'],
    mode='lines+markers',
    name='Projected Population Change',
    line=dict(color='red', width=2, dash='dash'),  # Dashed line for projection
    marker=dict(size=6)
))

# Customize the layout
fig.update_layout(
    title='Annual Population Growth of China (1949 - Present with Projections)',
    xaxis_title='Year',
    yaxis_title='Population Change (People)',
    yaxis_tickformat=',',  # Format the y-axis to show commas
    template="plotly_white",
    showlegend=True
)

# Show the interactive plot
fig.show()