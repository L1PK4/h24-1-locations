from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    pass



def get_settings() -> Settings:
    return Settings()