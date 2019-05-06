#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) App\
    leWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

# 获取首页url
def get_main_url(page):
    # http://www.bbsnet.com/doutu/page/2
    base_url_list = []
    for i in range(1, page+1):
        url = "http://www.bbsnet.com/doutu/page/{}".format(i)
        req = requests.get(url, headers=header)
        result = req.content

        soup = BeautifulSoup(result, "lxml")
        links = soup.select('ul[id="post_container"] li div[class="thumbnail"] a')
        for link in links:
            # 获取表情包地址
            base_url = link.get('href')
            base_url_list.append(base_url)

    return base_url_list

# 获取表情url
def download_imgs(base_url):
    src_url_list = []
    req = requests.get(url=base_url,headers=header).content
    soup = BeautifulSoup(req, "lxml")

    # 获取title
    title = soup.select('div[class="article_container row box"] h1')[0].get_text()

    # 获取url
    links = soup.select('div[id="post_content"] p img')
    for link in links:
        src_url = link.get('src')
        src_url_list.append(src_url)

    # 下载图片
    downloads(title, src_url_list)

# 新建文件夹
def make_dir(title):
    # dir_path = "F:/photo/" + title + "/"
    dir_path = "F:/photo/{}/".format(title)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

# 根据表情包title创建文件夹并下载图片
def downloads(title, url_list):
    # 新建文件夹
    filename = make_dir(title)
    j = 1

    for src_url in url_list:
        # filename = "%s/%s.jpg" % (file_name, str(j))
        print("正在下载......%s: NO.%s......" % (title, str(j)))
        with open(r"F:/photo/%s/%s.jpg" % (title, str(j)), "wb") as f:
            result = requests.get(url=src_url, headers=header).content
            f.write(result)
        j += 1
    print("==================")

def download_all_images(base_url_list):
    works = len(base_url_list)
    with ThreadPoolExecutor(works) as exector:
        for url in base_url_list:
            exector.submit(download_imgs, url)

if __name__ == '__main__':
    base_url_list = get_main_url(1)
    download_all_images(base_url_list)
    print("下载完成！")