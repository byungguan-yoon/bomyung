from sqlalchemy.sql.schema import Column
from sqlalchemy import Column, Integer, String
from database import Base


class Stats(Base):
    __tablename__ = 'stats'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)