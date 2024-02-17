import os
from dotenv import load_dotenv
load_dotenv(".env")

openai_api_key = os.getenv("OPENAI_API_KEY")
gpt_model = os.getenv("GPT_MODEL")

