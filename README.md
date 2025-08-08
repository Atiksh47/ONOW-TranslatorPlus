# ONOW-TranscriptPlus

An Azure Functions application that processes meeting transcripts using LangChain and Azure OpenAI to extract key information including topics, goals, and deadlines.

## Overview

This Azure Function takes meeting transcripts as input and uses Azure OpenAI's language model to intelligently extract and organize the following information:

- **Main topics discussed** - Key subjects covered during the meeting
- **Goals and action items** - Specific objectives and tasks assigned
- **Deadlines and due dates** - Time-sensitive commitments with context

## Features

- 🤖 **AI-Powered Analysis**: Uses Azure OpenAI's advanced language models
- 📋 **Structured Output**: Returns organized JSON responses
- 🔒 **Secure**: Azure Functions authentication and environment-based configuration
- 🚀 **Scalable**: Serverless architecture for automatic scaling

## Prerequisites

- Azure subscription
- Azure OpenAI service deployed
- Python 3.8 or higher
- Azure Functions Core Tools

## Setup

### 1. Local Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd ONOW-TranscriptPlus

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `local.settings.json` file with your Azure OpenAI credentials:

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "",
    "AZURE_OPENAI_API_KEY": "your-api-key-here",
    "AZURE_OPENAI_ENDPOINT": "https://your-resource.openai.azure.com/",
    "AZURE_OPENAI_DEPLOYMENT_NAME": "your-deployment-name"
  }
}
```

### 3. Azure OpenAI Setup

1. Create an Azure OpenAI resource in the Azure portal
2. Deploy a GPT model (e.g., gpt-35-turbo or gpt-4)
3. Note your endpoint, API key, and deployment name
4. Add these values to your environment configuration

## Usage

### Local Development

```bash
# Start the function locally
func start
```

The function will be available at `http://localhost:7071/api/process-transcript`

### API Endpoint

**POST** `/api/process-transcript`

**Request Body:**
```json
{
  "transcript": "Meeting transcript text here..."
}
```

**Response:**
```json
{
  "topics": ["Topic 1", "Topic 2", "Topic 3"],
  "goals": ["Goal 1", "Goal 2"],
  "deadlines": ["Deadline 1 with context", "Deadline 2 with context"]
}
```

### Example Usage

```bash
curl -X POST http://localhost:7071/api/process-transcript \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "In today\'s meeting, we discussed the Q4 marketing strategy. John will prepare the budget by Friday, and Sarah needs to finalize the campaign timeline by next Monday."
  }'
```

## Deployment

### Azure Functions Deployment

1. **Using Azure CLI:**
   ```bash
   az functionapp create --name your-function-app --storage-account your-storage-account --consumption-plan-location eastus --resource-group your-resource-group --runtime python --functions-version 4
   ```

2. **Deploy the function:**
   ```bash
   func azure functionapp publish your-function-app
   ```

3. **Configure environment variables in Azure:**
   - Go to your Function App in Azure Portal
   - Navigate to Configuration > Application settings
   - Add the following app settings:
     - `AZURE_OPENAI_API_KEY`
     - `AZURE_OPENAI_ENDPOINT`
     - `AZURE_OPENAI_DEPLOYMENT_NAME`

## Project Structure

```
ONOW-TranscriptPlus/
├── main.py              # Main Azure Function entry point
├── function.json        # Function configuration
├── requirements.txt     # Python dependencies
├── local.settings.json  # Local development settings
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Dependencies

- `azure-functions`: Azure Functions runtime
- `langchain`: LLM orchestration framework
- `azure-ai-openai`: Azure OpenAI client library

## Error Handling

The function includes comprehensive error handling for:
- Missing transcript data
- Azure OpenAI configuration issues
- LLM processing errors
- General exceptions

## Security Considerations

- API keys are stored as environment variables
- Function uses Azure Functions authentication
- Local settings are excluded from version control
- HTTPS is enforced in production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `func start`
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please create an issue in the repository or contact the development team. 