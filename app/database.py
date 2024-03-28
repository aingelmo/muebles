from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from app.config import POSTGRES_SETTINGS

connection_string = URL.create(
    "postgresql",
    username=POSTGRES_SETTINGS.user,
    password=POSTGRES_SETTINGS.password,
    host=POSTGRES_SETTINGS.host,
    database=POSTGRES_SETTINGS.db_name,
)

engine = create_engine(
    connection_string,
    connect_args={"sslmode": "require"},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
