import pandas as pd
import numpy as np

# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)
df2 = pd.read_csv('test_data_2.csv', index_col=0)

df_concat = pd.concat([df, df2]) #avoid calling this many times, as it is expensive
print(df_concat)

#we can split labels into groups, which is very useful when we are querying a specific category
print(f"Grouped by their names and summed: \n{df_concat.groupby('names').sum()}")
print(f"Grouped by their names then their label 3 then summed: \n{df_concat.groupby(['names', 'label3']).sum()}")

#we can make heirarchical axes to "compress" a level in the columns
stacked = df_concat.stack()
print(stacked)