import pandas as pd
import numpy as np

#the idea is the a series is like a vector and we can use it to make dataframes
s = pd.Series([1, 3, 5, 4, 6, 8]) #this makes a "series" object
print(s)

#we make a 2d array whose content is np.random.randn, x axis is the dates, and the y is the columns
df = pd.DataFrame(np.random.randn(6, 4), index=list("123456"), columns=list("ABCD"))
print(df)
print(df.dtypes) #get the datatypes

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"), #autobroadcast
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo", #autobroadcast
    }
)
print(df2)