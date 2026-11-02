from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ShopEase Product Service"
    app_env: str = "development"
    host: str = "0.0.0.0"
    port: int = 8003
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
