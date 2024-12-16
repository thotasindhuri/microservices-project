from fastapi import APIRouter
from pydantic import BaseModel

# Create a router instance
router = APIRouter()

# Define a User model
class User(BaseModel):
    id: int
    name: str
    email: str

# Create a fake user database
fake_users = [{"id": 1, "name": "John Doe", "email": "john.doe@example.com"}]

# Define the route for fetching users
@router.get("/users")
def get_users():
    return fake_users
