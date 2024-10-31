# 1. Importing the Libraries
import pandas as pd
import numpy as np
import logging

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 2. Reading the file
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/ImputedStudentPerformanceFactors.csv")
logger.info(f"Dataset loaded:\n{df.head()}")

# 3. Apply Label encoding to the field 'Attendance'
# Import LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Attendance'] = le.fit_transform(df['Attendance'])
logger.info(f"Label encoded 'Attendance' column:\n{df['Attendance']}")

# For Teacher_Quality field
df['Teacher_Quality'] = le.fit_transform(df['Teacher_Quality'])
logger.info(f"Label encoded 'Teacher_Quality' column:\n{df['Teacher_Quality']}")

# Represent Attendance using One-Hot Encoding
logger.info(f"Attendance value counts:\n{df['Attendance'].value_counts()}")
df = pd.get_dummies(df, columns=['Attendance'])
logger.info(f"One-hot encoded 'Attendance' column:\n{df.head()}")

# One hot encoding for Teacher_Quality field
logger.info(f"Teacher_Quality value counts:\n{df['Teacher_Quality'].value_counts()}")
df = pd.get_dummies(df, columns=['Teacher_Quality'])
logger.info(f"One-hot encoded 'Teacher_Quality' column:\n{df.head()}")

# For multiple columns (if needed in the future, uncomment below)
# df = pd.get_dummies(df, columns=['Teacher_Quality', 'Attendance'])
# logger.info(f"One-hot encoded columns 'Teacher_Quality' and 'Attendance':\n{df.head()}")