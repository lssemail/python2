import urllib
import urllib2

url = 'http://www.testlogin.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {"username":"useranme", "password":"password"}
headers = {'User-Agent': user_agent, 'Referer':'http://www.baidu.com'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()