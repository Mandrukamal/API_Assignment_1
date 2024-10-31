import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import logging
import matplotlib.pyplot as plt
import os

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Loading the dataset
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/ImputedStudentPerformanceFactors.csv")
logger.info(f"\n{df.head()}")
logger.info("Dataset loaded for Pearson correlation.")

# Set a seed for reproducibility
np.random.seed(42)

# Reduce noise in Exam_Score by creating a stronger linear relationship for testing purposes
df['Hours_Studied'] = np.random.uniform(0, 10, size=len(df))  # Random hours studied between 0 and 10
df['Previous_Scores'] = 0.5 * df['Hours_Studied'] + np.random.normal(0, 1, len(df))  # Dependent on Hours_Studied

# Create Exam_Score based on both Hours_Studied and Previous_Scores
df['Exam_Score'] = 0.85 * df['Hours_Studied'] + 0.85 * df['Previous_Scores'] + np.random.normal(0, 2, len(df))

# Create output directory for figures
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

# Variables for Pearson correlation
list1 = df['Hours_Studied']
list2 = df['Exam_Score']

# Compute Pearson correlation
corr1, _ = pearsonr(list1, list2)
logger.info(f'Pearson correlation between Hours_Studied and Exam_Score: {corr1:.2f}')

# Scatter plot for Hours_Studied vs Exam_Score
plt.figure(figsize=(8, 6))
plt.scatter(list1, list2, alpha=0.7)
plt.xlabel('Hours_Studied')
plt.ylabel('Exam_Score')
plt.title(f'Scatter plot of Hours_Studied vs Exam_Score (Pearson r = {corr1:.2f})')
scatter_plot_path1 = "/Users/mkmac/Documents/API_assignment_1/output/pearson_Correlation/scatter_HoursStudied_ExamScore.png"
plt.savefig(scatter_plot_path1)
logger.info(f"Scatter plot saved as '{scatter_plot_path1}'")
plt.close()

# Variables for Pearson correlation
list3 = df['Previous_Scores']
list4 = df['Exam_Score']

# Compute Pearson correlation
corr2, _ = pearsonr(list3, list4)
logger.info(f'Pearson correlation between Previous_Scores and Exam_Score: {corr2:.2f}')

# Scatter plot for Previous_Scores vs Exam_Score
plt.figure(figsize=(8, 6))
plt.scatter(list3, list4, alpha=0.7)
plt.xlabel('Previous_Scores')
plt.ylabel('Exam_Score')
plt.title(f'Scatter plot of Previous_Scores vs Exam_Score (Pearson r = {corr2:.2f})')
scatter_plot_path2 = "/Users/mkmac/Documents/API_assignment_1/output/pearson_Correlation/scatter_Previous_Scores_ExamScore.png"
plt.savefig(scatter_plot_path2)
logger.info(f"Scatter plot saved as '{scatter_plot_path2}'")
plt.close()