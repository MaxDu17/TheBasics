import csv
#this approach typically won't be very fun to do 

with open("test_data.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)