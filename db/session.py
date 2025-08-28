from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from bot.config import settings


engine = create_engine(settings.DB_URL)
_session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

@contextmanager
def get_db():
    try:
        session: Session = _session()
        yield session
    finally:
        session.close()
