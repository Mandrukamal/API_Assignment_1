import pandas as pd
from prefect import flow, task
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt  # Corrected import for matplotlib
import seaborn as sns
import numpy as np

@task
def load_dataset():
    # Load the dataset from a local file path
    file_path = "data/StudentPerformanceFactors.csv"
    return pd.read_csv(file_path)

@task(log_prints=True)
def preprocess_data(df):
    # Handle missing values
    missing_values = df.isna().sum().sum()
    print('Missing values:', missing_values)

    # Encode categorical variables
    label_columns = [
        'Teacher_Quality', 'Parental_Education_Level', 'Distance_from_Home',
        'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities',
        'Motivation_Level', 'Internet_Access', 'Family_Income', 'School_Type',
        'Peer_Influence', 'Learning_Disabilities', 'Gender'
    ]

    for col in label_columns:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    df_imputed.to_csv('data/ImputedStudentPerformanceFactors.csv', index=False)
    return df_imputed

@task
def perform_eda(df):
    # Example EDA function
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Exam_Score')
    plt.title('Distribution of Exam Scores')
    plt.savefig('output/exam_score_distribution.png')
    plt.close()
    print("EDA completed and saved.")

# Step 5: Define Prefect Flow
@flow(log_prints=True)
def student_performance_s():
    # Step 1: Load Data
    data = load_dataset()
    
    # Step 2: Preprocessing
    preprocessed_data = preprocess_data(data)

    # Step 3: Perform EDA
    perform_eda(preprocessed_data)

# Step 6: Run the Prefect Flow
if __name__ == "__main__":
    student_performance_s.serve(name="student-performance-data-2",
                      tags=["first workflow"],
                      parameters={},
                      interval=120)
