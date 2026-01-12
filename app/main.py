from fastapi import FastAPI

app = FastAPI(title="Vibecheck", version="1.0.0")

@app.get("/")
async def home():
    return {"message": "Welcome to Vibecheck!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}