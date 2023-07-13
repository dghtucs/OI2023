import json

# 打开输入文件
with open('exam.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化列表来保存所有的JSON对象
json_objects = []

# 初始化变量来保存当前问题的信息
question = ''
options = []
answer = ''
zhongjian = ''
input_content = ''
# 循环处理文件中的每一行
for line in lines:
    line = line.strip()

    if line.startswith('#'):
        input_content = line[1:]
        # 如果已经存在上一个问题的信息，则将其保存为JSON对象
        zhongjian = ''


        # 重置当前问题的信息
        question = line
        options = []
        answer = ''
        
    elif line.startswith('【羿文解析】'):
        # 提取选项
        pass
    elif line.startswith('参考答案：'):
        # 提取答案
        for char in line[2:8]:
            if char in ['A', 'B', 'C', 'D','对','错','a','b','c','d']:
                answer += char

        input_content += zhongjian
        if question != '':
            data = {
                "input": input_content,
                "<ans>": answer
            }
            json_objects.append(data)
    else:
        zhongjian += line




# 处理最后一个问题的信息
if question != '':
    data = {
        "input": input_content,
        "<ans>": answer
    }
    json_objects.append(data)

# 写入输出文件
with open('output3.json', 'w', encoding='utf-8') as file:
    json.dump(json_objects, file, ensure_ascii=False, indent=4)



