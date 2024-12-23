import pandas as pd
from glob import glob

#df = pd.concat(map(pd.read_csv, glob("results/anthropic_claude_all_2018_*.csv")))
#df = pd.concat(map(pd.read_csv, glob("results/anthropic_claude_all_2019_*.csv")))

#df = pd.concat(map(pd.read_csv, glob("results/gemini*_17_*.csv")))
#df = pd.concat(map(pd.read_csv, glob("results/gemini*_18_*.csv")))
#df = pd.concat(map(pd.read_csv, glob("src/new_results/all_data_18*output_*")))
df = pd.concat(map(pd.read_csv, glob("src/new_results/all_data_19_anthropic*output_*")))

#for file in glob("src/new_results/all_data_18*output_*"):
#    df = pd.read_csv(file)
#    print(file)
#    print(df.head(2))
#    print(df.shape)
#    print(df.tail(2))
#    print(df[df.duplicated()])

print(df.columns)
print(df.shape)
#print(df.head())
#print(df.tail())
print(df.isnull().sum())
print(df.duplicated().sum())
#print(df.duplicated)

#df = df.drop_duplicates()
#print(df.shape)
#df.to_csv("results/anthropic_claude_all_2018results.csv", index=False)
#df.to_csv("results/anthropic_claude_all_2019results.csv", index=False)
df.to_csv("src/new_results/all_data_19_anthropic_claude_sonnet_output.csv", index=False)

#df.to_csv("results/geminipro_data_2017results.csv", index=False)
#df.to_csv("results/geminipro_data_2018results.csv", index=False)
