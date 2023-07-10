import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
url = "https://www.guanwuxiaoer.com/thread-1747-1-1.html"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
all_p = soup.find_all('td')
for p in all_p:
    print(p)






