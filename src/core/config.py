from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"mongodb://{self.DB_HOST}:{self.DB_PORT}/"

    class Config:
        env_file = ".env"


settings = Settings()