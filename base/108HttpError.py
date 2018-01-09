import urllib2

request = urllib2.Request('http://www.xxxxx.com')

try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print(e.reason)
    print(e.code)