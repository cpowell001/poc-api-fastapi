from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://api:secret@localhost/fastapidb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def session_factory():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class BaseRepository:

    def __init__(self, session: Session, model: Base):
        # self.session_factory = session_factory
        self.session = session
        self.model = model


    # @property
    # def session(self):
    #     return self.session_factory()

    @property
    def query(self):
        return self.session.query(self.model)

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.query.offset(skip).limit(limit).all()

    def get(self, id):
        return self.query.get(id)

    def create(self, **kwargs):
        item = self.model(**kwargs)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item