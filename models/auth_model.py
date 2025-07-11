from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    phone: int
    hashed_password: str
    date: str
    time: str
   