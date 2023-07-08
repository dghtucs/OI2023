import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.douban.com/doulist/124402609/'
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')
all_p = soup.findAll('div',attrs={"class":"doulist-about"})

print(all_p)
for i in all_p:
    cleaned_text = re.sub(r"[a-zA-Z]+|[^\u4e00-\u9fa5\s。，\d]+|\n\s*\n", "", str(i))
    print(cleaned_text)









