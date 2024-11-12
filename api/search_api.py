import requests
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def perform_web_search(query):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 3
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        return response.json().get("organic_results", [])
    return []
