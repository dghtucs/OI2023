import json
import re
import random


with open('output5.json', 'r') as file:
    json_data = json.load(file)





for item in json_data:
    pattern = r"A."
    item['input'] = re.sub(pattern,' A、',item['input'])
    pattern = r"B."
    item['input'] = re.sub(pattern,' B、',item['input'])
    pattern = r"C."
    item['input'] = re.sub(pattern,' C、',item['input'])
    pattern = r"D."
    item['input'] = re.sub(pattern,' D、',item['input'])



with open('out5.json', 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)



