# find nan in a dataframe
boolean_index = df['value'].isnull().values.reshape(-1) # -1 stands for 1-d array
df_output = df.loc[boolean_index] # or df[boolean_index]
