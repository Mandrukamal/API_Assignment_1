import boto3

# Create a low-level client representing Amazon SageMaker Runtime
sagemaker_runtime = boto3.client("sagemaker-runtime", region_name='ap-south-1')

# The endpoint name
endpoint_name = 'canvas-studentPredictedDeployement'

# Specify the content type of the input data
content_type = 'application/json'

# Gets inference from the model hosted at the specified endpoint:
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Body=bytes('{"features": [23.0,84.0,1.0,0.0,0.0,7.0,73.0,1.0,1.0,0.0,1.0,2.0,1.0,2.0,3.0,0.0,1.0,2.0,1.0]}', 'utf-8')
)

# Decodes and prints the response body:
print(response['Body'].read().decode('utf-8'))