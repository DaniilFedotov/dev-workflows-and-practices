from fastapi import APIRouter

from app.schemas.customer import CustomerCreate, CustomerOut
from app.schemas.order import OrderCreate, OrderOut

router = APIRouter()

_CUSTOMERS: list[CustomerOut] = []
_ORDERS: list[OrderOut] = []


@router.post("/customers", response_model=CustomerOut)
def create_customer(payload: CustomerCreate) -> CustomerOut:
    customer = CustomerOut(id=len(_CUSTOMERS) + 1, **payload.model_dump())
    _CUSTOMERS.append(customer)
    return customer


@router.get("/customers", response_model=list[CustomerOut])
def list_customers() -> list[CustomerOut]:
    return _CUSTOMERS


@router.post("/orders", response_model=OrderOut)
def create_order(payload: OrderCreate) -> OrderOut:
    order = OrderOut(id=len(_ORDERS) + 1, **payload.model_dump())
    _ORDERS.append(order)
    return order


@router.get("/orders", response_model=list[OrderOut])
def list_orders() -> list[OrderOut]:
    return _ORDERS
