import urllib.request as req
def getData(url):
    # 建立一個 Request 物件 ， 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1", #抓取 ptt 八卦版 裡面的東西
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4 #載入 beautifulsoup4 
    root = bs4.BeautifulSoup(data, "html.parser")
    #尋找 class = "nav-trigger hamburger"
    for title in root.find_all("div",class_="title"): #印出所有
        if title.a != None: #如果 html 的 .a 存在 就印出來
            if "陳時中" in title.a.string:
                print(title.a.string)   
    #尋找 nextlink 的網址
    nextlink = root.find("a",string="‹ 上頁")
    return nextlink["href"] # 找 href 屬性
pageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(3):
    pageUrl = "https://www.ptt.cc"+getData(pageUrl)
