#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
        html = getHtmlByWebDriver(main_url)
        getDetailUrl(html)

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
    driver = webdriver.PhantomJS()
    driver.get(url)
    try:
        WebDriverWait(driver, 10, 0.5).until(lambda driver: driver.find_element_by_link_text("全球招聘"))
        html = driver.page_source
        # print(html)
    finally:
        driver.close()

    return html

# 通过BeautifulSoup查找标签，获取对应岗位详情页面对应的url
def getDetailUrl(html):
    base_url = "https://hr.tencent.com/"
    soup = BeautifulSoup(html, 'lxml')
    # 获取td标签下面属性为target="_blank"的a标签列表
    s = soup.select('td a[target="_blank"]')
    for x in s:
        # 获取a标签的href属性值
        href = x.attrs["href"]
        # 对获取的href(href="position_detail.php?id=49582&amp;keywords=&amp;tid=0&amp;lid=0")进行切片
        # n = len("&amp;keywords=&amp;tid=0&amp;lid=0")
        # main_href = href[:-n]
        # 得到岗位详情页面对应的url
        my_url = base_url+href

        # 获取岗位详情页面信息
        html1 = getHtmlByWebDriver(my_url)
        job_name = jobName(html1)
        # job_site = jobSite(html1)
        # job_category = jobCategoryNum(html)[0]
        # job_num = jobCategoryNum(html)[1]
        job_response = jobResponse(html1)

        print("-----------------------------------------------------")
        print(job_name)
        # print(job_site)
        # print(job_category)
        # print(job_num)
        print(job_response)



# 获取工作岗位
def jobName(html):
    soup = BeautifulSoup(html, 'lxml')
    name_list = soup.select('tr td[id="sharetitle"]')
    job_name = name_list[0].get_text()
    return job_name

# 获取工作地点
# def jobSite(html):
#     soup = BeautifulSoup(html, 'lxml')
#     site_list = soup.select('td span[class="lightblue l2"]')
#     job_site = site_list[0].get_text()
#     return job_site

# 获取职位类别与招聘人数
# def jobCategoryNum(html):
#     soup = BeautifulSoup(html, 'lxml')
#     category_list = soup.select('td span[class="lightblue"]')
#     job_category = category_list[0].get_text()
#     job_num = category_list[1].get_text()
#     return job_category, job_num

# 获取工作职责与工作要求
def jobResponse(html):
    soup = BeautifulSoup(html, 'lxml')
    site_list = soup.select('ul[class="squareli"] li')
    text = ""
    for t in site_list:
        text += t.get_text()

    return text


if __name__ == '__main__':
    getMainUrl(1, 1)