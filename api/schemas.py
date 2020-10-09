from typing import Optional, List
from pydantic import BaseModel
from api.models import Roles

class OrganizationBase(BaseModel):
    email: str
    name: str
    address: str
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True


class OrganizationRead(OrganizationBase):
    id: int


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(OrganizationBase):
    pass


class UserBase(BaseModel):
    email: str
    name: str
    address: str
    role: str = Roles.ROLE_USER
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True


class UserRead(UserBase):
    id: int
    organization: OrganizationRead


class UserCreate(UserBase):
    organization_id: int


class UserUpdate(UserBase):
    pass
