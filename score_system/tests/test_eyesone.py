import pytest
import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

@pytest.fixture
def client():
    client = app.app.test_client()
    yield client

def test_send_result_success(client):
    request_data = {'user_name':'jyh', 'score':0, 'clear_time':1.21, 'session_id':'1wfvsawertaqqqqqqqqqwt23t2'}
    response_data = client.post('/score/sendresult', data=json.dumps(request_data))
    assert '0000' in (json.loads(response_data.data))['response_code']

def test_send_result_invalid_input(client):
    request_data = {'user_name':'jyh', 'score':0, 'clear_time': 1.21}
    response_data = client.post('/score/sendresult', data=json.dumps(request_data))
    assert '1101' in (json.loads(response_data.data))['response_code']

def test_get_rank_data_success(client):
    request_data = {'user_name':'jyh', 'score':0, 'clear_time':1.21, 'session_id':'1wfvsawertawt23t2'}
    response_data = client.post('/score/getrankdata', data=json.dumps(request_data))
    assert '0000' in (json.loads(response_data.data))['response_code']

def test_get_rank_data_invalid_input(client):
    request_data = {'user_name':'jyh', 'score':0, 'clear_time': 1.21}
    response_data = client.post('/score/getrankdata', data=json.dumps(request_data))
    assert '1101' in (json.loads(response_data.data))['response_code']
    
def test_register_user_success(client):
    request_data = {'user_name':'jyh'}
    response_data = client.post('/score/register_user', data=json.dumps(request_data))
    assert '0000' in (json.loads(response_data.data))['response_code']
    
def test_check_restartable_success(client):
    user_name = 'jyh'
    session_id = None
    prefix = 'game:session_id:'
    session_request_data = {'user_name':user_name}
    session_response_data = client.post('/score/register_user', data=json.dumps(session_request_data))
    session_response_dict = json.loads(session_response_data.data)
    session_id = session_response_dict['response_body']
    request_str = '/score/checkrestartable/%s' % (session_id)
    response_data = client.get(request_str)
    assert '0000' in (json.loads(response_data.data))['response_code']
    
def test_check_restartable_expired(client):
    request_str = '/score/checkrestartable/%s' % ('1234')
    response_data = client.get(request_str)
    assert '2101' in (json.loads(response_data.data))['response_code']

def test_get_user_score_success(client):
    request_str = '/score/getuserscore/%s/%s' % ('qwwwwww124weibrht', 'jyh')
    response_data = client.get(request_str)
    assert '0000' in (json.loads(response_data.data))['response_code']
    
def test_get_user_score_no_user_data(client):
    request_str = '/score/getuserscore/%s/%s' % ('1234', 'jyh')
    response_data = client.get(request_str)
    assert '1102' in (json.loads(response_data.data))['response_code']