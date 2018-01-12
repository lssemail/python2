# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import urllib2
import urllib

# url = 'https://tieba.baidu.com/p/2741534726'
# response = urllib2.urlopen(url)
# content = response.read().decode('utf-8')
# print(content)
file = open('tieba.html', 'r')
content = file.read()

pattern_title = re.compile('<h3 class="core_title_txt.*?">(.*?)</h3>', re.S)
result = re.search(pattern_title, content)
if result:
    print "title", result.group(1).strip()
else:
    print("None")

pattern_pages = re.compile('<span class="red">(.*?)</span>')
result = re.search(pattern_pages, content)
if result:
    print "pages", result.group(1).strip()
else:
    print("None")

pattern = re.compile("p_content.*?<cc>.*?>(.*?)</div>", re.S)
items = re.findall(pattern, content)
print(len(items))
for index, item in enumerate(items):
    print index,"content:",item.strip()
