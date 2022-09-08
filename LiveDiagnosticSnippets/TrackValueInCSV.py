import csv

# put this at the beginning
_diagnosis_writer = csv.writer(open("diagnosis.csv", "w", newline=""))
_diagnosis_writer.writerow(["step", "value"]) #change this up if you want

# put this where you want to monitor the values
i = 1
value = 253
_diagnosis_writer.writerow([i, value])