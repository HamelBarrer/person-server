from sqlalchemy import insert
from sqlalchemy.orm import Session

from ..models import user_model
from ..schema import user_schema


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
    person = user_model.User.update().where(
        user_model.User.user_id == 1
    ).values(username=user.username)

    db.commit()

    return person
