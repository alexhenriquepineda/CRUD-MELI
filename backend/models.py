from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from database import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    category = Column(String, index=True)
    email_supplier = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
