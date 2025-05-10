from pydantic import BaseModel, Field
from typing import Optional

    # basemodel for standard data format
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    
class UserSchema(UserCreate):
    id: Optional[str] = Field(default = None)
    
    class Config:
        orm_mode = True