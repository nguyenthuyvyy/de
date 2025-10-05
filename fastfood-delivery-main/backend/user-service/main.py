from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="User Service")

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/user")
def create_user(username: str, email: str):
    return {"message": "User registered", "user": {"username": username, "email": email}}
