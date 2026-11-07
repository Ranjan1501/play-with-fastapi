from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome from FastAPI!",
        "status": "success"
    }

# Define another GET endpoint.
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Ranjan",
        "status": "success"
    }


# With Query Parameters
@app.get("/user")
def get_user2(user_id: int):
    return {"id": user_id}

# With optional Query Parameters
@app.get("/users/")
def get_user3(limit : int = 10, active: bool = True):
    return {
        "limit": limit,
        "active": active
    }

# /users	limit=10, active=true
# /users?limit=20	limit=20, active=true
# /users?limit=20&active=false	limit=20, active=false

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    address: dict | None = None

# create user 
@app.post("/users")
def create_user(user: UserCreate):

    return {
        "message": "User created successfully",
        "user": user
    }

class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None

# update user 
@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    notify: bool = False,
    user: UserCreate = None
):
    return {
        "user_id": user_id,
        "notify": notify,
        "updated_user": user
    }

