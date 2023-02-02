import json
with open("setting.json",mode = "r") as file:
    data = json.load(file)

print(data["name"])