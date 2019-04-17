# 图片爬虫
import urllib
from urllib import request
from lxml import etree

class Spider(object):

    def __init__(self):
        self.tiebaName = "java"
        self.beginPage = 1
        self.endPage = 2
        self.url = "http://tieba.baidu.com/f?"
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.pageName = 1
        # self.fileName = r"F:\image\\"

    # 构造url
    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage+1):
            pn = (page-1)*50
            wo = {'pn':pn, 'kw':self.tiebaName}
            word = urllib.parse.urlencode(wo)
            my_url = self.url+word
            self.loadPage(my_url)
        print("下载完成！")

    # 获取页面内容，爬取页面对应帖子的href属性值，通过href属性值构造对应帖子详情页面url，即link
    def loadPage(self, url):
        req = request.Request(url, headers=self.ua_header)
        data = request.urlopen(req).read()
        # print(data)

        html = etree.HTML(data)
        links = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        # print(links)
        for link in links:
            link = "http://tieba.baidu.com"+link
            self.loadImages(link)

    # 爬取帖子详情，通过爬取src属性获取图片的链接image_link
    def loadImages(self, link):
        req = request.Request(link, headers=self.ua_header)
        result = request.urlopen(req).read()

        html = etree.HTML(result)
        links = html.xpath('//img[@class="BDE_Image"]/@src')
        # print(links)

        for image_link in links:
            self.writeImages(image_link)

    # 通过图片链接，爬取图片并保存图片到本地
    def writeImages(self, image):
        print("正在保存第%d张图片" % self.pageName)
        req = request.Request(image, headers=self.ua_header)
        data = request.urlopen(req).read()

        # 保存图片到本地
        with open(r"F:\image\\"+str(self.pageName)+".jpg", "wb") as f:
            f.write(data)
        # file = open(r"F:\image\\" + str(self.pageName) + ".jpg", "wb")
        # file.write(data)
        # file.close()

        self.pageName += 1

if __name__ == '__main__':
    my_spider = Spider()
    my_spider.tiebaSpider()

