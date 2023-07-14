import json
import random

data = []
with open('code2name.json') as f:
    data += json.load(f)

with open('code2value.json') as f:
    data += json.load(f)

with open('name2code.json') as f:
    data += json.load(f)

with open('name2value.json') as f:
    data += json.load(f)

random.shuffle(data)

with open('shuffle.json','w') as f:
    json.dump(data,f,ensure_ascii=False, indent=4)
