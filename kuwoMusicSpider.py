#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Apple\
    WebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

# 在酷我音乐榜单主页获取榜单名跟ID
def getBangInfo(name):
    url = "http://www.kuwo.cn/bang/index"
    resp = requests.get(url, headers=header).text

    # 正则表达式提取name和bangid
    pat1 = r'data-name="(.*?)" data-bangid="'
    pat2 = r'data-bangid="(.*?)">'
    namelist = re.findall(pat1, resp)
    bangIdList = re.findall(pat2, resp)

    # 根据输入的榜单name获取相应的bangId
    idx = namelist.index(name)
    bangId = bangIdList[idx]
    return bangId

# 通过获取榜单页面信息来获取歌曲id
def getSongId(name, bangId):
    # 请求对应榜单页面，如酷我热歌榜，获取该页面信息
    baseurl = "http://www.kuwo.cn/bang/content"
    par = {"name": name, "bangId": bangId}
    html = requests.get(url=baseurl, params=par, headers=header).text

    # 获取该榜单页面的歌曲id
    pat3 = '"id":"(.*?)","name"'
    pat4 = '"name":"(.*?)","artist"'
    songIdList = re.findall(pat3, html)
    songNameList = re.findall(pat4, html)
    return songIdList, songNameList

# 通过ant_url获取.aac文件的url,并下载.aac文件
def getSong(songIdList, songNameList):
    for i in range(0, len(songIdList)):
        # key = songKeyList[i][6:]  # 对id MUSIC_48742179切片取48742179
        key = songIdList[i]
        ant_url = "http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=" + key + "&type=convert_url&response=res"
        songName = songNameList[i]
        song_number = i + 1

        # 获取.acc文件url
        data = getAac(ant_url)
        saveSong(songName, song_number, data)

    print("下载完成！")


# 获取.aac文件url方法，再获取.acc文件
def getAac(url):
    resp3 = requests.get(url, headers=header, allow_redirects=False)
    aac_url = resp3.headers['Location']

    # 获取.acc文件
    acc_data = requests.get(url=aac_url,headers=header).content
    return acc_data

# 将歌曲写入文件
def saveSong(songName, songId, data):
    print("正在下载第",songId,"首")
    with open("F:\\music\\{}.mp3".format(songName), "wb") as f:
        f.write(data)

if __name__ == '__main__':
    name = input("请输入需要下载的榜单名称：")
    bang_id = getBangInfo(name)
    l = getSongId(name, bang_id)
    getSong(l[0], l[1])

