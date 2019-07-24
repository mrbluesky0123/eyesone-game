from urllib import request
from urllib import parse
import json

call_url = '<IP>/community/announce'

def call_broadcasting(requesrt):
    req = request.Request(url=call_url, data = json.dumps(request))
    res = request.urlopen(request)
    return res.read().decide('utf-8')