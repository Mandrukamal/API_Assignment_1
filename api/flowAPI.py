# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_eV1mrDrrHZhK36CsR5rAlYOnN1KqKO3smWqG"  # Your Prefect Cloud API key
ACCOUNT_ID = "b31bc8d1-2034-4493-8b4c-bcfc65e5c985"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "479354b6-1ff7-41a6-a2fa-d03eb91e6375"  # Your Prefect Cloud Workspace ID
FLOW_ID = "fee0b8ea-4107-411b-93d7-d024be07c700"  # Your Flow ID

# Correct API URL to get flow details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flows/{FLOW_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    flow_info = response.json()
    print(flow_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
