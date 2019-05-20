#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36/DCLOUD-APP/2/1/3601234567891011121314151617181920212223242526272829303132333fafdsafdsa/",
    "X-Requested-With": "com.dcloud.DAKKALCGTK",
}
url = "http://www.fzdmpy.com/index/introduce?id=34"

html = requests.get(url, headers=headers).text
print(html)
url_pat = re.compile(r'<a href="(.*?)" target="_self"')
name_pat = re.compile(r'<a href=".*?" target="_self".*?">(.*?)</span></strong>|<a href=".*?" target="_self".*?><strong>(.*?)</strong></span>')
#
urls = url_pat.findall(html)
names = name_pat.findall(html)

for url in urls:
    print(url)
print(len(urls))
print(len(names))