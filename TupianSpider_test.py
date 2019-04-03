#!/usr/bin/env python
# -*- coding:utf-8 -*-

from  urllib import request
import time

# http://588ku.com/image/qingmingjie.html
# http://588ku.com/sucai/0-default-0-0-qingmingjie-0-1/
#
# http://588ku.com/sucai/0-default-0-0-qingmingjie-0-2/
#
# http://588ku.com/sucai/0-default-0-0-qingmingjie-0-3/
#
# http://588ku.com/sucai/0-default-0-0-qingmingjie-0-4/

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko\
     ) Chrome/73.0.3683.86 Safari/537.36"
}

# 爬取页面
def loadPage(fullurl, filename):
    print("正在下载：", filename)
    req = request.Request(fullurl, headers=header)
    res = request.urlopen(req).read()
    return res

# 将爬取页面写入文件进行保存
def writePage(html, filename):
    print("正在保存：", filename)
    with open(filename, "wb") as f:
        f.write(html)
    print("--------------------------")

# 构造url，定义保存文件名
def tupianSpider(url, begin, end):
    for page in range(begin, end+1):
        fullurl = url + str(page)
        filename = "F:/spider_project第" + str(page) + "页.html"

        html = loadPage(fullurl, filename)
        writePage(html, filename)

    print("下载完成！")

if __name__ == '__main__':
    key = "http://588ku.com/sucai/"
    theme = input("请输入需要搜索的内容的拼音：")
    url = key + "0-default-0-0-" + theme + "-0-"
    begin = int(input("请输入需要下载的起始页："))
    end = int(input("请输入需要下载的结束页："))

    tupianSpider(url, begin, end)

    time.sleep(10)
