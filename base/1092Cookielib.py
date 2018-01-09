# -*- coding: utf-8 -*-

import urllib2
import cookielib
filename = 'cookie.txt'
#设置保存cookie的文件，
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)
