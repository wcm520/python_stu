import requests,json,re


def shop():
    url = 'https://you.163.com/item/detail?id=1177000&_stat_area=mod_14_item_1&_stat_id=1005002&_stat_referer=itemList'
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    # 字符串方法
    # da = res.text.split('"item":')[1].split('"commentCount"')[0].replace('"itemSizeTableFlag":false},','"itemSizeTableFlag":false}')
    # 正则
    da = re.findall('"item":(.*)},',res.text)
    data = da[0]+'}'
    info = json.loads(data)
    # print(info)
    name = info['name']
    desc = info['simpleDesc']
    price = info['retailPrice']
    img1 = info['itemDetail']['picUrl1']+'?type=webp&quality=95&imageView'
    img2 = info['itemDetail']['picUrl2'] + '?type=webp&quality=95&imageView'
    img3 = info['itemDetail']['picUrl3'] + '?type=webp&quality=95&imageView'
    img4 = info['itemDetail']['picUrl4'] + '?type=webp&quality=95&imageView'
    img5 = info['itemDetail']['picUrl5'] + '?type=webp&quality=95&imageView'
    d = {}
    d["name"] = name
    d["desc"] = desc
    d["price"] = price
    d["img1"] = img1
    d["img2"] = img2
    d["img3"] = img3
    d["img4"] = img4
    d["img5"] = img5
    print(d)

shop()