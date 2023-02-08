from datetime import datetime, timedelta

from jose import JWTError, jwt

from .. import config


def create_token(data: dict):
    to_encode = data.copy()
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.utcnow() + access_token_expires

    to_encode.update({'exp': expire})

    token = jwt.encode(to_encode, config.SECRET_KEY,
                       algorithm=config.ALGORITHM)

    return token


def validation_token(token: str):
    validation = jwt.decode(
        token,
        config.SECRET_KEY,
        algorithms=[config.ALGORITHM]
    )

    return validation
