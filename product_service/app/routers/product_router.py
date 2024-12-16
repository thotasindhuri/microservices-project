from fastapi import APIRouter
from app.models.product import Product

router = APIRouter()

fake_products = [{"id": 1, "name": "Sample Product", "price": 19.99, "in_stock": True},
    {"id": 2, "name": "Another Product", "price": 29.99, "in_stock": False}]

@router.post("/products")
def create_product(product: Product):
    fake_products.append(product)
    return product

@router.get("/products")
def list_products():
    return fake_products