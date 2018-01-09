# -*- coding: utf-8 -*-
import urllib
import urllib2

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
print(response.read())