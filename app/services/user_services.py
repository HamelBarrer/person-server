from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..models import user_model
from ..schema import user_schema


def get_username_or_email(db: Session, access: str):
    user = db.query(user_model.User).filter(
        or_(user_model.User.username == access,
            user_model.User.email == access)
    ).first()

    return user


def read_user(db: Session, user_id: int):
    person = db.query(user_model.User).filter(
        user_model.User.user_id == user_id
    ).first()

    return person


def get_users(db: Session):
    users = db.query(user_model.User).all()

    return users


def insert_user(db: Session, user: user_schema.CreateUser):
    person = user_model.User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(person)
    db.commit()

    return person


def updated_user(db: Session, user: user_schema.UserBase, user_id: int):
    person = db.query(user_model.User).filter(
        user_model.User.user_id == user_id
    ).first()

    if not person:
        raise Exception('not found')

    person.username = user.username
    person.email = user.email
    person.is_active = user.is_active

    db.commit()

    return person
