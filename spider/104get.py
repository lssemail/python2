import urllib
import urllib2

values = {"username":"useranme", "password":"password"}
data = urllib.urlencode(values)
url = 'http://www.testlogin.login' + data
print(url)
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print(response.read())
