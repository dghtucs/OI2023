import re

# 读取文本文件内容
with open("1.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 使用正则表达式清洗文本数据
cleaned_text = re.sub(r"[a-zA-Z]+|[\u3000-\u303F\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65]|[^\u4e00-\u9fa5\s]+|\n\s*\n", "", text)

cleaned_text = re.sub(r"\n\s*\n","",cleaned_text)
cleaned_text = cleaned_text.replace('字段','')
cleaned_text = cleaned_text.replace('繁体','')

# 将清洗后的数据写入新的文本文件
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)
