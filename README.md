Microservices Demo Project

This project demonstrates a simple microservices-based architecture using FastAPI, Docker, and Python. The primary goal of the project is to showcase the design and implementation of independent microservices that interact through an API Gateway.

Table of Contents
- Features
- Technologies
- Architecture
- Getting Started
    -  Prerequisites
    -  Installation
    -  Running the Project
- Project Structure
- API Endpoints
- Testing

Features
- Microservices:
  - Product Service: Handles product-related data.
  - User Service: Manages user-related data.
- API Gateway:
  - Acts as a single entry point for all requests and routes them to the appropriate service.
- Dockerized:
  - Each service is containerized for easy deployment using Docker.
- Environment Variables:
  - Service URLs and configuration are managed through ".env" files for flexibility.
- Unit Testing:
  - Includes tests for key functionalities using "pytest".

---

Technologies Used
- Python: Primary programming language.
- FastAPI: Framework for building APIs quickly and efficiently.
- Docker & Docker Compose: For containerization and service orchestration.
- Uvicorn: ASGI server for serving FastAPI applications.
- Pytest: For testing.
- httpx: For asynchronous HTTP client requests.

Architecture
The project consists of three core components:
1. Product Service:
   - Handles all product-related operations.
   - Exposes an endpoint to fetch a list of products.

2. User Service:
   - Handles all user-related operations.
   - Exposes an endpoint to fetch a list of users.

3. API Gateway:
   - Acts as a central point of communication between clients and services.
   - Routes requests to the appropriate service.

---

 Getting Started

 Prerequisites
Ensure the following are installed on your system:
- Python 3.9+
- Docker & Docker Compose
- Git

 Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/microservices-project.git
   cd microservices-project
   

2. Create a virtual environment (if running locally):
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   

3. Install dependencies for each service:
   bash
   cd product_service
   pip install -r requirements.txt
   cd ../user_service
   pip install -r requirements.txt
   cd ../gateway
   pip install -r requirements.txt

---

 Running the Project

# Using Docker Compose
1. Ensure Docker is running.
2. Run the following command to build and start all services:
   bash
   docker-compose up --build
   
3. Access the services:
   - API Gateway: "http://127.0.0.1:8000"
   - Product Service: "http://127.0.0.1:8001/products"
   - User Service: "http://127.0.0.1:8002/users"

# Running Locally
1. Start each service individually using Uvicorn:
   bash
   # In product_service directory:
   uvicorn main:app --reload --port 8001

   # In user_service directory:
   uvicorn main:app --reload --port 8002

   # In gateway directory:
   uvicorn main:app --reload --port 8000
   
2. Access the endpoints as above.

---

 Project Structure
plaintext
e_commerce_project/
├── product_service/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI entry point
│   │   ├── models.py      # Pydantic models
│   │   ├── routers/
│   │   │   ├── product_router.py
│   ├── Dockerfile
│   ├── requirements.txt
├── user_service/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI entry point
│   │   ├── models.py      # Pydantic models
│   │   ├── routers/
│   │   │   ├── user_router.py
│   ├── Dockerfile
│   ├── requirements.txt
├── gateway/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI entry point
│   │   ├── routes.py
│   ├── Dockerfile
│   ├── requirements.txt
├── docker-compose.yml
├── README.md
└── .gitignore


---

 API Endpoints

 Gateway
- "GET /products": Fetches a list of products via the Product Service.
- "GET /users": Fetches a list of users via the User Service.

 Product Service
- "GET /products": Returns product details.

 User Service
- "GET /users": Returns user details.

---

 Testing
1. Install "pytest":
   bash
   pip install pytest
   
2. Run tests:
   bash
   pytest tests/
   
3. Example test file ("tests/test_gateway.py"):
   python
   import httpx

   def test_gateway_root():
       response = httpx.get("http://127.0.0.1:8000/")
       assert response.status_code == 200
       assert response.json() == {"message": "Gateway is running fine"}
   

---
