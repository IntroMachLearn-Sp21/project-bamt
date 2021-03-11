import json
#How to load JSONS and access elements
data = open("tags.json")
data = json.load(data)
print(data['cGc0vDp2ZqApGOE1']['signTags'])