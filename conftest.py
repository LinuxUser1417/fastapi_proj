import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base
from settings import SQLALCHEMY_DATABASE_URL

@pytest.fixture(scope="module")
def TestSessionLocal():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal

@pytest.fixture(scope="function")
def db_session(TestSessionLocal):
    session = TestSessionLocal()
    yield session
    session.rollback()
    session.close()
