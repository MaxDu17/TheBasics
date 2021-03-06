import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

with open("samples/sample.json", "r") as f:
  data = json.load(f) #data is now a nested dictionary
  with open("samples/sample.json", "r") as g:
    data2 = json.load(g)
  data.update(data2) #redundant, but imagine if data2 were different values

y = json.dumps(x) #this creates a json string
y_data = json.loads(y) #this does the reverse of dumps (the "s" is for string)

with open("samples/sample_written.json", "w") as f:
  f.write(y) #it's that simple!!



