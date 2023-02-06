from fastapi import APIRouter, Depends, HTTPException, status
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


@router.get('/{user_id}', response_model=user_schema.UserBase)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_services.read_user(db, user_id)


@router.get('/', response_model=list[user_schema.UserBase])
async def get_users(db: Session = Depends(get_db)):
    return user_services.get_users(db)


@router.post('/')
async def create_user(user: user_schema.CreateUser, db: Session = Depends(get_db)):
    user = user_services.insert_user(db, user)

    return user


@router.put('/{user_id}', response_model=user_schema.UserBase)
async def update_user(user_id: int, user: user_schema.UserBase, db: Session = Depends(get_db)):
    try:
        person = user_services.updated_user(db, user, user_id)

        return person
    except Exception as ex:
        error = ex.__str__()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=error)
