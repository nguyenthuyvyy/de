from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Product Service")

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/product")
def add_product(name: str, price: float):
    return {"message": "Product added", "product": {"name": name, "price": price}}
