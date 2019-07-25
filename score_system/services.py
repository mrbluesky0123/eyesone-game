import rediscache
import configwork
import dbwork
from common import logger
import app
import uuid
import braodcasting


logger = logger.get_standard_logger('service')

def get_game_config():
    # config = configwork.get_config()
    config = {'Game': {'max-rank':5}}
    return config['Game']

def send_result_service(request):
    # Log request
    logger.info('Received request: ' + str(request)) 
    # Declare response
    response = {'response_code': None, 'response_msg': None, 'response_body': None}
    # Validate request
    # {"user_name" : string, "score": int, "clear_time": double}
    if (
        'user_name' not in request
        or 'score' not in request
        or 'clear_time' not in request
        or 'session_id' not in request
    ):
        app.logger.error('Invalid input values.')
        logger.error('Got invalid input values. ' + str(response))        
        response['response_code'] = '1101'
        response['response_msg'] = 'Invalid input values'
        return response
    
    ##### Send game result to redis or DB
    send_result = False
    db_session = dbwork.connect()
    send_result = dbwork.insert_game_result(db_session, request)
    
    # If it is failed to send result...
    if send_result is False:
        logger.error('Failed to send result to redis.')
        logger.error('Need to be implemented.')
        response['response_code'] = '2201'
        response['response_msg'] = 'Fail to insert result'
        return response
    
    dbwork.close(db_session)
    # Make response
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    return response

def get_rank_data_service(request):
    # Log request
    logger.info('Received request: ' + str(request)) 
    # Declare response
    response = {'response_code': None, 'response_msg': None, 'response_body': None}
    if (
        'user_name' not in request
        or 'score' not in request
        or 'clear_time' not in request
        or 'session_id' not in request
    ):
        app.logger.error('Invalid input values.')
        logger.error('Got invalid input values. ' + str(response))        
        response['response_code'] = '1101'
        response['response_msg'] = 'Invalid input values'
        return response
    ##### Get ranked data.
    # Get config for max rank
    game_config = get_game_config()
    max_rank = int(game_config['max-rank'])
    # Declare raw data
    raw_data = []
    db_session = dbwork.connect()
    raw_data = dbwork.get_rank_data(db_session, max_rank)
    # logger.info('Raw data from db' + str(raw_data))
    # Include requested data to raw data
    raw_data.append(request)
    # Get ranked data
    ranked_data = _get_ranked_data(raw_data, request, max_rank)
    # If rank is in max rank, push information
    '''
    for i in range(0, len(ranked_data)-1):
        if ranked_data[i]['requested'] is True:
            # logger.error(str(type(max_rank)))
            if int(ranked_data[i]['rank']) < int(max_rank):
                external.call_broadcasting(ranked_data[i])
    '''
    # Close db connection
    dbwork.close(db_session)
    # Make response
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    response['response_body'] = ranked_data
    logger.info('Response - ' + str(response))
    return response


def get_user_score_service(session_id, user_name):
    # Declare response
    response = {'response_code': None, 'response_msg': None, 'response_body': None}
    db_session = dbwork.connect()
    user_score = dbwork.get_user_score(db_session, session_id, user_name)
    # Close db connection
    dbwork.close(db_session)
    if user_score is None:
        response['response_code'] = '1102'
        response['response_msg'] = 'No user data'
        return response
    
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    response['response_body'] = user_score
    logger.info('Response - ' + str(response))
    return response

def check_restartable_service(session_id):
    # Declare response
    response = {'response_code': None, 'response_msg': None, 'response_body': None}
    # Connect to redis
    connection = rediscache.connect()
    # Check session
    user_name = rediscache.get_session(connection, session_id)
    if user_name is None:
        response['response_code'] = '2101'
        response['response_msg'] = 'Session expired!'
        return response
    
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    logger.info('Response - ' + str(response))
    return response

def register_user_service(request):
    user_id = request['user_name']
    session_prefix = 'game:session_id:'
    # Declare response
    response = {'response_code': None, 'response_msg': None, 'response_body': None}
    # Get session_id
    session_id = str(uuid.uuid4()) 
    # Connect to redis
    connection = rediscache.connect()
    set_result = rediscache.set_session(connection, session_id, user_id)
    
    if set_result is False:
        response['response_code'] = '2102'
        response['response_msg'] = 'Session setting error!'
        return response
    
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    response['response_body'] = session_id
    logger.info('Response - ' + str(response))
    return response
        
def _get_ranked_data(raw_data, request, max_rank):
    # Sort by score and clear_time 
    ranked_data = sorted(raw_data, key=lambda k:(int(k['score']), -float(k['clear_time'])), reverse=True)
    # Make data
    for i in range(0, max_rank+1):
        if(
            ranked_data[i]['user_name'] == request['user_name']
            and ranked_data[i]['score'] == request['score']
            and ranked_data[i]['clear_time'] == request['clear_time']
        ):
            ranked_data[i]['requested'] = True
        else:
            ranked_data[i]['requested'] = False
            
        if i == max_rank:
            ranked_data[i]['rank'] = str(i) + '+'
        else:
            ranked_data[i]['rank'] = str(i+1)

    return ranked_data

def test(request):
    db_session = dbwork.connect()
    dbwork.insert_game_result(db_session, request)
    # Close db connection
    dbwork.close(db_session)
    return "True"