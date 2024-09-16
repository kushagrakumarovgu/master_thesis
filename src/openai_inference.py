from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from helpers import gpt_model
from prompts import human_template
from data_classes import ModelOutput
import pandas as pd
import argparse
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='openai_inference.log')


load_dotenv()

# Create the parser
parser = argparse.ArgumentParser(description='Process some csv file.')

# Add the --csv-file argument
parser.add_argument('--csv-file', type=str, required=True, help='Path to the CSV file')

GPT_MODEL = "gpt-4o"
model = ChatOpenAI(
    model=GPT_MODEL,
    temperature=0.1, # Not given the paper
    max_tokens=1000, # Not given in the paper 
    model_kwargs={
        "top_p": 1, # Not given in the paper
        "frequency_penalty": 0.0, # Not given in the paper
        "presence_penalty": 0.0, # Not given in the paper
    },
)

def generate_inference_openai(review: str):

    pydantic_parser = PydanticOutputParser(pydantic_object=ModelOutput)

    format_instructions = pydantic_parser.get_format_instructions()

    prompt = PromptTemplate(
        template=human_template,
        input_variables=["review"],
        partial_variables={"format_instructions": format_instructions},
    )

    chain = prompt | model | pydantic_parser
    #print(f"{chain=}")

    model_output = chain.invoke({"review": review})
    #print(f"{model_output=}")

    return model_output

# Parse the arguments
args = parser.parse_args()


if __name__ == "__main__":
    
    # Get the CSV file path.
    csv_file_path = args.csv_file
    print(f'The path to the CSV file is: {csv_file_path}')
    file_name = csv_file_path.split('/')[-1]
    output_file_path = f"src/new_results/{file_name.replace('.csv', '_openai_gpt4o_output.csv')}"
    print(f'The path to the output CSV file is: {output_file_path}')

    df = pd.read_csv(csv_file_path)
    # for testing - only take 5 rows.
    #df = df.head(5) 

    output_list = []

    output_cols = ['review', 'reasoning', 'sentiment_score', 'politeness_score']
    
    for index, row in df.iterrows():
        reviews = list()
        review_list = eval(row['review'])
        #print(f"{len(review_list)=}")
        outputs = list()
        import time
        time.sleep(5)
        for review in review_list:
            for _ in range(3):
                try: 
                    output = generate_inference_openai(review)
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
        print(f"Row : {index} done!")

    df_output = pd.DataFrame(output_list)

    df_output.to_csv(output_file_path, index=False)
