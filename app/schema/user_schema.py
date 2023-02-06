from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool

    class Meta:
        orm_mode = True


class CreateUser(UserBase):
    password: str
    password_confirm: str
