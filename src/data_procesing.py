import pandas as pd


df = pd.read_csv('csv_data/all_data_19.csv')

def convert_review_to_string(review):
    return eval(review)[0]

df['review'] = df['review'].apply(convert_review_to_string)

df.to_csv('csv_data/all_data_19_clean.csv', index=False)