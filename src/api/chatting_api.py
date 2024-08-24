from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import connect_database

chat_router = APIRouter(
    prefix = "/chat",
    tags = ["chatting"]
)