from openai import OpenAI
import logging
import json
from datetime import datetime
import uuid # universal unique identifier 
from dotenv import load_dotenv
import os
from logging_llm.utilities.app_constants import *

#load_dotenv()
# 🔧 Explicitly load the .env from the subfolder
load_dotenv(dotenv_path=os.path.join(LOGGING_LLM_DIR ,ENV_FILE_NAME))
api_key = os.getenv("OPENAI_API_KEY")

def load():
    print(f'api_key -- :{api_key}')
    return

def setup_logging():
    logger = logging.getLogger("chatbot")
    logger.setLevel(logging.INFO)
    
    #create file handler for json logs 
    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s%")
    )
    logger.addHandler(console_handler)
    