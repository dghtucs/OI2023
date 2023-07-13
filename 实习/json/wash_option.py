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


    options = [content_b_c,content_c_d,content_d,content_a_b]

    # random.shuffle(options)

    pattern1 = r'A、(.*?)B、'
    pattern2 = r'B、(.*?)C、'
    pattern3 = r'C、(.*?)D、'
    pattern4 = r'D、(.*?)$'


    item['input'] = re.sub(pattern1, 'A、' + options[2] + 'B、', item['input'])
    print(item['input'])
    item['input'] = re.sub(pattern2, 'B、' + options[3] + 'C、', item['input'])
    print(item['input'])
    item['input'] = re.sub(pattern3, 'C、' + options[0] + 'D、', item['input'])
    print(item['input'])
    item['input'] = re.sub(pattern4, 'D、' + options[1] + ' ', item['input'])
    print(item['input'])




    ans = item['<ans>']
    replacement_map = {
        "A": "B",
        "B": "C",
        "C": "D",
        "D": "A"
    }
    ans = "".join(replacement_map.get(char, char) for char in ans)
    ans = ''.join(sorted(ans))
    item['<ans>'] = ans

with open('shuffled.json', 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
