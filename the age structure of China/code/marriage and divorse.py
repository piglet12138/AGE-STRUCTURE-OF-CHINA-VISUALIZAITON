import pandas as pd
import plotly.graph_objects as go

new_file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/marriage and divorse.csv"
new_data = pd.read_csv(new_file_path, encoding='latin1')
new_data_t = new_data.set_index('indicator').T

# 将年份转换为数值并按年份排序
new_data_t.index = pd.to_numeric(new_data_t.index, errors='coerce')
new_data_t = new_data_t.sort_index()

selected_indicators_interactive = [
    'Marriage registration (10,000 couples)',
    'First marriage registration of mainland residents (10,000 people)',
    'Divorce registration (10,000 couples)'
]

# 定义手动设置的颜色列表
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 每个指标对应的颜色

# Create a figure using plotly
fig = go.Figure()

# Add lines for each selected indicator
for idx, indicator in enumerate(selected_indicators_interactive):
    trace = go.Scatter(x=new_data_t.index,
                       y=new_data_t[indicator],
                       mode='lines+markers',
                       name=indicator,
                       line=dict(color=colors[idx]),  # 使用手动设置的颜色
                       showlegend=False)

    # Add the trace to the figure
    fig.add_trace(trace)

    # Add annotation at the end of each line with customized font and color
    fig.add_annotation(
        x=new_data_t.index[-1],  # Last year
        y=new_data_t[indicator].iloc[-1],  # Last value for the indicator
        text=indicator,  # Indicator name
        font=dict(size=12, color=colors[idx]),  # Larger font size and matching line color
        showarrow=False,
        xanchor='left',
        yanchor='middle',
        xshift=10  # Adjust the position slightly to the left
    )

# Update layout for better readability
fig.update_layout(
    title='Marriage and Divorce Registration Trends Over the Years',
    xaxis_title='Year',
    yaxis_title='Number of Registrations',
    xaxis=dict(tickangle=-45),
    hovermode='x unified',
    template="plotly_white"  # Clean white background template
)

# Show the interactive plot
fig.show()
