from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ...schema import access_schema, user_schema
from ...services import user_services
from ...token import token
from ...utils import database_utils, hash_utils
from ...middleware.comprobation_token import get_current_user

router = APIRouter(
    prefix='/api/v1/users'
)


@router.post('/login')
async def login(access: access_schema.AccessBase, db: Session = Depends(database_utils.get_db)):
    user = user_services.get_username_or_email(db, access.username)

    is_valid = hash_utils.validation_hash(user.password, access.password)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User or password incorrect'
        )

    jwt = token.create_token(
        {'user_id': user.user_id}
    )

    return {'token': jwt}


@router.get('/{user_id}', response_model=user_schema.UserBase)
async def get_user(user_id: int, db: Session = Depends(database_utils.get_db)):
    user = user_services.read_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )

    return user


@router.get('/', response_model=list[user_schema.UserBase])
async def get_users(db: Session = Depends(database_utils.get_db), current_user: user_schema.UserBase = Depends(get_current_user)):
    return user_services.get_users(db)


@router.post('/')
async def create_user(user: user_schema.CreateUser, db: Session = Depends(database_utils.get_db)):
    if user.password != user.password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The passwords not equals'
        )

    user = user_services.insert_user(db, user)

    return user


@router.put('/{user_id}', response_model=user_schema.UserBase)
async def update_user(user_id: int, user: user_schema.UserBase, db: Session = Depends(database_utils.get_db)):
    try:
        person = user_services.updated_user(db, user, user_id)

        return person
    except Exception as ex:
        error = ex.__str__()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=error)
