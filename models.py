import datetime
from database import Base
from sqlalchemy import UUID, Column, Integer, String, DateTime, func

# User
class Users(Base):
    __tablename__ = 'users'
    id: str = Column(Integer, primary_key=True, nullable=False)
    date_created: datetime = Column(DateTime, default=func.now(), nullable=False)
    first_name: str = Column(String(20), nullable=False)
    last_name: str = Column(String(20), nullable=False)
    username: str = Column(String(50), nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    uuid: str = Column(UUID, nullable=False, unique=True)
    role: str = Column(String, nullable=False, server_default='user')
