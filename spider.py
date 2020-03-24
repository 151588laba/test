import requests
url=input("输入网址链接:")
req=requests.get(url)
print(req.text)
