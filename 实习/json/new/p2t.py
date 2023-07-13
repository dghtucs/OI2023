import os
from PyPDF2 import PdfReader

# PDF文件夹路径
pdf_folder = './2'

# TXT文件夹路径
txt_folder = './4'

# 遍历PDF文件夹中的所有文件
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # 构建PDF文件的完整路径
        pdf_path = os.path.join(pdf_folder, filename)

        # 打开PDF文件
        with open(pdf_path, 'rb') as file:
            # 创建PDF阅读器对象
            pdf_reader = PdfReader(file)

            # 读取所有页面的内容
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()

        # 构建TXT文件的完整路径
        txt_path = os.path.join(txt_folder, f'{os.path.splitext(filename)[0]}.txt')

        # 将文本内容写入TXT文件
        with open(txt_path, 'w', encoding='utf-8') as file:
            file.write(text)
