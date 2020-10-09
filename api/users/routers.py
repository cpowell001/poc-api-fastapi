from fastapi import APIRouter, Depends
from typing import List
from api import models, schemas
from api.database import BaseRepository, Session, session_factory

router = APIRouter()


@router.get("/users/", response_model=List[schemas.UserRead])
def get_users():
    return [
        models.User(id=1, name="Chris 1", email="1@mail.com", address="4200 boul st laurent", role="admin"),
        models.User(id=2, name="Chris 2", email="2@mail.com", address="4200 boul st laurent", role="user", phone_number="5145555555")
    ]


@router.get("/users/current", response_model=schemas.UserRead)
def get_current_user():
    return models.User(id=1, name="Chris 1", email="1@mail.com", address="4200 boul st laurent", role="admin")


@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.User)
    return repo.create(**user.dict())
