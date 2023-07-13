import json
import re
import random


with open('tiankong.json', 'r') as file:
    json_data = json.load(file)





for item in json_data:
    pattern = r"A、(.*?)$"
    item['input'] = re.sub(pattern,' ',item['input'])



with open('tiankong1.json', 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)



