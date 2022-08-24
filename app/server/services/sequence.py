from sqlalchemy.orm import Session


from server.schemas import sequence as sequenceschema
from server.models import sequence as sequencemodel


def get_user(db: Session, user_id: int):
    return db.query(sequencemodel.User).filter(sequencemodel.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(sequencemodel.User).filter(sequencemodel.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sequencemodel.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: sequenceschema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = sequencemodel.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sequencemodel.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: sequenceschema.ItemCreate, user_id: int):
    db_item = sequencemodel.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
