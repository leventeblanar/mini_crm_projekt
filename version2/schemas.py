from pydantic import BaseModel, Field
from typing import Optional

    # basemodel for standard data format
class UserSchema(BaseModel):
    id: Optional[str] = Field(default = None)
    first_name: str
    last_name: str
    email: str
    phone: str
    
    class Config:
        orm_mode = True