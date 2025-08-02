# azure-ai-engineer
This repository holds code related to the certification for the azure ai engineering certification including azure foundry. 


### Create a keys folder and add a keys.json file
This file should contain the following information:
```json
{
  "azure_foundry": {
    "subscription_id": "subscription-id-here",
    "resource_group": "resource-group-name-here",
    "workspace_name": "your-foundry-workspace-name",
    "api_key": "api-key-here",
    "endpoint": "https://project-name-here.eastus.api.azureml.ms",
    "api_version": "2023-05-01"
  },
  "authentication": {
    "tenant_id": "your-tenant-id-here",
    "client_id": "your-client-id-here",
    "client_secret": "your-client-secret-here"
  },
  "models": {
    "default_model": "gpt-4",
    "available_models": [
      "gpt-4",
      "gpt-35-turbo",
      "text-embedding-ada-002"
      
    ]
  },
  "settings": {
    "timeout": 30,
    "max_retries": 3,
    "rate_limit": {
      "requests_per_minute": 60,
      "tokens_per_minute": 40000
    }
  }
}   
```