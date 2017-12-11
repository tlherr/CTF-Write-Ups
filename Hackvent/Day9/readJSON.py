import json

raw = open('jsonion.json', 'r')

data = json.load(raw)

print(json.dumps(data))

for root in data:
    for (attribute, val) in root:
        print(attribute)
        print(val)


raw.close()
quit()