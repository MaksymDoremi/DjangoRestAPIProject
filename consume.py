import requests
from hashlib import sha256
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("SECRET_SALT"))

