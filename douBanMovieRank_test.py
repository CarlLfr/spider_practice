#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request
import re

def getHtml(url, header):
    res = request.Request(url, headers=header)
    rep = request.urlopen(res).read().decode()
    return rep

def dealPat(patt, data):
    pat = re.compile(patt)
    result_list = pat.findall(data)
    return result_list


def combineList(list1, list2, list3):
    li = []
    for i in range(len(list1)):
        li.append(str(i+1)+"，"+list1[i]+"，"+list2[i]+"，评分"+list3[i])
    return li

def saveToFile(filename, li):
    with open(filename, "w") as f:
        for s in li:
            f.write(str(s)+'\n')
        f.close()
        print("保存成功！")

if __name__ == '__main__':
    filename = "F:\spider_project\doubanrank.txt"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    url = r"https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
    data = getHtml(url, header)
    # pat = r'"title":"(.*?)","url"|"regions":(.*?),"title"|"release_date":"(.*?)","actor_count"|"score":"(.*?)","actors"'
    name_pat = r'"title":"(.*?)","url"'
    regions_pat = r'"regions":(.*?),"title"'
    date_pat = r'"release_date":"(.*?)","actor_count"'
    score_pat = r'"score":"(.*?)","actors"'
    list1 = dealPat(name_pat, data)
    # list2 = dealPat(regions_pat, data)
    list3 = dealPat(date_pat, data)
    list4 = dealPat(score_pat, data)
    lii = combineList(list1, list3, list4)
    print(lii)
    saveToFile(filename, lii)