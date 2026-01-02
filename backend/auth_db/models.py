from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .base import Base


# SQLAlchemy DB Models
class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Pydantic models
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class MythologyRequest(BaseModel):
    prompt: str

class MythologyResponse(BaseModel):
    mythology: str