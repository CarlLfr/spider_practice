#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import request
import re
import json

def ydFanyi(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    formdata = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15541764499438",
        "sign": "70fe57ef928dbae3c72438b93a6581bf",
        "ts": "1554176449943",
        "bv": "6945a57e1923a3517303cdcdb2d3d15e",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        "typoResult": "false",
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    data = urllib.parse.urlencode(formdata).encode(encoding='utf-8')
    req = request.Request(url, data=data, headers=header)
    resp = request.urlopen(req).read().decode()

    # 正则表达式，提取"tgt": "和"}]]中间的任意内容
    # pat = r'"tgt": "(.*?)"}]]'
    # result = re.findall(pat, resp)

    # 将json格式转换为字典
    dic = json.loads(resp)
    res = dic["translateResult"][0][0]["tgt"]
    print(res)

if __name__ == '__main__':
    key = input("请输入需要翻译的词语或句子：")
    ydFanyi(key)