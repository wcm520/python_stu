import requests
from lxml import html
import json
url = 'https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1667282802437'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
a = response.text
b = json.loads(a)
c = b["data"]
e = c["cateList"]
for f in e:
    cate1 = f["name"]  # 一级类目
    for g in f["subCateGroupList"]:
        cate2 = g["name"]  # 二级类目
        for h in g["categoryList"]:
            cate3 = h["name"]
            print(cate1, cate2, cate3)



