from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Order Service")

# Tích hợp Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/order")
def create_order(item_id: int, quantity: int):
    return {"message": "Order created", "order": {"item_id": item_id, "quantity": quantity}}
