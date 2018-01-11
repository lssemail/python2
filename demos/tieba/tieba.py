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

pattern = re.compile("p_content.*?<cc>.*?>(.*?)</div>", re.S)
items = re.findall(pattern, content)
print(len(items))
for index, item in enumerate(items):
    print index,"content:",item.strip()
