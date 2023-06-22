from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr

from src.database.models import Role


class ContactModel(BaseModel):
    first_name: str = Field('John', min_length=3, max_length=16)
    last_name: str = Field('Smith', min_length=3, max_length=16)
    phone_number: str = Field(min_length=10, max_length=12)
    birthday: date
    email: EmailStr
    additional_data: str


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: str = None

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=6, max_length=12)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: str
    roles: Role

    class Config:
        orm_mode = True


class TokeModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"