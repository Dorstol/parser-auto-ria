import json

with open("cars.json") as json_file:
    data = json.load(json_file)

for car in data:
    if "BMW" in car["name"] and int(car["price"]) <= 10000:
        print(car)