import yaml
import redis
import os
import configwork
import json
from common import logger

logger = logger.get_standard_logger('rediscache')
session_prefix = 'game:session_id:'

def get_redis_config():
    # config = configwork.get_config()
    config = {'Redis': {'host':'198.13.47.188', 'port':9762, 'session-timeout':120}}
    return config['Redis']

def connect():
    redis_config = get_redis_config()
    try:
        connection = redis.Redis(host=redis_config['host'], port=int(redis_config['port']), db=0)
        connection.ping()
    except redis.exceptions.ConnectionError:
        logger.error('Connection failed')
        return None
    return connection

def check_connection(connection):
    try:
        connection.ping()
        return True
    except redis.exceptions.ConnectionError:
        logger.error('Ping failed')
        return False

def send_game_result(connection, game_result):
    # Health check
    if check_connection(connection) is False:
        return False
    # Get configs
    redis_config = get_redis_config()
    # Get key name for getting rank from config file
    set_rank_key = str(redis_config['set-key-name'])
    # Push game result
    result = connection.rpush(set_rank_key, str(game_result))
    # Check the result is true
    if result < 0:
        print('Failed to set')
        return False
    # Return result
    return True

def get_rank_data(connection, max_rank):
    # Health check
    if check_connection(connection) is False:
        return None
    # Get configs
    redis_config = get_redis_config()
    # Get key name for getting rank from config file
    get_rank_key = str(redis_config['get-key-name'])
    # Get rank data from redis
    rank_data = connection.lrange(get_rank_key, 0, max_rank)
    for i in range(0, max_rank):
        rank_data[i] = json.loads(rank_data[i])
    # Check data
    if rank_data is None:
        print('Rank data is null')
        return None
    else: 
        pass
    # Return data
    return rank_data

def get_session(connection, session_id):
    redis_config = get_redis_config()
    user_name = connection.get(session_prefix + session_id)
    
    if user_name is None:
        return None
    
    connection.expire(session_prefix + session_id, int(redis_config['session-timeout']))
    return user_name

def set_session(connection, session_id, user_name):
    redis_config = get_redis_config()
    try:
        connection.set(session_prefix + session_id, user_name)
        connection.expire(session_prefix + session_id, int(redis_config['session-timeout']))
    except Exception as e:
        logger.error(str(e))
        logger.error('Error ocurred on setting session')
        return False
    return True