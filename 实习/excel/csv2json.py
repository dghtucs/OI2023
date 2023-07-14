import csv
import json
import random


codes = []
names = []
values = []


with open('code.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        codes.append(row[0])

with open('name.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        names.append(row[0])

with open('value.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        values.append(row[0])


# name2code
prompt1 = [
    '我的商品是',
    '商品名称是',
    '我有一件商品',
    '现有一商品，名称是',
    '这个商品名为'
]
prompt2 = [
    '请给出编码',
    '可以给我商品编码吗',
    '给出商品编码',
    '我需要这个商品的编码',
    '它的编码是？'
]
# code2name
prompt3 = [
    '我的商品编码是',
    '商品编码是',
    '我有一件商品的编码是',
    '现有一商品，编码是',
    '这个商品编码为'
]
prompt4 = [
    '请给出商品名称',
    '可以给我商品名称吗',
    '给出商品名称',
    '我需要这个商品的名称',
    '它的名称是？'
]

# code2value
prompt5 = [
    '我的商品编码是',
    '商品编码是',
    '我有一件商品的编码是',
    '现有一商品，编码是',
    '这个商品编码为'
]
prompt6 = [
    '请给出商品申报要素',
    '可以给我商品申报要素吗',
    '给出商品申报要素',
    '我需要这个商品的申报要素',
    '它的商品申报要素是？'
]

# name2value
prompt7 = [
    '我的商品是',
    '商品名称是',
    '我有一件商品',
    '现有一商品，名称是',
    '这个商品名为'
]
prompt8 = [
    '请给出商品申报要素',
    '可以给我商品申报要素吗',
    '给出商品申报要素',
    '我需要这个商品的申报要素',
    '它的商品申报要素是？'
]
json_data = []
for i in range(len(names)):
    item = {
        "input": prompt7[random.randint(0,4)] + names[i] + ',' +prompt8[random.randint(0,4)],
        "<ans>": values[i]
    }
    json_data.append(item)

with open('name2value.json', 'w',encoding='utf-8') as f:
    json.dump(json_data, f,ensure_ascii=False, indent=4)