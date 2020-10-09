from fastapi import APIRouter, Depends
from typing import List
from api import models, schemas
from api.database import BaseRepository, Session, session_factory

router = APIRouter()


@router.get("/organizations/", response_model=List[schemas.OrganizationRead])
def get_users():
    return [
        models.Organization(id=1, name="Org 1", email="1@mail.com", address="4200 boul St Laurent"),
        models.Organization(id=2, name="Org 2", email="2@mail.com", address="4161 ave Esplanade", phone_number="5145555555")
    ]


@router.post("/organizations/", response_model=schemas.OrganizationRead)
def create_organization(organization: schemas.OrganizationCreate, session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.Organization)
    return repo.create(**organization.dict())
