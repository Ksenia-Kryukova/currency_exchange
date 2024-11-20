from api.models.user import UserInDB
from pymongo import MongoClient
from core.config import settings


client = MongoClient(settings.ASYNC_DATABASE_URL)
db = client[settings.DB_NAME]
collection = db["users"]
# в реальной БД мы храним только ХЭШИ паролей + соль


def get_user_from_db(collection, username: str):
    '''
    Получение данных пользователя.
    '''
    user = collection.find_one({"username": {username}})
    if user:
        return UserInDB(**user)
    return None


def save_user(user: UserInDB):
    '''
    Сохранение пользователя в БД.
    '''
    collection.insert_one(**user.model_dump())
