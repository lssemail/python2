import re

class Tool:
    # 替换掉img标签或7位长空格
    removeImg = re.compile('<img.*?>| {7}|&nbsp;')
    # 删除超连接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签替换位\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 把表格制表<td>替换为\t
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
