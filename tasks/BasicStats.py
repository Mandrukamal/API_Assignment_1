import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/StudentPerformanceFactors.csv")
logger.info(f"\n{df.head()}")
logger.info("Dataset loaded successfully.")
logger.info(f"DataFrame head:\n{df.head()}")

# Summary statistics for numerical and categorical data
logger.info("Summary Statistics (Numerical):")
logger.info(f"\n{df.describe(include=[np.number])}")

logger.info("Summary Statistics (Categorical):")
logger.info(f"\n{df.describe(include=[object])}")

# Checking for missing values
logger.info("Missing Values:")
logger.info(f"\n{df.isnull().sum()}")

#drop missing values
logger.info("Drop missing values")
logger.info(f"\n{df.dropna(axis =1 , inplace=True)}")
logger.info(f"\n{df.isnull().sum()}")

#drop duplicates
logger.info("Drop Duplicate values")
logger.info(f"\n{df.drop_duplicates(inplace=True)}")
logger.info(f"\n{df.head()}")

# Data type information
logger.info("Data Types:")
logger.info(f"\n{df.dtypes}")
logger.info(f"\n{df.info()}")
logger.info(f"\n{df.describe()}")