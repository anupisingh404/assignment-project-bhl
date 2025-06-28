import os
from dotenv import load_dotenv
from typing import Optional

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

class Settings:
    database_hostname    = os.getenv("DATABASE_HOSTNAME")
    database_port        = os.getenv("DATABASE_PORT")
    database_password    = os.getenv("DATABASE_PASSWORD")
    database_name        = os.getenv("DATABASE_NAME")
    database_username    = os.getenv("DATABASE_USERNAME")
    SQL_LOGGING          = os.getenv("SQL_LOGGING", "false")
    SECRET_KEY           = os.getenv("SECRET_KEY")
    
settings = Settings()