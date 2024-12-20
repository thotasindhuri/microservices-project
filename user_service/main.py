from fastapi import FastAPI
from app.routers.user_router import router as user_router

app = FastAPI()

# Include the user router
app.include_router(user_router)
