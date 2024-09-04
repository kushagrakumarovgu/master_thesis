from openai_inference import generate_inference
from examples import sample_review
import pandas as pd
import os
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some csv file.')

# Add the --csv-file argument
parser.add_argument('--csv-file', type=str, required=True, help='Path to the CSV file')
parser.add_argument('--output-file-path', type=str, required=True, help='Path to the output CSV file')

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    
    # Get the CSV file path.
    csv_file_path = args.csv_file
    print(f'The path to the CSV file is: {csv_file_path}')
    output_file_path = args.output_file_path
    print(f'The path to the output CSV file is: {output_file_path}')

    df = pd.read_csv(csv_file_path)
    # for testing - only take 5 rows.
    #df = df.head(2)

    output_list = []

    output_cols = ['review', 'reasoning', 'sentiment_score', 'politeness_score']
    
    for index, row in df.iterrows():
        #print(row)
        #row = row[1]
        try:
            review = eval(row['review'])[0]

            output = generate_inference(review)

            output_dict = output.dict()
            output_dict['review'] = review

            output_dict = { col:output_dict[col] for col in output_cols }
        except Exception as e:
            print(f"Error in row : {index}")
            print(e)
            output_dict = { col:None for col in output_cols }
            output_dict['review'] = eval(row['review'])[0]
            output_dict = { col:output_dict[col] for col in output_cols }

        output_list.append(output_dict)
        print(f"Row : {index} done")


    df_output = pd.DataFrame(output_list)

    df_output.to_csv(output_file_path, index=False)
    