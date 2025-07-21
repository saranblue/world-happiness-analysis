import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('data/world_happiness.csv')

# Create visuals directory
os.makedirs("visuals", exist_ok=True)

# Select numeric columns only
numeric_df = df[['Happiness Score', 'GDP per Capita', 'Social Support',
                 'Life Expectancy', 'Freedom', 'Corruption']]

# Create correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu", linewidths=0.5)

plt.title("Correlation Heatmap of World Happiness Factors")
plt.tight_layout()

# Save the heatmap
plt.savefig("visuals/seaborn_heatmap.png")
print(" Seaborn heatmap saved to visuals/seaborn_heatmap.png")
