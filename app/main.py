from fastapi import FastAPI
from .database import Base, engine
from .routers import employee, address

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee API")

app.include_router(employee.router)
app.include_router(address.router)
