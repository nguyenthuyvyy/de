from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Payment Service")

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/payment")
def make_payment(order_id: int, amount: float):
    return {"message": "Payment processed", "payment": {"order_id": order_id, "amount": amount}}
