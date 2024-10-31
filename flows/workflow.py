from prefect import flow, task, get_run_logger
import subprocess
import os

@task(log_prints=True)  # Ensures all prints are captured in logs
def run_task(script_name):
    logger = get_run_logger()
# =======
# @task
# def load_dataset():
#     # Load the dataset from a local file path
#     file_path = "data/StudentPerformanceFactors.csv"
#     return pd.read_csv(file_path)

# @task(log_prints=True)
# def preprocess_data(df):
#     # Handle missing values
#     missing_values = df.isna().sum().sum()
#     print('Missing values:', missing_values)

#     # Encode categorical variables
#     label_columns = [
#         'Teacher_Quality', 'Parental_Education_Level', 'Distance_from_Home',
#         'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities',
#         'Motivation_Level', 'Internet_Access', 'Family_Income', 'School_Type',
#         'Peer_Influence', 'Learning_Disabilities', 'Gender'
#     ]

#     for col in label_columns:
#         encoder = LabelEncoder()
#         df[col] = encoder.fit_transform(df[col])

#     # Impute missing values
#     imputer = SimpleImputer(strategy='mean')
#     df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
#     df_imputed.to_csv('data/ImputedStudentPerformanceFactors.csv', index=False)
#     return df_imputed

# @task
# def perform_eda(df):
#     # Example EDA function
#     plt.figure(figsize=(10, 6))
#     sns.countplot(data=df, x='Exam_Score')
#     plt.title('Distribution of Exam Scores')
#     plt.savefig('output/exam_score_distribution.png')

#     plt.figure(figsize=(6,4))
#     sns.histplot(x='Hours_Studied', data=df)
#     plt.xlabel('Hours Studied')
#     plt.ylabel('Number of Students')
#     plt.title('How much time student spend on studies?')
#     plt.savefig('output/hours_studied.png')


#     plt.figure(figsize=(6,4))
#     sns.histplot(x='Attendance', data=df)
#     plt.xlabel('Attendance')
#     plt.ylabel('Number of Students')
#     plt.title('Attendance Distribution among Students')
#     plt.savefig('output/attendance.png')

#     plt.figure(figsize=(6,4))
#     sns.histplot(x='Parental_Involvement', data=df)
#     plt.xlabel('Parental Involvement')
#     plt.ylabel('Number of Students')
#     plt.title('What amount of Parental Focus are Students getting?')
#     plt.savefig('output/involvement_of_parants.png')

#     plt.figure(figsize=(6,4))
#     sns.histplot(x='Access_to_Resources', data=df)
#     plt.xlabel('Access To Resources')
#     plt.ylabel('Number of Students')
#     plt.title('Are there enough Resources present?')
#     plt.savefig('output/students_access.png')

#     plt.close()

#     print("EDA completed and saved.")

# # Step 5: Define Prefect Flow
# @flow(log_prints=True)
# def student_performance_s():
#     # Step 1: Load Data
#     data = load_dataset()
    
    # Define the full path to the script based on the project structure
    script_path = os.path.join(os.path.dirname(__file__), '/Users/mkmac/Documents/API_assignment_1/tasks', script_name)
    
    try:
        # Run the external Python script using its full path
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        
        # Log both stdout and stderr
        if result.returncode == 0:
            logger.info(f"Successfully executed {script_name}:\n{result.stdout}")  # Log standard output
        else:
            logger.error(f"Error in {script_name}: {result.stderr}")  # Log standard error

        # Always print both stdout and stderr, regardless of success or failure
        print(result.stdout)
        print(result.stderr)

    except Exception as e:
        logger.error(f"Failed to execute {script_name}: {str(e)}")

    return 0

@flow
def student_performance_factors():
    # Run tasks sequentially and capture the results
   data1 = run_task("BasicStats.py")
   data2 = run_task("Binning.py", wait_for=[data1])  
   data3 = run_task("PearsonCorrelation.py", wait_for=[data2])
   data4 = run_task("Encoding.py", wait_for=[data3]) 
   data5 = run_task("CorrelationCoffecient.py", wait_for=[data4]) 
   data6 = run_task("FeatureImportanceMLAlgorithms.py", wait_for=[data5])
   data7 = run_task("Visualization.py", wait_for=[data6]) 

# To run locally
if __name__ == "__main__":
    student_performance_factors.serve(name="student_performance_factors",
                      tags=["studentperfromacefactors datascience project workflow"],
                      parameters={},
                      interval=60)