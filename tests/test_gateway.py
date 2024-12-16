import httpx

def test_gateway_root():
    response = httpx.get("http://127.0.0.1:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Gateway is running fine"}

def test_users_endpoint():
    response = httpx.get("http://127.0.0.1:8000/users")
    assert response.status_code == 200

def test_products_endpoint():
    response = httpx.get("http://127.0.0.1:8000/products")
    assert response.status_code == 200
