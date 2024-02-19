import pytest
from fastapi.testclient import TestClient
from sqlalchemy_utils import create_database, database_exists

from app import app
from database import session, Base
from factories import CustomerFactory


class TestSettings:
    DATABASE_URL = 'postgresql://postgres:postgres@postgres:5432/db-test'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'postgres'
    POSTGRES_DB = 'db'


@pytest.fixture(scope='session')
def db(session_mocker):
    session_mocker.patch('database.Settings', return_value=TestSettings)
    db_session = session()
    engine = db_session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    CustomerFactory._meta.sqlalchemy_session = db_session
    return db_session


@pytest.fixture()
def cleanup_db(db):
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())


@pytest.fixture()
def app_client(cleanup_db):
    yield TestClient(app=app)


@pytest.fixture()
def customer():
    yield CustomerFactory()


@pytest.fixture()
def customer2():
    yield CustomerFactory()


@pytest.fixture()
def customer_body():
    return {
        "name": "Jane Doe",
        "address": "London",
        "age": 12,
        "description": "Lorem ipsum dolorem est",
    }
