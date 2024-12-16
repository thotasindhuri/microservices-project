import os
from fastapi import FastAPI
import httpx
import logging
logger = logging.getLogger("uvicorn")
app = FastAPI()

# Load environment variables
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product_service:8001")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user_service:8002")

@app.get("/")
async def root():
    return {"message": "Gateway is running fine"}

@app.get("/products")
async def get_products():
    logger.info("Received request for /products")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{PRODUCT_SERVICE_URL}/products")
            logger.info(f"Response from product_service: {response.status_code}, {response.text}")
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        logger.error(f"Error in /products: {exc}")
        return {"error": "Internal Server Errror"}

@app.get("/users")
async def get_users():
    logger.info("Received request for /users")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USER_SERVICE_URL}/users")
            logger.info(f"Response from user_service: {response.status_code}, {response.text}")
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        logger.error(f"Error in /users: {exc}")
        return {"error": "Internal Server Error"}
    
