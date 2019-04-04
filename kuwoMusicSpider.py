#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKi\
    t/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url = "http://www.kuwo.cn/bang/index"

# 各榜单请求url
# 酷我热歌榜 http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E7%83%AD%E6%AD%8C%E6%A6%9C&bangId=16
# 酷我新歌榜 http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E6%96%B0%E6%AD%8C%E6%A6%9C&bangId=17
# 酷我飙升榜 http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E9%A3%99%E5%8D%87%E6%A6%9C&bangId=93
resp = requests.get(url, headers=header).text
# print(resp)

# 正则表达式提取name和bangid
pat1 = r'data-name="(.*?)" data-bangid="'
pat2 = r'data-bangid="(.*?)">'
namelist = re.findall(pat1, resp)
bangIdList = re.findall(pat2, resp)

# 根据输入的榜单name获取相应的bangId
name = input("请输入需要下载的榜单名称：")
idx = namelist.index(name)
bangId = bangIdList[idx]

# print(len(namelist))
# print(len(bangIdList))

# 榜单url
baseurl = "http://www.kuwo.cn/bang/content"
par = {"name": name, "bangId": bangId}
html = requests.get(baseurl, params=par, headers=header).text
print(html)

# 榜单歌曲各自对应的url
# 一曲相思  http://www.kuwo.cn/yinyue/54761734?catalog=yueku2016
# 绿色    http://www.kuwo.cn/yinyue/63803414?catalog=yueku2016
# 生僻字   http://www.kuwo.cn/yinyue/37107986?catalog=yueku2016
# 狂浪  http://www.kuwo.cn/yinyue/58185350?catalog=yueku2016
# http://www.kuwo.cn/yinyue/歌曲id


# 获取歌曲id
pat3 = '"id":"(.*?)","name"'
pat4 = '"name":"(.*?)","artist"'
songKeyList = re.findall(pat3, html)
songNameList = re.findall(pat4, html)
print(len(songKeyList))
print(len(songNameList))
# for i in range(0, len(songKeyList)):
#     key = songKeyList[i][6:]  # 对id MUSIC_48742179切片取48742179
#     songName = songNameList[i]
#     songUrl = "http://www.kuwo.cn/yinyue/" + key
#     ct = {"catalog": "yueku2016"}
#     resp2 = requests.get(songUrl, headers=header, params=ct).content
#
#     print("正在下载第",i+1,"首")
#     with open("F:\\music\\{}.mp3".format(songName), "wb") as f:
#         f.write(resp2)
#
# print("下载完成！")