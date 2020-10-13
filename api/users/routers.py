from fastapi import APIRouter, Depends
from typing import List
from api import models, schemas
from api.database import BaseRepository, Session, session_factory

router = APIRouter()


@router.get("/users/", response_model=List[schemas.UserRead])
def get_users(session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.User)
    return repo.get_all()


@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.User)
    return repo.create(**user.dict())
