# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
try:
    # request = urllib2.Request(url, headers=headers)
    # response = urllib2.urlopen(request)
    # content = response.read().decode('utf-8')
    # print content
    file = open('qsbs.html', 'r')
    content = file.read()

    pattern1 = re.compile('h2>(.*?)</h2.*?content".*?span>(.*?)</.*?!--.*?-->(.*?)</.*?number">(.*?)</i>', re.S)
    # pattern2 = re.compile('<h2>(.*?)</h2>', re.S)
    # items = re.findall(pattern2, content)
    # for item in items:
    #     # print item[0], item[1], item[2], item[3]
    #     print item
    #     # print item[0]

    # pattern3 = re.compile('<span>(.*?)</.*?!--', re.S)
    # items = re.findall(pattern3, content)
    # for item in items:
    #     print item

    pattern4 = re.compile('<h2>(.*?)</h2.*?content".*?span>(.*?)</span>.*?number">(.*?)</i>', re.S)
    items = re.findall(pattern4, content)
    for item in items:
        print "作者：", item[0]
        print "内容：", item[1]
        print "评论：", item[2]

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason