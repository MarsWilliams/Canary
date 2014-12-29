from model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///ratings.db", echo=True)
Session = sessionmaker(bind=engine, autocommit = False, autoflush = False)

session = Session()

def createTables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    createTables()