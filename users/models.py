from sqlalchemy import Column,String,Integer,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class UserModel(Base):
    __tablename__   = 'Users'

    id              = Column(Integer,primary_key=True,index=True)
    username        = Column(String)
    email           = Column(String)
    full_name       = Column(String)
    disabled        = Column(Boolean)
    password        = Column(String)

class ProfileModel(Base):
    __tablename__   = 'Profile'

    id              = Column(Integer,primary_key=True,index=True)
    name            = Column(String)
    user_id         = Column(Integer,ForeignKey('Users.id'))
    photo_id        = Column(String)
    experience      = Column(String)
