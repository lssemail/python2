# -*- coding: utf-8 -*-

import os
import re
import urllib
import urllib2


class TBMM:

    def __init__(self):
        self.baseUrl = 'https://mm.taobao.com/json/request_top_list.htm?page='
        # self.tool = tool.Tool()


    def getContent(self, currentPage):

        try:
            url = self.baseUrl + str(currentPage)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            content = response.read().decode('gbk')
            return content
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print e.reason
                return None


    def getItems(self, currentPage):
        content = self.getContent(currentPage)
        if not content:
            print "page loading error"
            return None
        pattern = re.compile('class="lady-avatar">(.*?)</a>.*?class="top".*?target="_blank">(.*?)</a>.*?<em><strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, content)
        contens = []
        for item in items:
            print item[0], item[1], item[2], item[3]
            # self.mkdir(item[1])
            # self.saveImg(item[0], item[1])

        return contens


    def getImgUrl(self, item):
        pattern = re.compile('src="(.*?)"')
        item = re.search(pattern, item)
        return item.group(1)

    def saveImg(self, imgUrl, fileName):

        url = self.getImgUrl(imgUrl)
        url = "https:" + url
        splitPath = url.split('.')
        fTail = splitPath.pop()
        fileName = fileName + "/icon." + fTail
        u = urllib.urlopen(url)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    def saveBrief(self, content, name):
        fileName = name + "/" + ".txt"
        f = open(fileName, "w+")
        print u"save her infomations", fileName
        f.write(content.decode('utf-8'))

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
            return True
        else:
            return False



tbmm = TBMM()
tbmm.getItems(1)