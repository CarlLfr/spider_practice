#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

# 网易云音乐下载，输入歌名下载搜索页面排名第一的歌曲

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.3\
    6 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
# 获取搜索页面排名第一位的歌曲ID
def getMusicId(music_name):
    # 搜索页面url https://music.163.com/#/search/m/?s=歌名&type=1
    search_url = "https://music.163.com/#/search/m/"
    par = "s=" + music_name + "&type=1"
    html = requests.get(url=search_url, params=par, headers=header).text
    pat1 = 'href="/mv?id=(.*?)"'
    songIdList = re.findall(pat1, html)
    print(songIdList)


if __name__ == '__main__':
    music_name = input("请输入需要下载的歌曲名称：")
    getMusicId(music_name)
