from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import UserScore
from flask_sqlalchemy import SQLAlchemy
import app
import configwork
from common import logger

logger = logger.get_standard_logger('dbwork')

def get_db_config():
    # config = configwork.get_config()
    config = config = {'Database': {'host':'198.13.47.188', 'port':19762, 'username':'mrbluesky', 'password':'kang12!@'}}
    return config['Database']

def connect():
    # Get config
    db_config = get_db_config()
    host = db_config['host']
    port = int(db_config['port'])
    username = db_config['username']
    password = db_config['password']
    # Make session
    # engine = create_engine('mysql+mysqldb://%s:%s@%s:%d/score_system' % (username, password, host, port), convert_unicode=True)
    engine = create_engine('mysql+mysqldb://mrbluesky:kang12!@@198.13.47.188:19762/score_system', convert_unicode=True)
    Session = sessionmaker(autocommit=False, bind=engine)
    db_session = Session()
    return db_session

def close(db_session):
    # Close session
    db_session.close()

def insert_game_result(db_session, game_result):
    game_result = UserScore(user_name=game_result['user_name'], 
                            score=game_result['score'], 
                            clear_time=game_result['clear_time'],
                            session_id=game_result['session_id'],
                            reg_dt=datetime.now()
                        )
    try:                        
        db_session.add(game_result)
        db_session.commit()
    except Exception as eee:
        logger.error(str(eee))
        logger.error('Failed to save on DB')
        db_session.rollback()
        return False

    return True

def get_rank_data(db_session, max_rank):
    # Get ranked data from db

    raw_data = db_session.query(UserScore)\
        .order_by(desc(UserScore.score), desc(UserScore.clear_time))\
        .limit(max_rank).all()
    # Convert raw data to dict
    rank_data = []
    for i in range(0, len(raw_data)):
        rank_data.append(raw_data[i].as_dict())
    return rank_data

def get_user_score(db_session, session_id, user_name):
    # Get user score from db
    user_score = db_session.query(UserScore).filter(UserScore.session_id==session_id).one_or_none()
    # UserScore.query.filter_by(sessiod_id=session_id, user_name=user_name).first()
    if user_score is None:
        return None
    return user_score.as_dict()