#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import queue
import time
import requests
from lxml import etree

# https://www.qiushibaike.com/8hr/page/1/
# https://www.qiushibaike.com/8hr/page/2/

# 采集网页线程--爬取段子列表所在网页，放进列表
class Thread1(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # super(Thread1, self).__init__()
        threading.Thread.__init__(self)
        self.threadName = threadName    #线程名
        self.pageQueue = pageQueue  #页码队列
        self.dataQueue = dataQueue    #数据队列
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def run(self):
        print("启动线程"+self.threadName)
        while not flag1:
            try:
                page = self.pageQueue.get()
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                content = requests.get(url, headers=self.headers).text
                time.sleep(0.5)
                self.dataQueue.put(content)  #将数据放入数据队列
            except Exception as e:
                pass

        print("结束线程"+self.threadName)

class Thread2(threading.Thread):
    def __init__(self, threadName, fileName, dataQueue):
        # super(Thread2, self).__init__()
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.fileName = fileName
        self.dataQueue = dataQueue

    def run(self):
        print("启动线程", self.threadName)
        while not flag2:
            try:
                data = self.dataQueue.get()
                html = etree.HTML(data)
                result = html.xpath('//div/a[@class="recmd-content"]')
                for s in result:
                    data1 = s.text
                    self.fileName.write(data1+'\n'+"----------------------------"+'\n')
            except Exception as e:
                pass

        print("结束线程", self.threadName)

flag1 = False   #判断页码队列中是否为空
flag2 = False   #判断数据队列中是否为空

def main():
    # 页码队列
    pageQueue = queue.Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)
    #存放采集结果的数据队列
    dataQueue = queue.Queue()

    #保存到本地文件
    fileName = open(r"F:\spider_project\dianzi.txt", "a")

    #启动线程
    t1 = Thread1("采集线程", pageQueue, dataQueue)
    t1.start()
    t2 = Thread2("解析线程", fileName, dataQueue)
    t2.start()

    # 当pageQueue为空时，结束采集线程线程
    while not pageQueue.empty():
        pass
    global flag1
    flag1 = True

    # 当dataQueue为空时，结束解析线程
    while not dataQueue.empty():
        pass
    global flag2
    flag2 = True

    t1.join()
    t2.join()

    fileName.close()

    print("结束！")

if __name__ == '__main__':
    main()



