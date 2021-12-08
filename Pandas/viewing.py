import pandas as pd
# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)

# Show dataframe
print(df)
#show the top 2 rows
print(f"top 2 rows: {df.head(2)}")
#show the bottom 3 rows
print(f"bottom 3 rows: {df.tail(3)}")
print(f"These are the index: {df.index}") #the leftmost tcolumn. in this case, there is no index
print(f"These are the columns: {df.columns}")
print(f"This is the numpy array: {df.to_numpy()}") #excludes index and column labels
print(f"quick stats: {df.describe()}")
print(f"Transposing: {df.T}")
print(f"Sorting by axis: {df.sort_index(axis=1, ascending=False)}")
print(f"Sorting by values: {df.sort_values(by='prop_success')}")