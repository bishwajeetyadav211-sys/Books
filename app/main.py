from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.address import Address
from app.routers.address_routes import router as address_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(address_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Address Book API. Go to /docs to test the endpoints."}
