from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# temprary memory storage (instead of a database)
users = []

# basemodel for standard data format
class User(BaseModel):
    id: Optional[str] = Field(default = None)
    first_name: str
    last_name: str
    email: str
    avatar: str

# Get all the users
@app.get("/users", response_model=List[User])
def get_users():
    return users

# Get user by id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if 0 <= user_id < len(users):
        return users[user_id]
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Create new user
@app.post("/users", response_model=User)
def create_user(user: User):
    if not all([user.first_name, user.last_name, user.email, user.avatar]):
        raise HTTPException(status_code=400, detail="Missing user data")
    
    if "@" not in user.email or "." not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email format" )
    
    user.id = str(uuid4())
    users.append(user)
    return user

# Update user by id
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    if 0 <= user_id <len(users):
        updated_user.id = users[user_id].id
        users[user_id] = updated_user
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id:int):
    if 0 <= user_id <len(users):
        deleted_user = users.pop(user_id)
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="User not found")