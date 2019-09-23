# find nan in dataframe, using boolean index
boolean_index = df['value'].isnull().values.reshape(-1) # -1 stands for 1-d array
df_output = df.loc[boolean_index] # or df[boolean_index]

# find the index of nan in ndarray
np.argwhere(np.isnan(data))

# remove nan from an numpy array
x = x[~numpy.isnan(x)]
