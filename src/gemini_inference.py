from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from helpers import gemini_api_key
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
                    filename='gemini_inference.log')

load_dotenv()

# Create the parser
parser = argparse.ArgumentParser(description='Process some csv file.')

# Add the --csv-file argument
parser.add_argument('--csv-file', type=str, required=True, help='Path to the CSV file')
#parser.add_argument('--output-file-path', type=str, required=True, help='Path to the output CSV file')


# Now we can instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=3,
    google_api_key=gemini_api_key,
)

def generate_inference_gemini(review: str):

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
    # Get file name from csv_file_path
    file_name = csv_file_path.split('/')[-1]
    output_file_path = f"src/new_results/{file_name.replace('.csv', '_geminipro_output.csv')}"
    #output_file_path = csv_file_path.replace('.csv', '_gemini_sample_5_output.csv')
    print(f'The path to the output CSV file is: {output_file_path}')

    df = pd.read_csv(csv_file_path)
    # for testing - only take 5 rows.
    #df = df.head(5)

    output_list = []

    output_cols = ['review', 'reasoning', 'sentiment_score', 'politeness_score']
    
    for index, row in df.iterrows():
        review_list = eval(row['review'])
        outputs = list()
        #print(row)
        #row = row[1]
        import time
        time.sleep(5)
        for review in review_list:
            for _ in range(3):
                try: 
                    output = generate_inference_gemini(review)
                    break
                except Exception as e:
                    print(f"Error in row : {index} Error : {e}")
                    logging.error(f"Error in row : {index} Error : {e}")
                    #TODO: Handle an empty output
                    output = ModelOutput(reasoning="ERROR", sentiment_score=0, politeness_score=0)
                    print(e)
                    continue

            outputs.append(output)
        
        output_dict = dict()
        #print(f"outputs : {outputs}")

        output_dict['reviews'] = row['review']
        output_dict['sentiment_scores'] = [output.sentiment_score for output in outputs]
        output_dict['politeness_scores'] = [output.politeness_score for output in outputs]
        output_dict['reasonings'] = [output.reasoning for output in outputs]

        output_list.append(output_dict)
        print(f"Row {index} done!!.")

    df_output = pd.DataFrame(output_list)

    df_output.to_csv(output_file_path, index=False)
