import os

# 源文件夹路径
source_folder = './4'

# 目标文件路径
output_file = 'all_all.txt'

# 打开目标文件，以追加模式写入
with open(output_file, 'a', encoding='utf-8') as output:
    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            # 构建源文件的完整路径
            source_file = os.path.join(source_folder, filename)

            # 打开源文件，读取内容
            with open(source_file, 'r', encoding='utf-8') as file:
                content = file.read()

            # 写入目标文件
            output.write(content)
            output.write('\n')  # 可选：在每个文件内容之间添加换行符
