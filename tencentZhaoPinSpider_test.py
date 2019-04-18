#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import time
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

# 构造腾讯招聘网站url
# https://hr.tencent.com/position.php?keywords=&tid=0&start=0#a
# https://hr.tencent.com/position.php?keywords=&tid=0&start=10#a
# https://hr.tencent.com/position.php?keywords=&tid=0&start=20#a
def getMainUrl(beginPage, endPage):
    base_url = "https://hr.tencent.com/position.php?"
    for page in range(beginPage, endPage+1):
        start = str((page-1)*10) + "#a"
        parr = {"keywords": "", "tid": 0, "start": start}
        par_encode = urllib.parse.urlencode(parr)
        main_url = base_url + par_encode
        # get_urllib_request(main_url)
        getHtmlByWebDriver(main_url)

# 通过urllib.request发送请求（HTML加载不全面，缺少信息）
# def get_urllib_request(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
#          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368\
#          3.86 Safari/537.36"
#     }
#     req = request.Request(url, headers=header)
#     res = request.urlopen(req)
#     data = res.read().decode("utf-8")
#     print(data)

# 使用selenium获取网页信息
def getHtmlByWebDriver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    print(html)



if __name__ == '__main__':
    getMainUrl(1, 2)