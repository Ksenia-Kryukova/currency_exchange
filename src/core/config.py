from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    API_KEY: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"mongodb://{self.DB_HOST}:{self.DB_PORT}/"

    @property
    def ASYNC_API_URL(self):
        return f"https://v6.exchangerate-api.com/v6/{self.API_KEY}/latest/"

    class Config:
        env_file = ".env"


settings = Settings()