#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368\
     3.86 Safari/537.36"
}

url = r"http://www.00cha.com/tel.htm"
res = requests.get(url, headers=header)
# res.text获取网页后发现中文为乱码
# print(res.apparent_encoding)发现该网页编码格式为GB2312，于是先res.content获取源码再解码
response = res.content.decode("GB2312", "ignore")
print(response)

num_pat1 = r'<td width="20%" height="25"[\s\S]*?><a target=_blank href=[\s\S]*?>(.*?)</a>[\s\S]*?</td>'
orz_pat1 = r'<td width="33%"[\s\S]*?>(.*?)\s*?</td>'
num_pat2 = r'<td width="10%"><a target=_blank href=[\s\S]*?>(.*?)</a></td>[\s\S]*?<td width="35%">[\s\S]*?</td>'
orz_pat2 = r'<td width="10%"><a target=_blank href=[\s\S]*?>[\s\S]*?</a></td>[\s\S]*?<td width="35%">[\s\S]*?([\u4e00-\u9fa5]*?)\s*?</td>'


pat1 = re.compile(num_pat1)
pat2 = re.compile(orz_pat1)
pat3 = re.compile(num_pat2)
pat4 = re.compile(orz_pat2)

num1 = pat1.findall(response)
orz1 = pat2.findall(response)
num2 = pat3.findall(response)
orz2 = pat4.findall(response)
print(num1)
print(orz1)
print(num2)
print(orz2)

num_list = []
def numList(num, orz):
    for i in range(len(num)):
        num_list.append(orz[i]+num[i])
    print(num_list)

numList(num1, orz1)
numList(num2, orz2)




# <tr>
# 		<td width="20%" height="25"><a target=_blank href=http://www.00cha.com/p4008517517.html>4008517517</a>　</td>
# 		<td width="33%">麦当劳　</td>
# 		<td width="10%"><a target=_blank href=http://www.00cha.com/p4008823823.html>4008823823</a></td>
# 		<td width="35%">
# 	肯德基</td>
# </tr>

# <td width="20%" height="25" style="font-size: 14px"><a target=_blank href=[\s\S]*?>(.*?)</a>　</td>[\s\S]*?<td width="33%" style="font-size: 14px">[\s\S]*?　</td>
# <td width="20%" height="25" style="font-size: 14px"><a target=_blank href=[\s\S]*?>[\s\S]*?</a>　</td>[\s\S]*?<td width="33%" style="font-size: 14px">(.*?)　</td>
# <td width="20%" height="25" style="font-size: 14px"><a target=_blank href=[\s\S]*?>116114</a>　</td>[\s\S]*?<td width="33%" style="font-size: 14px">中国联通的“电话导航”业务　</td>
