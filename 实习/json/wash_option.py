import json
import re
import random


with open('out5.json', 'r') as file:
    json_data = json.load(file)


for item in json_data:



    match_a_b = re.search(r'A、(.*?)B、', item['input'])
    if match_a_b:
        content_a_b = match_a_b.group(1)
    else:
        continue

    match_b_c = re.search(r'B、(.*?)C、', item['input'])
    if match_b_c:
        content_b_c = match_b_c.group(1)
    else:
        continue

    match_c_d = re.search(r'C、(.*?)D、', item['input'])
    if match_c_d:
        content_c_d = match_c_d.group(1)
    else:
        continue

    match_d = re.search(r'D、(.*?)$', item['input'])
    if match_d:
        content_d = match_d.group(1)
    else:
        continue


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

with open('s3.json', 'w') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
