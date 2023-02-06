from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


def connection_db() -> Engine:
    return create_engine('sqlite:///./person.db')


def create_session():
    return sessionmaker(autoflush=False, bind=connection_db())
