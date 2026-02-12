from fastapi import FastAPI
from .database import Base, engine
from api.routes import auth, requests, services, users
from api import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoDonor API")

app.include_router(auth.router)
app.include_router(requests.router)
app.include_router(services.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"status": "API running"}


