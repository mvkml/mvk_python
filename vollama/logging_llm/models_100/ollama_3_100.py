import requests
from logging_llm.utilities.api_utility import *
from logging_llm.models.llama3.llama3model import *


def ollama_100_3():
    url = get_prompt_url()
    payload = {
    "model": "llama3",           # Model name (make sure it’s pulled via ollama)
    "prompt": "Explain quantum computing simply. in one line",
    "stream": False              # Set to True if you want stream-style output
    }
    print(payload)
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"failed : {response.status_code}")
        
    print("process done")
    print("ollama_100_3 100 ollama 3")
    
    
