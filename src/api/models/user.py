from pydantic import BaseModel


class Base(BaseModel):
    pass


class User(Base):
    username: str
    email: str
    password: str


class UserInDB(Base):
    username: str
    email: str
    hashed_password: str
