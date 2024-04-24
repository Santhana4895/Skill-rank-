import json

# Read data from the JSON file
with open('ex5.json', 'r') as file:
    example = json.load(file)

# Find the "Old Fashioned" donut and add a new type of batter
for donut in example:
    if donut["name"] == "Old Fashioned" and donut["type"] == "donut":
        donut["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

# Write the modified data back to the JSON file
with open('ex5.json', 'w') as file:
    json.dump(example, file, indent=2)
