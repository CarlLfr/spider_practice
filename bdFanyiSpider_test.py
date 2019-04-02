#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import request

context = input("请输入需要翻译的词语或句子：")
url = "http://fanyi.baidu.com/v2transapi/"
formdata = {
    "from": "zh",
    "to": "en",
    "query": context,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "777849.998728",
    "token": "10077a3659846c7bc0e31a9de9e59bb7",
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = urllib.parse.urlencode(formdata).encode(encoding="utf-8")
req = request.Request(url, data=data, headers=header)
resp = request.urlopen(req).read().decode()
print(resp)

