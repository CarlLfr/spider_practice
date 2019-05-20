#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36/DCLOUD-APP/2/1/3601234567891011121314151617181920212223242526272829303132333fafdsafdsa/",
    "X-Requested-With": "com.dcloud.DAKKALCGTK",
}
url = "http://www.fzdmpy.com"

html = requests.get(url, headers=headers).text
# print(html)
soup = BeautifulSoup(html, 'lxml')
links = soup.select('div[class="tab-content"] ul li a')
print(links)
for link in links:
    kouzi_url = link['href']
    kouzi_name = link.find('div', class_="title").text
    print(kouzi_url)
    print(kouzi_name)