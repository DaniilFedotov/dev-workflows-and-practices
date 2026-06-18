from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr


class CustomerOut(CustomerCreate):
    id: int
