from typing import List, Optional
from fastapi import APIRouter, Query, status
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate):
    return ProductService.create(payload)

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
def list_products(category: Optional[str] = Query(None), skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    return ProductService.list(category, skip, limit)

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    return ProductService.get(product_id)

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, payload: ProductUpdate):
    return ProductService.update(product_id, payload)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    ProductService.delete(product_id)
    return None
