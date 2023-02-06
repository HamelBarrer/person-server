from fastapi import FastAPI

from .db import sqlite
from .models import base, user_model
from .routes.v1 import user_router

user_model.Base.metadata.create_all(bind=sqlite.connection_db())

app = FastAPI()

app.include_router(user_router.router)
