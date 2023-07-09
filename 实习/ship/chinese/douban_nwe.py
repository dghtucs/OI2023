import requests
from bs4 import BeautifulSoup
import re #正则表达式

u = ["https://www.douban.com/doulist/124402609/",
     "https://www.douban.com/doulist/124402609/",
     "https://www.douban.com/doulist/124402609/"]

url = "https://www.douban.com/doulist/124402609/"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}




response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')
all_div = soup.findAll('div')
# print(all_div)

f = open("liukexin.txt","w")
import sys
sys.stdout = f

for i in all_div:
    cleaned_text = re.sub(r"[a-zA-Z]+|[^\u4e00-\u9fa5\s。，]+|\n\s*\n","",str(i))
    print(cleaned_text)








