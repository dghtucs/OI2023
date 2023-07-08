import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
def get_all_chinese_words(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    text = soup.get_text()  # 获取网页中的纯文本内容
    chinese_words = re.findall(r'[\u4e00-\u9fff]+', text)  # 使用正则表达式匹配汉字
    return chinese_words

# 使用示例
url = 'https://www.cmp1872.com/'  # 要爬取的网站地址
all_chinese_words = get_all_chinese_words(url)
for word in all_chinese_words:
    print(word)
