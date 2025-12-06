import json

with open("abc.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["age"])
print(data["city"])
# t