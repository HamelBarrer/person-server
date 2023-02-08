from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int | None
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str
    password_confirm: str
