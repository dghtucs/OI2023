import json
import re
import random


with open('resre_option_only.json', 'r') as file:
    json_data = json.load(file)


for item in json_data:



    match_a_b = re.search(r'A、(.*?)B、', item['input'])
    content_a_b = match_a_b.group(1)

    match_b_c = re.search(r'B、(.*?)C、', item['input'])
    content_b_c = match_b_c.group(1)

    match_c_d = re.search(r'C、(.*?)D、', item['input'])
    content_c_d = match_c_d.group(1)

    match_d = re.search(r'D、(.*?) ', item['input'])
    content_d = match_d.group(1)


    options = [content_a_b,content_b_c,content_c_d,content_d]






    ans = item['<ans>']
    replacement_map = {
        "A": content_a_b,
        "B": content_b_c,
        "C": content_c_d,
        "D": content_d
    }
    ans = "".join(replacement_map.get(char, char) for char in ans)

    item['<ans>'] = ans
    print(ans)

with open('tiankong.json', 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
