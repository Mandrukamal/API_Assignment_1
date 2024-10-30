import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/StudentPerformanceFactors.csv")
logger.info(f"\n{df.head()}")
logger.info("Dataset loaded for binning.")

# Create output directory for figures
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

# Binning Hours_Studied into custom bins
min_value = df['Hours_Studied'].min()
max_value = df['Hours_Studied'].max()
logger.info(f"Min Hours_Studied: {min_value}, Max Hours_Studied: {max_value}")

# Bin size is custom, with 4 bins (e.g., Low, Medium, High, Very High)
bins = np.linspace(min_value, max_value, 5)
labels = ['Low', 'Medium', 'High', 'Very High']

# Distance binning
df['Hours_Studied_Binned'] = pd.cut(df['Hours_Studied'], bins=bins, labels=labels, include_lowest=True)
logger.info(f"Hours_Studied Distance Binning Results:\n{df['Hours_Studied_Binned']}")

# Frequency binning for Exam_Score into quartiles
df['Exam_Score_Binned'] = pd.qcut(df['Exam_Score'], q=4, precision=1, labels=['Low', 'Medium', 'High', 'Very High'])
logger.info(f"Exam_Score Frequency Binning Results:\n{df['Exam_Score_Binned']}")

# Plotting the binned results for Hours_Studied
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Hours_Studied_Binned')
plt.title("Hours_Studied binning plot")
plt.xlabel("Hours_Studied")
plt.ylabel("Count")
plt.savefig(f"/Users/mkmac/Documents/API_assignment_1/output/binning/Binned_Hours_Studied.png")
plt.close()
logger.info("Binned Hours_Studied plot saved.")

# Plotting the binned results for Exam_Score
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Exam_Score_Binned')
plt.title("Exam_Score binning plot")
plt.xlabel("Exam_Score")
plt.ylabel("Count")
plt.savefig(f"/Users/mkmac/Documents/API_assignment_1/output/binning/Binned_Exam_Score.png")
plt.close()
logger.info("Binned Exam_Score plot saved.")

logger.info("Binning process completed successfully.")