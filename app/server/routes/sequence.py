from msilib import sequence
from typing import List

from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session



from server.schemas import sequence as sequenceschema
from server.services import sequence as sequenceservice

from server.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=sequenceschema.User)
def create_user(user: sequenceschema.UserCreate, db: Session = Depends(get_db)):
    db_user = sequenceservice.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return sequenceservice.create_user(db=db, user=user)


@router.get("/users/", response_model=List[sequenceschema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = sequenceservice.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=sequenceschema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = sequenceservice.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=sequenceschema.Item)
def create_item_for_user(
    user_id: int, item: sequenceschema.ItemCreate, db: Session = Depends(get_db)
):
    return sequenceservice.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[sequenceschema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = sequenceservice.get_items(db, skip=skip, limit=limit)
    return items
