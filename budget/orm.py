from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from budget.alchemy_fields import CIText

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres_test_data_types')
Base = declarative_base()
_SessionFactory = sessionmaker(bind=engine)

class users(Base):
    __tablename__ = 'budget_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    place = Column(String)

    def __init__(self, var1, var2):
        self.name = var1
        self.place = var2


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()