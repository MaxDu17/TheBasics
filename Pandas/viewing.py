import pandas as pd
# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)

# Show dataframe
print(df)
print(f"The number of rows:\n{len(df)}")
#show the top 2 rows
print(f"top 2 rows: {df.head(2)}")
#show the bottom 3 rows
print(f"bottom 3 rows:\n {df.tail(3)}")
print(f"These are the index:\n {df.index}")
print(f"These are the columns:\n {df.columns}")
print(f"This is the numpy array:\n {df.to_numpy()}") #excludes index and column labels
print(f"quick stats:\n {df.describe()}")
print(f"Transposing:\n {df.T}")
print(f"Sorting by axis:\n {df.sort_index(axis=1, ascending=False)}")
print(f"Sorting by column value:\n {df.sort_values(by='label1')}")