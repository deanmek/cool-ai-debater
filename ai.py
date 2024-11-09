from openai import OpenAI

# Initialize the client with your API key
YOUR_API_KEY = "API KEY HERE"
client = OpenAI(api_key=YOUR_API_KEY, base_url="https://openrouter.ai/api/v1")

def aiQuery(question):
    """
    Function to query the AI model with a single question.
    
    Args:
        question (str): The question to ask the AI.
        
    Returns:
        str: The response from the AI.
    """
    messages = [
        {
            "role": "user",
            "content": question,
        }
    ]
    
    response = client.chat.completions.create(
        model="google/gemini-flash-1.5",
        messages=messages,
    )
    
    # Extract and return the content of the response
    return response['choices'][0]['message']['content']

def agentResponse(system_prompt, conversation_history):
    """
    Function to query the AI model with a system prompt and conversation history.
    
    Args:
        system_prompt (str): The system-level prompt describing the AI's behavior.
        conversation_history (str): The conversation history to provide context.
        
    Returns:
        str: The response from the AI.
    """
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": conversation_history,
        }
    ]
    
    response = client.chat.completions.create(
        model="google/gemini-flash-1.5",
        messages=messages,
    )
    
    # Extract and return the content of the response
    return response['choices'][0]['message']['content']
