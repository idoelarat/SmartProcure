# clean_db.py
from database import engine
from models import Base

def nuke_database():
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Database is now clean.")

if __name__ == "__main__":
    nuke_database()