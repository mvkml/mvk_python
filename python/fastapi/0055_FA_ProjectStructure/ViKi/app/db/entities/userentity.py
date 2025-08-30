from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = "user"  # Matches the table name in PostgreSQL

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    fullname = Column(String, nullable=True)
    isactive = Column(Boolean, nullable=False, default=True, server_default="true")
    issuperuser = Column(Boolean, nullable=False, default=False, server_default="false")
    createddate = Column(DateTime(timezone=True), server_default=func.now())
    updateddate = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
