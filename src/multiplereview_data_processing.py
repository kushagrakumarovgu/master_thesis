import pandas as pd


df = pd.read_csv('src/csv_data/all_data_17.csv')
print(len(df))

#def convert_review_to_string(review):
#    return eval(review)[1:]

#df['review'] = df['review'].apply(convert_review_to_string)

#df.to_csv('csv_data/all_data_19_clean.csv', index=False)
