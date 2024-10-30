from prefect import flow, task, get_run_logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Task 1: Model Preparation
@task
def model_preparation():
    logger = get_run_logger()
    logger.info("Preparing models: Linear Regression and Random Forest Regressor")

    # Define models
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, random_state=42)
    }
    return models

# Task 2: Split Data
@task
def split_data(data):
    logger = get_run_logger()

    # Separate features and target
    X = data.drop(columns=['Exam_Score'])
    y = data['Exam_Score']

    # Split the data (70% training, 30% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    logger.info(f"Data split completed: {X_train.shape[0]} train samples, {X_test.shape[0]} test samples")
    
    return X_train, X_test, y_train, y_test

# Task 3: Train Models
@task
def train_models(X_train, y_train, models):
    trained_models = {}
    
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[model_name] = model
        
    return trained_models

# Task 4: Evaluate Models
@task
def evaluate_models(X_test, y_test, trained_models):
    logger = get_run_logger()

    for model_name, model in trained_models.items():
        # Predictions
        y_pred = model.predict(X_test)
        
        # Metrics
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        logger.info(f"{model_name} - MSE: {mse}, MAE: {mae}, R²: {r2}")

        # Log metrics using MLFlow
        with mlflow.start_run(run_name=model_name):
            mlflow.log_param("Model", model_name)
            mlflow.log_metric("MSE", mse)
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("R²", r2)
            
    logger.info("Model evaluation completed")

# Main Flow
@flow(name="student_performance_factors_ml_pipeline")
def student_performance_factors(file_path):
    # Load data (assumes data preprocessing has been done)
    data = pd.read_csv(file_path)

    # Model Preparation
    models = model_preparation()

    # Split Data
    X_train, X_test, y_train, y_test = split_data(data)

    # Train Models
    trained_models = train_models(X_train, y_train, models)

    # Evaluate Models
    evaluate_models(X_test, y_test, trained_models)

# Run the pipeline
if __name__ == "__main__":
    file_path = "data/ImputedStudentPerformanceFactors.csv"  # Update the path to your dataset
    student_performance_factors(file_path)
