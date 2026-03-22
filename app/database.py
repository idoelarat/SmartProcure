from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(),override=True)

def get_connection_string():
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    return f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(get_connection_string())
SessionLocal = sessionmaker(bind=engine)

if __name__ == '__main__': 
    try:
        with engine.connect() as conn:
            print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")