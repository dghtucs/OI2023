import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
url = "https://www.cnss.com.cn/html/cbzsk/index_6.html"

def get_all_links(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    base_url = response.url
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
        elif href and href.startswith('http'):
            links.append(href)
    return links



all_links = get_all_links(url)


f = open("5.txt","a")
import sys
sys.stdout = f



for link in all_links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_p = soup.find_all('div',attrs={"id":"content"})
    for p in all_p:
        print(p)







