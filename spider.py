import requests
def main():
    url=input("输入网址链接:")
    UserAgent={"User-Agent":"Mozilla/5.0 (Linux; Android 9; PCAM10 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"}
    req=requests.get(utl=url,headers=UserAgent)
    req.encoding="utf-8"
    print(req.text)
if __name__=="__main__":
    main()

