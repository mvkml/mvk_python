from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

def get_db_session():
    # If your password is: Postgres@007  -> encode '@' as %40
    # postgres:Postgres%40007@localhost:5432/vikihospitalbot
    DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/vikihospitalbot"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return SessionLocal
