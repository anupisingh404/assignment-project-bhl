from fastapi import FastAPI
from routes import user, data

app = FastAPI()

# Include routes
app.include_router(user.router)
app.include_router(data.router)

@app.get("/")
def root():
    return {"message": "Backend API is running"}


