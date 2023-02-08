import os

from dotenv import load_dotenv

load_dotenv()

# Config jwt
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
