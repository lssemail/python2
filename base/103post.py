import urllib
import urllib2

values = {"username":"useranme", "password":"password"}
data = urllib.urlencode(values)
url = 'http://www.testlogin.login'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print(response.read())
