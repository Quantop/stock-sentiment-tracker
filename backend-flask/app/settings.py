import os

from dotenv import dotenv_values, load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")