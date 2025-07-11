from repositories.auth_repository import get_user_by_phone, create_user, get_user_by_username
from utils.hashing import Hasher
from datetime import datetime
 
def register_user(user):
    if get_user_by_phone(user.phone):
        return {"error": "Phone number already registered"}

    data = {
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "hashed_password": Hasher.get_password_hash(user.password),
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
    }
    create_user(data)
    return {"msg": "User registered successfully"}
 
def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if user and Hasher.verify_password(password, user["hashed_password"]):
        return user
    return None
 