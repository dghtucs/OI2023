import docx
import os

docs_folder = '.' # 当前文件夹

for filename in os.listdir(docs_folder):
    if filename.endswith('.doc'):
        doc = docx.Document(os.path.join(docs_folder, filename))
        txt_name = os.path.splitext(filename)[0] + '.txt'
        with open(txt_name, 'w') as txt_file:
            for para in doc.paragraphs:
                txt_file.write(para.text + '\n')
        print(f'{filename} converted to {txt_name}')