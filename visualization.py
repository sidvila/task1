# Week 4 – Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Age": [20,21,22,23,24,25,26],
    "Study_Hours": [2,3,4,5,3,4,6],
    "Score": [60,65,70,75,72,78,85]
}

df = pd.DataFrame(data)

# Histogram
plt.figure()
plt.hist(df["Score"], bins=5, color="skyblue")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()

# Scatter Plot
plt.figure()
plt.scatter(df["Study_Hours"], df["Score"], color="green")
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.savefig("scatter_plot.png")
plt.close()

# Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Pairplot
sns.pairplot(df)
plt.savefig("pairplot.png")
plt.close()