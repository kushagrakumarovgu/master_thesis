import os
from dotenv import load_dotenv
load_dotenv(".env")

openai_api_key = os.getenv("OPENAI_API_KEY")
gpt_model = os.getenv("GPT_MODEL")
gemini_api_key = os.getenv("GEMINI_API_KEY")
claude_api_key = os.getenv("CLAUDE_API_KEY")

