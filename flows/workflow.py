import pandas as pd
from prefect import flow, task
from sklearn.preprocessing import MinMaxScaler
import numpy as np # linear algebra
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib as plt
import seaborn as sns

@task
def load_dataset():
    # Load the dataset from a local file path
    file_path = "/Users/mkmac/Documents/API_assignment_1/data/StudentPerformanceFactors.csv"  # Update this path as needed
    return pd.read_csv(file_path)

# Step 4: Model Training
@task
@task(log_prints=True)
def preprocess_data(df):
    # Train your machine learning model with Logistic Regression
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    from sklearn.preprocessing import LabelEncoder
    from sklearn.impute import SimpleImputer
    import matplotlib as plt
    import seaborn as sns
    missing_values = df.isna().sum().sum()
    print('missing values are')
    print(missing_values)

    teacher_encoder = LabelEncoder()
    df['Teacher_Quality'] = teacher_encoder.fit_transform(df['Teacher_Quality'])
    df['Teacher_Quality']

    parent_education_encoder = LabelEncoder()
    df['Parental_Education_Level'] = parent_education_encoder.fit_transform(df['Parental_Education_Level'])
    df['Parental_Education_Level']

    distance_encoder = LabelEncoder()
    df['Distance_from_Home'] = distance_encoder.fit_transform(df['Distance_from_Home'])
    df['Distance_from_Home']


    Parental_Involvement = LabelEncoder()
    df['Parental_Involvement'] = Parental_Involvement.fit_transform(df['Parental_Involvement'])
    df['Parental_Involvement']

    Access_to_Resources = LabelEncoder()
    df['Access_to_Resources'] = Access_to_Resources.fit_transform(df['Access_to_Resources'])
    df['Access_to_Resources']

    Extracurricular_Activities = LabelEncoder()
    df['Extracurricular_Activities'] = Extracurricular_Activities.fit_transform(df['Extracurricular_Activities'])
    df['Extracurricular_Activities']

    Motivation_Level = LabelEncoder()
    df['Motivation_Level'] = Motivation_Level.fit_transform(df['Motivation_Level'])
    df['Motivation_Level']

    Internet_Access = LabelEncoder()
    df['Internet_Access'] = Internet_Access.fit_transform(df['Internet_Access'])
    df['Internet_Access']

    Family_Income = LabelEncoder()
    df['Family_Income'] = Family_Income.fit_transform(df['Family_Income'])
    df['Family_Income']

    School_Type = LabelEncoder()
    df['School_Type'] = School_Type.fit_transform(df['School_Type'])
    df['School_Type']

    Peer_Influence = LabelEncoder()
    df['Peer_Influence'] = Peer_Influence.fit_transform(df['Peer_Influence'])
    df['Peer_Influence']

    Learning_Disabilities = LabelEncoder()
    df['Learning_Disabilities'] = Learning_Disabilities.fit_transform(df['Learning_Disabilities'])
    df['Learning_Disabilities']

    Gender = LabelEncoder()
    df['Gender'] = Gender.fit_transform(df['Gender'])
    df['Gender']
    
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    return df_imputed

# Step 5: Define Prefect Flow
@flow(log_prints=True)
def student_peformance_s():
    # step 1 = loading data
    data = load_dataset()
    # step 2 = preprocessing
    # preprocessed_data = preprocess_data(data)
    # step 3 = data modeling
    eda = eda(data)

    #print("Accuracy: ", accuracy)
   

# Step 6: Run the Prefect Flow
if __name__ == "__main__":
    student_peformance_s.serve(name="student-performance-data-2",
                      tags=["first workflow"],
                      parameters={},
                      interval=5)
