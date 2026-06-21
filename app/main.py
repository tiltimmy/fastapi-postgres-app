from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API работает"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/sites")
def add_site(url: str):
    db = SessionLocal()
    new_site = Site(url=url)
    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    db.close()
    return {"id": new_site.id, "url": new_site.url}


@app.get("/sites")
def get_sites():
    db = SessionLocal()
    sites = db.query(Site).all()
    db.close()
    return sites