import pandas as pd
# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)

# Show dataframe
print(df)
#for more information on how to deal with dataframes, look at the Pandas folder
# https://pythonbasics.org/read-csv-with-pandas/