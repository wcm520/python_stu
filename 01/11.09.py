import requests
import csv
import json

for i in range(1, 4):
    url = f'http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-11-09&ed=2022-11-09&es=0&qdii=&pi={i}&pn=50&dx=0&v=0.15464017506715888'
    header = {
        "Referer": "http://fund.eastmoney.com/data/diyfundranking.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    info = response.text
    data = info.split('datas:')[1].split(',allRecords')[0]
    # print(data)
    res = json.loads(data)
    print(res)
    with open('jijin.csv', 'a', newline="", encoding='utf-8-sig') as f:
        row = ['基金代码'	'基金简称'	'期间涨幅'	'期间分红' '分红次数' '起始日期' '单位净值' '累计净值' '终止日期' '单位净值' '累计净值' '成立日期' '手续费']
        write = csv.writer(f)
        write.writerow(row)
        for items in res:
            li = items.split(',')
            write.writerow(li)








    # info = info.replace('var rankData = {datas:["', "")
    # info = info.replace("};", "")
    # info = info.split('","')
    # with open('jijin.csv', 'a', newline="", encoding='utf-8-sig') as f:
    #     row = ['基金代码', '基金简称', '期间涨幅', '期间分红', '分红次数', '起始日期', '单位净值', '积累净值']
    #     # 写入
    #     write = csv.writer(f)
    #     write.writerow(row)
    #     for i in info:
    #         info1 = i.split(',')
    #         jjdm = info1[0]
    #         jjjc = info1[1]
    #         qjzf = info1[3]
    #         qjfh = info1[4]
    #         fhcs = info1[5]
    #         qsrq = info1[6]
    #         dwjz = info1[7]
    #         jljz = info1[8]
    #         row1 = [jjdm, jjjc, qjzf, qjfh, fhcs, qsrq, dwjz, jljz]
    #         write.writerow(row1)




