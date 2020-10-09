from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, nullable=False) # should be unique too?
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    users = relationship("User", back_populates="organization")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True) # should be unique too?
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    role = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    # hashed_password = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id")) # 1 to many?

    organization = relationship("Organization", back_populates="users")

class Roles:
    # at least 1 admin per organization is required
    ROLE_ADMIN = "admin"
    ROLE_USER = "user"