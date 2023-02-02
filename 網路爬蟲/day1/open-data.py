import urllib.request as request 
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" #台大
with request.urlopen(src) as response:
    data = json.load(response) #抓取 json 

# 將公司名稱印出
clist = data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n") #字典 
