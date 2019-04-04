#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKi\
    t/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

# 获取热播榜网页url规律
# 第一页   http://www.htqyy.com/top/hot
# 第二页   http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 第三页   http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
# 第四页   http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20

# 获取热播榜网页信息
page = int(input("请输入需要下载的页数："))
songName = []
songId = []
for i in range(0, page):
    url1 = "http://www.htqyy.com/top/musicList/hot?pageIndex=" + str() + "1&pageSize=20"
    resp1 = requests.get(url1, headers=header).text

    # 获取歌曲名、id的正则表达式
    pat1 = r'title="(.*?)" sid="'
    pat2 = r'sid="(.*?)"'

    # 进行匹配
    namelist = re.findall(pat1, resp1)
    idlist = re.findall(pat2, resp1)

    # 将不同页面匹配到的结果整合到同一个list
    songName.extend(namelist)
    songId.extend(idlist)

# print(len(songName))
# print(len(songId))

# 好听轻音乐网热播榜歌曲url
# http://www.htqyy.com/play/33
# http://www.htqyy.com/play/62
# http://www.htqyy.com/play/58
# 歌曲播放url规律
# 第一首   http://f2.htqyy.com/play7/33/mp3/4
# 第二首   http://f2.htqyy.com/play7/62/mp3/4
# 第四首   http://f2.htqyy.com/play7/58/mp3/4

for j in range(0, len(songId)):
    url2 = "http://f2.htqyy.com/play7/" + str(songId[j]) + "/mp3/4"
    songname = songName[j]
    resp2 = requests.get(url2, headers=header).content

    print("正在下载第",j+1,"首")
    with open("F:\\music\\{}.mp3".format(songname), "wb") as f:
        f.write(resp2)

print("下载完成！")
