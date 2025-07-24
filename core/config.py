from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Location Tracker API"
    DEBUG: bool = True

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }


settings = Settings()
