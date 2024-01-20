from fastapi import Depends, FastAPI, HTTPException,Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from fastapi import Path

conn_str: str = (
    f"postgresql://Ch-Saqib:4H0iLkyNBpqu@ep-weathered-credit-48841962.us-east-2.aws.neon.tech/piaic?sslmode=require")

engine = create_engine(conn_str)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

class TodoCreate(BaseModel):
    name: str

class TodoResponse(BaseModel):
    id: int
    name: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()