import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("API_KEY")
database_key = os.environ.get("DATABASE_KEY")

print(api_key)
print(database_key)