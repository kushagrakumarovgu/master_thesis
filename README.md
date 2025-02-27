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

## To Generate the sentiment_scores, politeness_scores and reasoning using different LLMs.
a. OpenAI ChatGPT:
```
python src/openai_inference.py --csv-file <path_to_the_input_csv>
```
*NOTE*: The output file will be created in the folder src/new_results and name of the output will be `<input_file_name>_openai_gpt4o_output.csv`

b. Google Gemini:
```
python src/gemini_inference.py --csv-file <path_to_the_input_csv>
```
*NOTE*: The output file will be created in the folder src/new_results and name of the output will be `<input_file_name>_geminipro_output.csv`


c. Anthropic claude:
```
python src/anthropic_claude.py --csv-file <path_to_the_input_csv>
```
*NOTE*: The output file will be created in the folder src/new_results and name of the output will be `<input_file_name>__anthropic_claude_sonnet_output.csv`

## FAQ:
1. If you get `TOO Many requests` 
This is most likely due to the large number of rows in the input file.Please break the input file into smaller files and run the script for each individual single small file.
Later you can combine the outputs together into a single output file.

2. If you get `Number of requests exceeded`
This is most likely due to the large number of rows in the input file.Please break the input file into smaller files and run the script for each individual single small file.
Later you can combine the outputs together into a single output file.
