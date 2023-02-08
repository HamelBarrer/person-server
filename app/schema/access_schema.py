from pydantic import BaseModel


class AccessBase(BaseModel):
    username: str
    password: str
