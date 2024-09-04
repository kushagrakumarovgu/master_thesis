import pandas as pd
from glob import glob

#df = pd.concat(map(pd.read_csv, glob("results/anthropic_claude_all_2018_*.csv")))
#df = pd.concat(map(pd.read_csv, glob("results/anthropic_claude_all_2019_*.csv")))

#df = pd.concat(map(pd.read_csv, glob("results/gemini*_17_*.csv")))
df = pd.concat(map(pd.read_csv, glob("results/gemini*_18_*.csv")))

print(df.columns)
print(df.shape)
print(df.head())
print(df.tail())
print(df.isnull().sum())

#df.to_csv("results/anthropic_claude_all_2018results.csv", index=False)
#df.to_csv("results/anthropic_claude_all_2019results.csv", index=False)


#df.to_csv("results/geminipro_data_2017results.csv", index=False)
df.to_csv("results/geminipro_data_2018results.csv", index=False)
