import pandas as pd

# 读取Excel文件
df = pd.read_excel('1.xlsx',dtype={'code':str})

# 保存各列数据
for column in df.columns:
    column_data = df[column]
    print(column_data)
    column_data.to_csv(f'{column}.csv', index=False)
