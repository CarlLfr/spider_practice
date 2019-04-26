#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from urllib.request import quote
from lxml import etree
import xlsxwriter
import threading
import queue

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

# 获取豆瓣书籍页面信息
# https://www.douban.com/tag/%E5%8E%86%E5%8F%B2/book?start=0
def bookRankPageInfo(book_tag):
    page_num = 0
    bookList = []

    url = "https://www.douban.com/tag/" + quote(book_tag) + "/book?start=" + str(page_num*15)
    req = requests.get(url, headers=header).text

    # 获取页面书籍所在的标签信息
    html = etree.HTML(req)
    book_list = html.xpath('//div/div[@class="mod book-list"]/dl')
    # book_name = book_list[0].xpath('dd/a/text()')
    for book_info in book_list:
        book_name = book_info.xpath('dd/a/text()')[0].strip()  #书名
        desc = book_info.xpath('dd/div[@class="desc"]/text()')[0].strip() #作者、译者、出版社、出版时间、价格
        desc_list = desc.split('/')
        book_rating_nums = book_info.xpath('dd/div[@class="rating"]/span[@class="rating_nums"]/text()')[0].strip() #评分
        book_detail_url = book_info.xpath('dd/a/@href')

        try:
            book_author_info = "作者/译者：" + "/".join(desc_list[:-3])
        except:
            book_author_info = "作者/译者：暂无"

        try:
            book_public_info = "出版信息：" + "/".join(desc_list[-3:])
        except:
            book_public_info = "出版信息：暂无"

        try:
            book_rating = book_rating_nums.strip()
        except:
            book_rating = "0.0"

        bookList.append([book_name, book_rating, book_author_info, book_public_info])

    return bookList


# 创建excel表格
def buildExcel(bookList):
    # 创建表格
    # workbook = xlsxwriter.Workbook(r"F:\doubanBook\{}.xlsx".format(book_tag))
    workbook = xlsxwriter.Workbook("F:\doubanBook\history.xlsx")
    worksheet = workbook.add_worksheet()

    for i in range(len(bookList)):
        worksheet.write("A"+str(1), bookList[i][0])
        worksheet.write("B"+str(2), bookList[i][1])
        worksheet.write("C"+str(3), bookList[i][2])
        worksheet.write("D"+str(4), bookList[i][3])

    workbook.close()



if __name__ == '__main__':
    bookList = bookRankPageInfo("历史")
    buildExcel(bookList)