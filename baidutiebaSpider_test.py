#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import parse
from urllib import request
from lxml import etree


class Spider(object):
    def __init__(self):
        self.tiebaName = "java"
        self.beginPage = 1
        self.endPage = 3
        self.url = "http://tieba.baidu.com/f?"
        self.ua_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.pageName = 1
        # self.fileName = r"F:\image"

    # 构造java页面url
    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50
            wo = {"kw": self.tiebaName, "pn": pn}
            word = parse.urlencode(wo)
            my_url = self.url + word
            self.loadPage(my_url)

    # 获取页面内容
    def loadPage(self, my_url):
        req = request.Request(my_url, headers=self.ua_header)
        result = request.urlopen(req).read().decode()

        html = etree.HTML(result)
        links = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        print(links)
        for link in links:
            link = self.url + link
            self.loadImage(link)

    # 爬取帖子详情，获取图片的链接
    def loadImage(self, link):
        req = request.Request(link, headers=self.ua_header)
        result = request.urlopen(req).read().decode()

        html = etree.HTML(result)
        links = html.xpath('//img[@class="BDE_Image"]/@src')
        print(links)

        for link in links:
            self.writeImages(link)

    # 通过图片所在链接，爬取图片并保存图片到本地
    def writeImages(self, link):
        print("正在保存第%d张图片" % self.pageName)
        req = request.Request(link, headers=self.ua_header)
        result = request.urlopen(req).read()

        with open(r"F:\image\\" + str(self.pageName) + ".jpg", "a") as f:
            f.write(result)

        self.pageName += 1


if __name__ == '__main__':
    my_spider = Spider()
    my_spider.tiebaSpider()






