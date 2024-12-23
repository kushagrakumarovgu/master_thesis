import pandas as pd

#df = pd.read_csv('src/new_results/all_data_18_anthropic_claude_sonnet_output.csv')
#df = pd.read_csv('src/new_results/all_data_18_anthropic_claude_sonnet_output_c.csv')
df = pd.read_csv('src/new_results/all_data_19_anthropic_claude_sonnet_output_test_for_2.csv')
print(f"{len(df)=}")
print(df.columns)
print(df.loc[0].values)
print(df.isnull().sum())