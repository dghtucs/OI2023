import os
from PyPDF2 import PdfReader

pdf_folder = './2'


txt_folder = './4'


for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):

        pdf_path = os.path.join(pdf_folder, filename)

        
        with open(pdf_path, 'rb') as file:

            pdf_reader = PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()

        txt_path = os.path.join(txt_folder, f'{os.path.splitext(filename)[0]}.txt')

        with open(txt_path, 'w', encoding='utf-8') as file:
            file.write(text)
