import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

# User
class Users(Base):
    __tablename__ = 'users'
    id: str = Column(Integer, primary_key=True, nullable=False)
    date_created: datetime = Column(DateTime, default=func.now(), nullable=False)
    first_name: str = Column(String(20), nullable=False)
    last_name: str = Column(String(20), nullable=False)
    email: str = Column(String(100), nullable=False, unique=True)
    bio: str = Column(String(100), nullable=True)
    hashed_password: str = Column(String, nullable=False)
    role: str = Column(String, nullable=False, server_default='user')
