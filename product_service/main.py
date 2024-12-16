from fastapi import FastAPI
from app.routers.product_router import router as product_router
app = FastAPI()
app.include_router(product_router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Service!"}

