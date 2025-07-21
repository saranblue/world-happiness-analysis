import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/world_happiness.csv')

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='GDP per Capita',
    y='Happiness Score',
    color='Region',
    hover_name='Country',
    size='Life Expectancy',
    title='GDP vs Happiness Score (Interactive)'
)

# Show plot in browser
fig.show()
print(" Interactive Plotly graph displayed in browser.")
