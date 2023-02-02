import psycopg2 # pip3 install psycopg2
import urllib.request # pip3 install requests
from bs4 import BeautifulSoup  # pip3 install psycopg2

HOST = "localhost"
PORT = 5432
USER = "liyanxian"
PASSWD = ''
DATABASE = "postgres"
try:
    conn = psycopg2.connect(host=HOST, port=PORT, user=USER,password=PASSWD,
                            database=DATABASE)
    curr = conn.cursor()
    print('開始連接資料庫')
except:
    print('資料庫連接失敗')
    raise

url = "http://www.smeacommercialdistrict.tw/location/street"
# 發一個request去這串網址 並且拿回結果
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8-sig')

# 這邊參數很多可以選擇 不過基本上都在做同一件事情 (不過現在一般都推薦lxml 因為效能好)
soup = BeautifulSoup(text, "lxml")  # parse  (要先pip install lxml 不然會噴錯)

html_div = soup.find('div',class_="col-12")  #找到我們需要蒐集資料的外框 (find只會找第一個)

# 去外框裡面找到每一個(find_all)城市名稱
city_name = html_div.find_all(
    'h3', attrs={'class': 'county_title'})

#去外框裡面找到每一個(find_all)表格
table_content = html_div.find_all(
    'table', attrs={'class': 'table table-striped table-bordered table-sm contactxus_table'})

# range(len(xxx)) vs enumerate(xxx) 前者不可傳val 後者可傳 
for index in range(len(city_name)):
    # 找出表格裡所有的tr (select跟find_all功能其實一樣 只是語法不太一樣)
    table_tbody_tr = table_content[index].select(
        'tbody > tr')
    # 這邊在做資料庫的Insert 
    for index2, val2 in enumerate(table_tbody_tr):
        curr.execute("""INSERT IGNORE INTO `bussinessdistrict` 
			(`id`, `city`, `businessname`,`regio`, `businessarea`)
			 VALUES (%s,%s,%s,%s,%s)""",
                     (table_tbody_tr[index2].contents[1].contents[0], city_name[index].contents[0], table_tbody_tr[index2].contents[3].contents[0], table_tbody_tr[index2].contents[5].contents[0], table_tbody_tr[index2].contents[7].contents[0]))
        conn.commit()  # 確認送出(必要)
curr.close()        
conn.close()