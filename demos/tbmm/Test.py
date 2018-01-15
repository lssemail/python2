import re

html = '<img src="//gtd.alicdn.com/sns_logo/i8/TB1bU.UFFXXXXc0XpXXSutbFXXX.jpg_60x60.jpg" alt="" width="60" height="60"/>'
pattern = re.compile('src="(.*?)"')
item = re.search(pattern, html)
print(item.group(1))