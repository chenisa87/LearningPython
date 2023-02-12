URL = "http://ctf.scaict.org:8401/"

import requests

response = requests.get(URL)

try:
    html_content = response.text
    print(html_content)

except:
    print("錯誤")