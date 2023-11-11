from dotenv import load_dotenv
import os

load_dotenv()

DB_ENGINE=os.environ.get("DB_ENGINE")
DB_NAME=os.environ.get("DB_NAME")
DB_USER = os.environ['DB_USER']
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_HOST=os.environ.get("DB_HOST")
FILE_CHARSET=os.environ.get("FILE_CHARSET")
LANGUAGE_CODE=os.environ.get("LANGUAGE_CODE")
TIME_ZONE=os.environ.get("TIME_ZONE")
AUTO_LOGOUT=int(os.environ.get("AUTO_LOGOUT"))
SECRET_KEY=os.environ.get("SECRET_KEY")
ALLOWED_HOSTS=os.environ.get("ALLOWED_HOSTS").split(",")