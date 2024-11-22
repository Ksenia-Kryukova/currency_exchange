from api.models.user import UserInDB
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


client = AsyncIOMotorClient(settings.ASYNC_DATABASE_URL)
db = client[settings.DB_NAME]
collection = db["users"]


async def save_user(user: UserInDB):
    '''
    Сохранение пользователя в БД.
    '''
    await collection.insert_one(**user.model_dump())


async def get_user_from_db(collection, username: str):
    '''
    Получение данных пользователя.
    '''
    user = await collection.find_one({"username": {username}})
    if user:
        return UserInDB(**user)
    return None
