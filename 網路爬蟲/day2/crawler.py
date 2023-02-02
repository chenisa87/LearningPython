import urllib.request as req
url = "https://www.hwsh.ylc.edu.tw/home"
# 建立一個 Request 物件 ， 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
import bs4 #載入 beautifulsoup4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("dd",field="2") #尋找 class = "nav-trigger hamburger"
for title in titles: #印出所有
    if title.a != None: #如果 html 的 .a 存在 就印出來
        print(title.a.string)   