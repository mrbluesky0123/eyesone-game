from urllib import request
from urllib import parse
import json

call_url = 'http://eyesone-communication-serivce:8090/community/announce'

def call_broadcasting(request):
    message = make_message(request)
    req = request.Request(url=call_url, data = message)
    res = request.urlopen(request)
    return res.read().decide('utf-8')

def make_message(request):
    message = '!! %s is in the HALL OF FAME !!\n' % (request['user_name'])
    message += 'rankd : %s\n' % (request['rank'])
    message += 'score : %d\n' % (request['score'])
    message += 'clear time : %f\n' % (request['clear_time'])