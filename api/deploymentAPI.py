# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "cli-6775a16f-27ad-483f-b58d-8118642fc7d0"  # Your Prefect Cloud API key
ACCOUNT_ID = "7537c1be-d2ed-476b-86f2-07e43aa776de"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "5d43022c-3f8c-45c4-9994-eaa56b807de8"  # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "be5e17f9-32ce-4331-b367-bac8ddb7757a"  # Your Deployment ID

# Correct API URL to get deployment details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/deployments/{DEPLOYMENT_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    deployment_info = response.json()
    print(deployment_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
