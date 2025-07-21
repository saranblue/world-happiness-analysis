import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
df = pd.read_csv('data/world_happiness.csv')

# Create output folder if it doesn't exist
os.makedirs("visuals", exist_ok=True)

# Sort top 10 happiest countries
top10 = df.sort_values(by='Happiness Score', ascending=False).head(10)

# Create a bar chart
plt.figure(figsize=(10,6))
plt.bar(top10['Country'], top10['Happiness Score'], color='skyblue')
plt.xticks(rotation=45)
plt.title("Top 10 Happiest Countries")
plt.ylabel("Happiness Score")
plt.tight_layout()

# Save plot
plt.savefig("visuals/top10_happy.png")
print(" Plot saved to visuals/top10_happy.png")


