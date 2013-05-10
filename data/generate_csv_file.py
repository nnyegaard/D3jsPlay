import json
import csv


with open("ToNAFFIN.json", "r") as content:
    json_data = content.read()

data = json.loads(json_data)

my_list = []

my_list.append(["id", "lat", "lon", "rate"])

for i in data.keys():
    my_list.append([i, data[i]["latitude"], data[i]["longitude"], data[i].get("5", 0.0)])


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(my_list)