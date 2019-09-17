# find nan in dataframe, using boolean index
boolean_index = df['value'].isnull().values.reshape(-1) # -1 stands for 1-d array
df_output = df.loc[boolean_index] # or df[boolean_index]

# deep copy and shallow copy
# pandas的df和series在传递时默认是浅拷贝；即便是向方程传递参数，也是浅拷贝；所以要及时copy。

# find the index of nan in ndarray
np.argwhere(np.isnan(data))

# remove nan from an numpy array
x = x[~numpy.isnan(x)]
