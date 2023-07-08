import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}

res = httpx.get(url='https://www.cmenergyshipping.com/index.php', headers=headers, timeout=10, verify=False)
print(res.text)
