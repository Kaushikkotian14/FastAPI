from database import user_collection
 
def get_user_by_username(username: str):
    return user_collection.find_one({"username": username})

def get_user_by_phone(phone: int):
    return user_collection.find_one({"phone": phone})

def create_user(data: dict):
    return user_collection.insert_one(data)
 
def delete_user(username: str):
    return user_collection.delete_one({"username": username})