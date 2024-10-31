from prefect import flow, task, get_run_logger
import subprocess
import os

@task(log_prints=True)  # Ensures all prints are captured in logs
def run_task(script_name):
    logger = get_run_logger()
    
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