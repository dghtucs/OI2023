import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
def extract_chinese_text(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    chinese_text = ""
    for tag in soup.find_all(text=re.compile(r'[\u4e00-\u9fff]')):
        chinese_text += tag.strip()
    return chinese_text

def crawl_website(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    baseurl = response.url
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):  # 只获取以http开头的链接
            href = urljoin(baseurl,href)
            links.append(href)
    chinese_text = extract_chinese_text(url)
    print(chinese_text)
    print(links)
    for link in links:
        chinese_text = extract_chinese_text(link)
        print(chinese_text)

# 使用示例
url = 'https://www.cmp1872.com/'  # 要爬取的网站地址
crawl_website(url)
