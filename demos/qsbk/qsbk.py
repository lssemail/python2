# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.url = 'http://www.qiushibaike.com/hot/page/'
        self.stores = []

    def getPage(self, pageIndex):
        try:
            url = self.url + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            # 将页面转化为utf-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode;
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page loading error"
            return None

        pattern = re.compile('<h2>(.*?)</h2.*?content".*?span>(.*?)</span>.*?number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0], item[1], item[2]])

        return pageStories

    def loadPage(self):

        if self.enable == True:
            if len(self.stores) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stores.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self, pageStories, page):
        for item in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print "作者：", item[0]
            print "内容：", item[1]
            print "评论：", item[2]

    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stores)>0:
                pageStories = self.stores[0]
                nowPage +=1
                del self.stores[0]
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()