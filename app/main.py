from fastapi import FastAPI
from app.database import engine, Base
from app import models

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vibecheck", version="1.0.0")

@app.get("/")
async def home(): #function is able to handle requests and return responses
    return {"message": "Welcome to Vibecheck!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}