from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ---------- AUTH ----------

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_admin: bool

    class Config:
        orm_mode = True


# ---------- SERVICES ----------

class ServiceCreate(BaseModel):
    name: str
    description: str


class ServiceOut(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


# ---------- REQUESTS ----------

class RequestCreate(BaseModel):
    service_id: int
    phone: str
    comment: Optional[str] = None


class RequestOut(BaseModel):
    id: int
    status: str
    phone: str
    comment: Optional[str]
    created_at: datetime
    service: ServiceOut

    class Config:
        orm_mode = True
