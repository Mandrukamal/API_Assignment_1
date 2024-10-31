from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/ImputedStudentPerformanceFactors.csv")
print(df.head())  # Print the first few rows of the dataset for a quick preview

# Correlation Matrix using Pearson Correlation
corr_matrix = df.corr()  # Compute the correlation matrix

# Plotting Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Student Performance Factors")
plt.show()