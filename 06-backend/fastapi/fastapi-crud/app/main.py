from fastapi import FastAPI
from app.database import engine, Base
from app.routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API CRUD com FastAPI",
    version="1.0.0"
)

app.include_router(items.router)