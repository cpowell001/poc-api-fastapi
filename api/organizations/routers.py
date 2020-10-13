from fastapi import APIRouter, Depends
from typing import List
from api import models, schemas
from api.database import BaseRepository, Session, session_factory

router = APIRouter()


@router.get("/organizations/", response_model=List[schemas.OrganizationRead])
def get_organizations(session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.Organization)
    return repo.get_all()


@router.post("/organizations/", response_model=schemas.OrganizationRead)
def create_organization(organization: schemas.OrganizationCreate,
                        session: Session = Depends(session_factory)):
    repo = BaseRepository(session=session, model=models.Organization)
    return repo.create(**organization.dict())
