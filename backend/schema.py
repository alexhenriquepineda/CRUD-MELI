from pydantic import BaseModel, PositiveFloat, EmailStr, validator
from enum import Enum
from datetime import datetime
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    email_supplier: EmailStr
    created_at: datetime

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_supplier: Optional[EmailStr] = None
    

