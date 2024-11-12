import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def extract_info_with_llm(entity, search_results, user_prompt):
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

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",  
            headers=headers,
            json=data
        )
        response.raise_for_status()
        result = response.json()
   
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error with Groq API: {e}"
