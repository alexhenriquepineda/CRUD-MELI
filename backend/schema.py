# schema.py
from pydantic import BaseModel, PositiveFloat, EmailStr, Field
from datetime import datetime
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    email_supplier: EmailStr
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_supplier: Optional[EmailStr] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
