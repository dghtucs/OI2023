


with open('output.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 过滤掉以"prompt"开头的行
filtered_lines = [line for line in lines if not line.lstrip().startswith('"prompt"')]

# 将剩余的行写回文件中
with open('output1.json', 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)