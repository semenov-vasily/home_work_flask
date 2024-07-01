import pydantic
from typing import Optional
from models import Session, User


# Проверка правильности заполнения полей таблицы User
class BaseUser(pydantic.BaseModel):
    name: str
    password: str

    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, value):
        if len(value) < 8:
            raise ValueError("password small")
        return value


# При создании пользователя
class UserCreate(BaseUser):
    pass


# При изменении пользователя
class UserUpdate(BaseUser):
    name: Optional[str]
    password: Optional[str]


# Проверка правильности заполнения полей таблицы Post
class BasePost(pydantic.BaseModel):
    heading: str
    description: str
    user_id: int

    @pydantic.field_validator("user_id")
    @classmethod
    def user_se(cls, value):
        with Session() as session:
            user = session.get(User, value)
            if user is None:
                raise ValueError("not user")
            return value


# При создании объявления
class CreatePost(BasePost):
    pass


# При изменении объявления
class UpdatePost(BasePost):
    heading: Optional[str]
    description: Optional[str]
    user_id: Optional[int]
