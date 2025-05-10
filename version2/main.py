from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db_con import SessionLocal
from models import User as UserModel
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4
from schemas import UserSchema, UserCreate

app = FastAPI()

# temprary memory storage (instead of a database)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all the users
@app.get("/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

# Get user by id
@app.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create new user
@app.post("/users", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if not all([user.first_name, user.last_name, user.email, user.phone]):
        raise HTTPException(status_code=400, detail="Missing user data")
    
    if "@" not in user.email or "." not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email format" )
    
    db_user = UserModel(
        id=str(uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Update user by id
@app.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: str, updated_user: UserSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.first_name = updated_user.first_name
    user.last_name = updated_user.last_name
    user.email = updated_user.email
    user.phone = updated_user.phone
    
    db.commit()
    db.refresh(user)
    return user
    
# Delete user
@app.delete("/users/{user_id}", response_model=UserSchema)
def delete_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return user