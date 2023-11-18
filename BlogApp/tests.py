from django.test import TestCase
from dotenv import load_dotenv
import os

load_dotenv()
# Create your tests here.
print(os.getenv("SECRET_SALT"))