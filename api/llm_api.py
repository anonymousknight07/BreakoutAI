import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Get API key with validation
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

def extract_info_with_llm(entity, search_results, user_prompt):
    # Combine search results
    combined_text = "\n\n".join([result["snippet"] for result in search_results])
    prompt_content = user_prompt.replace("{entity}", entity) + f"\n\n{combined_text}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama3-8b-8192",  
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_content}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    api_url = "https://api.groq.com/openai/v1/chat/completions"

    try:
        # Print request details for debugging 
        print(f"API Key prefix: {GROQ_API_KEY[:8]}...")
        print(f"Request URL: {api_url}")
        
        response = requests.post(
            api_url,
            headers=headers,
            json=data,
            timeout=30
        )
        
        # Print response status and content for debugging
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text[:200]}")  # Print first 200 chars
        
        response.raise_for_status()
        result = response.json()
        
        return result["choices"][0]["message"]["content"].strip()
    
    except requests.exceptions.RequestException as e:
        error_msg = f"Error with Groq API: {str(e)}"
        print(error_msg)  # Log the error
        return error_msg
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)  # Log the error
        return error_msg