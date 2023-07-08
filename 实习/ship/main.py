import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
# 发送HTTP GET请求
u_energy = ["https://www.cmenergyshipping.com/index.php",
     "https://www.cmenergyshipping.com/page.php?p=profile",
     "https://www.cmenergyshipping.com/news.php?p=comnews",
     "https://www.cmenergyshipping.com/page.php?p=busoverview",
     "https://www.cmenergyshipping.com/page.php?p=contri"]

u_port=["https://www.cmp1872.com/",
   "https://www.cmp1872.com/about/groupInfo",
   "https://www.cmp1872.com/comBus/port",
   "https://www.cmp1872.com/investor/companyProfile",
   "https://www.cmp1872.com/sustainable/esgStrategy",
   "https://www.cmp1872.com/news/news",
   "https://www.cmp1872.com/hr/strategy",
   "https://www.cmp1872.com/contact/material"]

# u_port = ["https://www.cmp1872.com/"]

links = u_port
def get_urls(url):
    response = requests.get(url,headers=headers,timeout=10)
    soup = BeautifulSoup(response.text,"html.parser")
    base_url = response.url
    for link in soup.findAll('a'):
        href = link.get("href")
        if href and href.startswith('/'):
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
    return links

# for url in u_port:
#     all_links = get_urls(url)
#
# print(all_links)



with open('3.txt', 'a') as file:

    import sys
    sys.stdout = file
    for i in u_port:
        response = requests.get(i, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        all_p = soup.findAll('p')
        for j in all_p:
            if (j.string != None):
                print(j.string)


sys.stdout = sys.__stdout__













