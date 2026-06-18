from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    customer_id: str = Field(min_length=1)
    amount: float = Field(gt=0)


class OrderOut(OrderCreate):
    id: int
