from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...schema import user_schema
from ...services import user_services
from ...db import sqlite

router = APIRouter(
    prefix='/api/v1/users'
)


def get_db():
    db = sqlite.create_session()
    try:
        yield db()
    finally:
        db().close()


@router.post('/')
async def create_user(user: user_schema.CreateUser, db: Session = Depends(get_db)):
    user = user_services.insert_user(db, user)

    return user


@router.put('/{user_id}')
async def update_user(user_id: int, user: user_schema.UserBase, db: Session = Depends(get_db)):
    user_services.updated_user(db, user, user_id)
