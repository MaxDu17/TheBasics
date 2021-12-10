import pandas as pd
# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)

#select column by name
print(f"select column by name: \n{df['label1']}")
#select rows
print(f"select rows: \n{df[0:3]}")

# selection by names (column names, row names)
print(f"select row and column at same time: \n {df.loc[0, 'label1']}")
print(f"select rows and columns at same time: \n {df.loc[[0, 2], ['label1', 'label3']]}")

# selection by index. You can use a list or a slice
print(f"select rows and columns by indexes: \n {df.iloc[0:2, 1:3]}")
print(f"select columns by indexes: \n {df.iloc[:, 1:3]}")

# boolean indexing
print(f"boolean indexing:\n {df[df['label2'] > 10]}")
print(f"boolean indexing (another way):\n {df[df['label3'].isin([6, 74])]}")