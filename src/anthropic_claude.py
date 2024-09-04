from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from helpers import claude_api_key
from prompts import human_template
from data_classes import ModelOutput
from dotenv import load_dotenv
import argparse
import pandas as pd
import time
import random
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='claude_inference.log')


load_dotenv()

#Create the parser
parser = argparse.ArgumentParser(description='Process some csv file.')

# Add the --csv-file argument
parser.add_argument('--csv-file', type=str, required=True, help='Path to the CSV file')
parser.add_argument('--output-file-path', type=str, required=True, help='Path to the output CSV file')

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0,
    max_tokens=1024,
    timeout=None,
    #max_retries=2,
    #api_key=claude_api_key,
    # base_url="...",
    # other params...
)

def generate_inference_claude(review: str):

    pydantic_parser = PydanticOutputParser(pydantic_object=ModelOutput)

    format_instructions = pydantic_parser.get_format_instructions()

    prompt = PromptTemplate(
        template=human_template,
        input_variables=["review"],
        partial_variables={"format_instructions": format_instructions},
    )

    chain = prompt | llm | pydantic_parser
    #print(f"{chain=}")

    model_output = chain.invoke({"review": review})
    #print(f"{model_output=}")

    return model_output


args = parser.parse_args()

if __name__ == "__main__":
    
    # Get the CSV file path.
    csv_file_path = args.csv_file
    print(f'The path to the CSV file is: {csv_file_path}')
    output_file_path = args.output_file_path
    print(f'The path to the output CSV file is: {output_file_path}')

    df = pd.read_csv(csv_file_path)
    # for testing - only take 5 rows.
    #df = df.head(5)

    output_list = []

    output_cols = ['review', 'reasoning', 'sentiment_score', 'politeness_score']
    
    for index, row in df.iterrows():
        #print(row)
        #row = row[1]
        try:
            review = row['review']

            #time.sleep(random.randint(5, 10))

            output = generate_inference_claude(review)

            output_dict = output.dict()
            output_dict['review'] = review

            output_dict = { col:output_dict[col] for col in output_cols }
        except Exception as e:
            print(f"Error in row : {index} Error : {e}")
            logging.error(f"Error in row : {index} Error : {e}")
            print(e)
            output_dict = { col:None for col in output_cols }
            output_dict['review'] = row['review']
            output_dict = { col:output_dict[col] for col in output_cols }

        output_list.append(output_dict)
        print(f"Row : {index} done")

    df_output = pd.DataFrame(output_list)

    df_output.to_csv(output_file_path, index=False)

