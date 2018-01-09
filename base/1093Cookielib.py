# -*- coding: utf-8 -*-

import urllib2
import cookielib
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_expires=True, ignore_discard=True)

request = urllib2.Request('http://www.baidu.com')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)

print(response.read())
