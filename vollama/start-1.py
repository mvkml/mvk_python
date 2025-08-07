import requests
import json

url = "http://localhost:11434/generate"

data = {
    "model":"llama3.2",
    "prompt":"tell me short story"
}

response = requests.post(url,json = data,stream=True)
