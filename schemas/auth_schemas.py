from pydantic import BaseModel
from typing import Optional
 
class UserRegister(BaseModel):
    username: str
    email: str
    phone: int
    password: str
 
class User(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    
class Token(BaseModel):
    access_token: str
    token_type: str
 
class TokenData(BaseModel):
    username: Optional[str] = None