import pandas as pd

# Load the csv data
df_19 = pd.read_csv("csv_data/all_data_19_clean.csv")
print(df_19.columns)
print(df_19.shape)

print("Gemini" + '#' * 40)
# Load results data
df_gemini_19 = pd.read_csv("results/final/geminipro_data_2019results.csv")
print(df_gemini_19.columns)
print(df_gemini_19.shape)

# Merge the data on the 'review' column
df_gemini_merge_19 = pd.merge(df_19, df_gemini_19, on='review')
print(df_gemini_merge_19.columns)
print(df_gemini_merge_19.shape)

print("Claude" + "#" * 40)
df_claude_19 = pd.read_csv("results/final/anthropic_claude_all_2019results.csv")
print(df_claude_19.columns)
print(df_claude_19.shape)

# Merge the data on the 'review' column
df_claude_merge_19 = pd.merge(df_19, df_claude_19, on='review')
print(df_claude_merge_19.columns)
print(df_claude_merge_19.shape)

print("ChatGPT4o" + "#" * 40)
df_chatgpt_19 = pd.read_csv("results/final/chatgpt_4o_all_data_2019.csv")
print(df_chatgpt_19.columns)
print(df_chatgpt_19.shape)

# Merge the data on the 'review' column
df_chatgpt_merge_19 = pd.merge(df_19, df_chatgpt_19, on='review')
print(df_chatgpt_merge_19.columns)
print(df_chatgpt_merge_19.shape)


# Save the merged data
df_gemini_merge_19.to_csv("results/final/geminipro_data_2019finalresults.csv", index=False)
df_claude_merge_19.to_csv("results/final/anthropic_claude_all_2019finalresults.csv", index=False)
df_chatgpt_merge_19.to_csv("results/final/chatgpt_4o_all_data_2019finalresults.csv", index=False)