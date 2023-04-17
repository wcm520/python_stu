import requests
from lxml import html
for i in range(1, 4):
    url = f'https://www.cnblogs.com/sitehome/p/{i}'
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    page = html.etree.HTML(response.text)
    aa = page.xpath('//div[@class="post-list"]/article')
    for bb in aa:
        a = bb.xpath('.//a[@class="post-item-title"]/text()')
        b = bb.xpath('.//a[@class="post-item-title"]/@href')
        print(a[0], b[0])
