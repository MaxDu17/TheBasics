import csv
#this approach typically won't be very fun to do 

with open("samples/test_data.csv", "r") as f:
    dialect = csv.Sniffer().sniff(f.read(25)) #use this to determine the format of the csv. You can also omit this for convenience
    f.seek(0)
    reader = csv.reader(f, dialect=dialect)
    for line in reader:
        print(line)

with open("samples/test_data_written.csv", "w", newline="") as f:
    #the newline argument makes it so there isn't a blank space between every line
    writer = csv.writer(f)
    writer.writerow([2,5,6])
    writer.writerows([[1, 2, 3], {1, 43,6}])

#now, the pandas way
import pandas as pd
# Read CSV file into DataFrame df
df = pd.read_csv('samples/test_data.csv', index_col=0)
df.to_csv("samples/test_data_written_pandas.csv")
