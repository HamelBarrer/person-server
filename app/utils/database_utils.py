from ..db import sqlite


def get_db():
    db = sqlite.create_session()
    try:
        yield db()
    finally:
        db().close()
