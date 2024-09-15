from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    bio: Optional[str] = None

class UserCreate(UserBase):
    email: str
    password: str

class UserUpdate(UserBase):
    pass

