import pandas as pd
import numpy as np

# Read CSV file into DataFrame df
df = pd.read_csv('test_data.csv', index_col=0)
print(df)

print(f"this is the mean for each column:\n {df.mean()}")
print(f"this is the mean for each row:\n {df.mean(1)}")
print(f"this is the sum for each column:\n {df.sum()}")
print(f"this is the std for each column:\n {df.std()}")
print(f"this is the cumumlative sum for each column:\n {df.cumsum()}")