import sys
import os

# Add folder to Python path manually
sys.path.append(os.path.join(os.path.dirname(__file__), 'logging-llm'))

from logging_llm.chatbot_logging import *
from logging_llm.models_100.ollama_3_100 import *


if __name__ == "__main__":
    print("Welcome to Vollama Console Chatbot!")
    ollama_100_3()
    #load()  # Call chatbot loader function
    
