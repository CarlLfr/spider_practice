#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request
import urllib
import time

# 构造请求头信息
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko\
     ) Chrome/73.0.3683.86 Safari/537.36"
}

# url规律
# https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=0  第一页
# https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=50   第二页
# https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=100  第三页
# https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=150  第四页
# https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=200 第五页
# url = "https://tieba.baidu.com/f?kw=python%E7%88%AC%E8%99%AB&ie=utf-8&pn=" + str((n-1)*50)

def loadPage(fullurl, filename):
    print("正在下载：", filename)
    req = request.Request(fullurl, headers=header)
    res = request.urlopen(req).read()
    return res

def writePage(html, filename):
    print("正在保存：", filename)
    with open(filename, "wb") as f:
        f.write(html)

    print("------------------------")

# 构造url
def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage+1):
        pn = str((page-1)*50)
        fullurl = url+"&ie=utf-8&pn="+pn    #每次请求的完整的url
        filename = "F:/spider_project/第" + str(page) + "页.html" #每次请求后保存的文件名
        # filename = "c:/第" + str(page) + "页.html"

        html = loadPage(fullurl, filename)    #调用爬虫，爬去网页
        writePage(html, filename)   #把爬取到的网页写入本地

    print("下载完成！")

if __name__ == '__main__':
    kw = input("请输入贴吧名称：")
    beginPage = int(input("请输入需要下载的起始页："))
    endPage = int(input("请输入需要下载的结束页："))

    url = "https://tieba.baidu.com/f?"
    kws = urllib.parse.urlencode({"kw":kw})
    url = url + kws

    tiebaSpider(url, beginPage, endPage)

    time.sleep(10)
