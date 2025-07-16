import os
import azure.functions as func
import logging
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Helper function to extract info using LLM

def extract_meeting_info(transcript, llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are an assistant that organizes meeting transcripts. Given the following transcript, extract:
        1. The main topics discussed (as a list)
        2. Any goals or action items set (as a list)
        3. Any deadlines or due dates mentioned (as a list, with context)
        
        Transcript:
        {transcript}
        
        Respond in JSON with keys: topics, goals, deadlines.
        """
    )
    chain = prompt | llm
    response = chain.invoke({"transcript": transcript})
    return response.content

#Main function
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing meeting transcript for organization.')
    try:
        data = req.get_json()
        transcript = data.get('transcript', '')
        if not transcript:
            return func.HttpResponse('Missing transcript.', status_code=400)

        # Set up Azure OpenAI LLM
        api_key = os.environ.get('AZURE_OPENAI_API_KEY')
        endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
        deployment = os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME')
        if not all([api_key, endpoint, deployment]):
            return func.HttpResponse('Azure OpenAI configuration missing.', status_code=500)

        llm = AzureChatOpenAI(
            openai_api_key=api_key,
            azure_endpoint=endpoint,
            deployment_name=deployment,
            openai_api_version="2023-05-15"
        )

        result = extract_meeting_info(transcript, llm)
        return func.HttpResponse(result, mimetype="application/json")
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500) 