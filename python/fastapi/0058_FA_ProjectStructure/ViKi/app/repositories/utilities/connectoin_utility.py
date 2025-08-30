
'''
Author: Vikash Kiran
Date: 2024-08-01 12:00:00
Last Modified by: Vikash Kiran
Last Modified at: 2024-08-01 12:00:00
Pen Name: ViKi Pedia
'''

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

def get_connection():
    # Example connection string for PostgreSQL
    DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/VikiHospitalBot"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()  # Return a new session instance