import re

# 读取文本文件内容
with open("3.txt", "r", encoding="utf-8") as file:
    text = file.read()


# cleaned_text = re.sub(r"[a-zA-Z]+|[\u3000-\u303F\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65]|[^\u4e00-\u9fa5\s]+|\n\s*\n", "", text)
# cleaned_text = re.sub(r"\n\s*\n","",cleaned_text)


import re

cleaned_text = re.sub(r"[a-zA-Z]+|[^\u4e00-\u9fa5\s。，\d]+|\n\s*\n", "", text)
cleaned_text = cleaned_text.replace('字段','')
cleaned_text = cleaned_text.replace(' ','')
cleaned_text = re.sub(r"\n\s*\n","",cleaned_text)


with open("output3.txt", "a", encoding="utf-8") as file:
    file.write(cleaned_text)
