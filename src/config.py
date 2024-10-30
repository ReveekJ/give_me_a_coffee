import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')

TOKEN_ADMIN = os.environ.get('TOKEN_ADMIN')
TOKEN_USER = os.environ.get('TOKEN_USER')