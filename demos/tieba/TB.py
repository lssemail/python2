# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import urllib2
import urllib


class Tool:
    #替换掉img标签或7位长空格
    removeImg = re.compile('<img.*?>| {7}')
    #删除超连接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签替换位\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #把表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头替换位为\n加2空格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余的标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x, 0)
        x = re.sub(self.removeAddr, "", x, 0)
        x = re.sub(self.replaceLine, "\n", x, 0)
        x = re.sub(self.replaceTD, "\t", x, 0)
        x = re.sub(self.replacePara, "\n       ", x, 0)
        x = re.sub(self.replaceBR, "\n", x, 0)
        x = re.sub(self.removeExtraTag, "", x, 0)

        return x.strip()

class BDTB:

    def __init__(self, baseUrl, seeLZ, flootTag):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u"百度贴吧"
        #是否写入楼分隔符的标记
        self.floorTag = flootTag

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"链接百度贴吧失败", e.reason
                return None

    def getTitle(self, page):

        pattern = re.compile('<h3 class="core_title_txt.*?">(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page):

        pattern = re.compile('<span class="red">(.*?)</span>')
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getConent(self, page):
        pattern = re.compile("p_content.*?<cc>.*?>(.*?)</div>", re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):

        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")


    def writeData(self, contens):
        for item in contens:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"---------------"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):

        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已经失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getConent(page)
                self.writeData(contents)
        except IOError, e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"


print u"请输入帖子代号"
# 3138733512
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u"id\n"))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()