import requests
from bs4 import BeautifulSoup

# 发送HTTP GET请求
url = "http://www.baidu.com/"
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.content, "html.parser")



# 打印提取的数据
print(response.content())
