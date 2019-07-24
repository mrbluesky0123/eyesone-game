import urllib2
import json

call_url = '<IP>/community/announce'

def call_broadcasting(requesrt):
    request = urllib2.Request(url=call_url, data = json.dumps(request))
    response = urllib2.urlopen(request)
    return response.read()