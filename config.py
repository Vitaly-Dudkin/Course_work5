import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")[::]
PORT = os.environ.get("PORT")[::]
DATABASE = os.environ.get("DATABASE")[::]
USE = os.environ.get("USE")[::]
PASSWORD = os.environ.get("PASSWORD")[::]
