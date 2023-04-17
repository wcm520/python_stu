import requests
from lxml import html
import csv


with open("go2.csv", "a", newline='')as f:
    row = ['商品名', '商品价格', '介绍', '商品链接', '图片链接']
    write = csv.writer(f)
    write.writerow(row)
    for i in range(1, 7):
        url = f"http://www.go2.cn/search/all/page{i}.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot"
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=header)
        response.encoding = 'utf-8'
        page = html.etree.HTML(response.text)
        aa = page.xpath('//div[@class="search-result-list"]/ul[@class="clearfix"]/li')
        for bb in aa:
            name_a = bb.xpath('.//div[@class="pro-222-three-cont"]//div[@class="pro-name app-text-nowrap"]/text()')[0]
            jg = bb.xpath('.//div//span[@class="price"]/text()')[0]
            jj = bb.xpath('.//div[@class="pro-222-three-cont"]//div[@class="pro-info app-text-nowrap"]/text()')[0]
            lj_sp = bb.xpath('.//a[@class="img-wrap"]/@href')[0]
            lj_sp = f"http://www.go2.cn{lj_sp}"
            lj_img = bb.xpath('//a[@class="img-wrap"]/img/@src')[0]
            lj_img = f"http:{lj_img}"
            row1 = [name_a, jg, jj, lj_sp, lj_img]
            write.writerow(row1)
            # print(name_a, jg, jj, lj_sp, lj_img)

