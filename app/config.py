from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DATABASE_URL: str

    BOT_TOKEN: str
    ADMIN_ID: int


    @model_validator(mode="before")
    def prepare(cls, values):
        values["DATABASE_URL"] = (f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}"
                                  f"@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}")
        return values

    class Config:
        env_file = '.env'


settings = Settings()
