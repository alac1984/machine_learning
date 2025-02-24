import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    ENV: str = "development"
    DB: str

    def __init__(self, env: str = "development"):
        dotenv_path = f"04_euro_soccer/.env.{env}"
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path=dotenv_path, override=True)

        super().__init__()

        object.__setattr__(self, "ENV", env)

        if self.DB is None:
            raise Exception("Database not found")

