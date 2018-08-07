#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
from base64 import encodestring


url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
req = Request(url)
encodeout = ''
b64str = encodestring(bytes('%s:%s' % ('user', 'password'), 'utf-8'))[:1]
hreq = req.add_header("Authorization", "Basic %s" % b64str)
f = urlopen(hreq)
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# req = Request(url, data={'user': 'user', 'password': 'password'}, headers=headers)
# f = urlopen(req)
print(f.readline())
f.close()


# from urllib.parse import urlparse
# from urllib.request import HTTPBasicAuthHandler, build_opener, install_opener
# from urllib.request import urlopen
#
#
# url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
# hdlr = HTTPBasicAuthHandler()
# hdlr.add_password('Secure Archive', urlparse(url)[1], 'user', 'password')
# opener = build_opener(hdlr)
# install_opener(opener)
# f = urlopen(url)
# out = open('out.html', 'w')
# for line in f.readlines():
#     out.write(line.decode('utf-8'))
#     print(line)
# f.close()
