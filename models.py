from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    slots: int

class ClassOut(ClassBase):
    id: int
    available_slots: int

    class Config:
        orm_mode = True

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        orm_mode = True
