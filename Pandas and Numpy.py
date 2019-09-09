# find nan in dataframe, using boolean index
boolean_index = df['value'].isnull().values.reshape(-1) # -1 stands for 1-d array
df_output = df.loc[boolean_index] # or df[boolean_index]

# deep copy and shallow copy
# pandas的df和series在传递时默认是浅拷贝，连向方程传递参数时也是浅拷贝，所以一定要及时copy。
