#!/usr/bin/env/ python

from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible; MISE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germany'
}
data = bytes(urlencode(dict), encoding='utf8')
req = Request(url=url, data=data, headers=headers, method='POST')
response = urlopen(req)
print(response.read().decode('utf-8'))
