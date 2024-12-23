import pandas as pd
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some csv file.')

# Add the --csv-file argument
parser.add_argument('--data-file', type=str, required=True, help='Path to the original CSV file')
parser.add_argument('--result-file', type=str, required=True, help='Path to the result CSV file')


def apply_eval(x):
  return eval(x)

def convert_to_list(df):
  for index, row in df.iterrows():
    for col in df.columns:
      #print(index, col, row[col])
      #df.loc[index, col] = apply_eval(row[col])
      df.at[index, col] = apply_eval(row[col])

  return df

# Parse the arguments
args = parser.parse_args()

data_file = args.data_file
result_file = args.result_file
result_file_name = result_file.split('/')[-1]

output_file = f"src/new_results/final_result/{result_file_name.replace('.csv', '_final.csv')}"

# Load the original data
df_data = pd.read_csv(data_file)

# For 2018 and 2019 dataset New column order
new_order = ['title', 'decision', 'year', 'Authors', 'academic_age', 'current_age',
             'total_num_pub', 'total_num_conference', 'total_num_informal',
             'total_num_journal', 'review', 'rating_score', 'rating_text',
             'confidence_score', 'confidence_text']

df_data = df_data[new_order]
print(df_data.columns)
#print(len(df_data.columns))
#print(df_data.loc[0].values)
df_result = pd.read_csv(result_file)

df_result.columns = ['review', 'sentiment_scores', 'politeness_scores', 'reasonings']

df_merged = df_data.merge(df_result, on='review')

df_merged_to_list = convert_to_list(df_merged[df_merged.columns[3:]])

df_merged.loc[:, df_merged.columns[3:]] = df_merged_to_list

#print(df_merged.loc[0].values)
print(df_merged.head(1))
print(df_merged.head(1).values)

# Save the merged data
df_merged.to_csv(output_file, index=False)