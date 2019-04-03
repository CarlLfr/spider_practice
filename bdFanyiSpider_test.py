#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import request
import json

# 百度翻译移动端爬虫
# content = input("请输入需要翻译的词语或句子：")
# url = "http://fanyi.baidu.com/basetrans"
# formdata = {
#     "from": "zh",
#     "to": "en",
#     "query": content,
#     "transtype": "realtime",
#     "simple_means_flag": "3",
#     "sign": "777849.998728",
#     "token": "10077a3659846c7bc0e31a9de9e59bb7",
# }
# header = {
#     "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/53\
#   7.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
# }
#
# data = urllib.parse.urlencode(formdata).encode(encoding="utf-8")
# req = request.Request(url, data=data, headers=header)
# resp = request.urlopen(req).read().decode()
# print(resp)


# 百度翻译web端爬虫（不可用）
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

def langdetect(content):
    lang_data = {"query": content}
    lan_data = urllib.parse.urlencode(lang_data).encode(encoding="utf-8")
    lang_url = "https://fanyi.baidu.com/langdetect"
    lang_req = request.Request(lang_url, data=lan_data, headers=header)
    lang_resp = request.urlopen(lang_req).read().decode()
    lan_dict = json.loads(lang_resp)
    lan = lan_dict["lan"]
    if lan == "zh":
        lan_to = "en"
    else:
        lan_to = "zh"
    return lan,lan_to

def v2transapi(content, lan, lan_to):
    transapi_data = {
    "from": lan,
    "to": lan_to,
    "query": content,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "115395.336370",
    "token": "10077a3659846c7bc0e31a9de9e59bb7"
    }
    trans_data = urllib.parse.urlencode(transapi_data).encode(encoding="utf-8")
    trans_url = "https://fanyi.baidu.com/v2transapi"
    trans_req = request.Request(trans_url, data=trans_data, headers=header)
    trans_resp = request.urlopen(trans_req).read().decode()
    print(trans_resp)

if __name__ == '__main__':
    content = input("请输入需要翻译的词语或句子：")
    lan = langdetect(content)[0]
    lan_to = langdetect(content)[1]
    v2transapi(content,lan, lan_to)
