import pandas as pd
import numpy as np

# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)
print(df)
#sets the 3rd row 1st column to be 0
df.at[3, "label1"] = 0
print(df)
#same deal but with indexes
df.iat[5, 0] = 0
#use selection to modify many rows at once
df.iloc[:, 2] = np.array([5] * len(df))
#showing dataframe after modifications
print(f"after modifications: \n{df}")

print(f"after dropping a column:\n {df.drop('label1', axis = 'columns')}")

#now, to demonstrate recovery from missing data
#this code will make a copy of the dataframe with one extra column
df1 = df.reindex(index=list(df.index), columns = list(df.columns) + ["test"])
print(df1)
print(f"Boolean mask of nans: \n {pd.isna(df1)}")
print(f"Drop nans (will yield an empty frame here): \n {df1.dropna(how ='any')}")
print(f"Fill nans \n {df1.fillna(value = 5)}")