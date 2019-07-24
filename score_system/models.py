from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()

class UserScore(Base):
    __tablename__ = 'SCORE_MST'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = Column(String, primary_key=True)
    score = Column(Integer, primary_key=True)
    clear_time = Column(Float, primary_key=False)
    session_id = Column(String, primary_key=False)
    reg_dt = Column(DateTime, primary_key=False)

    def __init__(self, user_name, score, clear_time, session_id, reg_dt):
        self.user_name = user_name
        self.score = score
        self.clear_time = clear_time
        self.session_id = session_id
        self.reg_dt = reg_dt

    def __repr__(self):
        return 'user_name: %s, score: %d, clear_time: %f, session_id: %s, reg_dt: %s'\
                   % (self.user_name, self.score, self.clear_time, self.session_id, self.reg_dt)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}