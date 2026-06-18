from fastapi.testclient import TestClient

from app.main import app


def test_customers_and_orders_flow() -> None:
    client = TestClient(app)

    customer_payload = {"name": "Ada", "email": "ada@example.com"}
    customer_response = client.post("/api/v1/customers", json=customer_payload)
    assert customer_response.status_code == 200
    customer = customer_response.json()
    assert customer["id"] == 1

    order_payload = {"customer_id": str(customer["id"]), "amount": 42.0}
    order_response = client.post("/api/v1/orders", json=order_payload)
    assert order_response.status_code == 200
    order = order_response.json()
    assert order["id"] == 1

    listed_customers = client.get("/api/v1/customers")
    listed_orders = client.get("/api/v1/orders")
    assert listed_customers.status_code == 200
    assert listed_orders.status_code == 200
    assert len(listed_customers.json()) == 1
    assert len(listed_orders.json()) == 1
