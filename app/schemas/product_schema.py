from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.models.product_model import ProductStatus

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0.0)
    stock: int = Field(..., ge=0)
    category: str = Field(..., min_length=1, max_length=50)
    status: ProductStatus = Field(default=ProductStatus.ACTIVE)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0.0)
    stock: Optional[int] = Field(None, ge=0)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    status: Optional[ProductStatus] = None

class ProductResponse(ProductBase):
    product_id: int
    created_at: datetime
    class Config:
        from_attributes = True
