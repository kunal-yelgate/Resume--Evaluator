import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Missing DATABASE_URL. Set it in your .env file or environment.")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"ssl": {"ssl": True}},
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
