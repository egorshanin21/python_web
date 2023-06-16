from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr


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