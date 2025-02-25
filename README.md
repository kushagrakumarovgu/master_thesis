# Bias Detection Tool using various LLMs.

## Steps to prepare the tool environment
1. Python Version required:
```
python --version
Python 3.10.12
```
2. Create python virtual environment
```
python3 -m venv env
source env/bin/activate
```
3. Install required packages.
```
pip3 install -r requirements.txt
```

4. Create .env file in the master_thesis folder and populate the values of the below env variables. 
<b>NOTE:</b> The env values shown below are dummy values. You need to get your own API keys.
```
OPENAI_API_KEY=OPENAI_DUMMY_KEY_XXXXXYYYYYY
GPT_MODEL=gpt-4o

GEMINI_API_KEY=GEMINI_DUMMY_KEY_XXXXXYYYYYY
GROQ_API_KEY=GROQ_DUMMY_KEY_AAAAABBBBBBB
ANTHROPIC_API_KEY=ANTHROPIC_DUMMY_KEY_ZZZZZ_HHHHHH
```

