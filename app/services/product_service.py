from typing import List, Optional
from fastapi import HTTPException, status
from app.models.product_model import product_db, ProductItem
from app.schemas.product_schema import ProductCreate, ProductUpdate

class ProductService:
    @staticmethod
    def _next_id() -> int:
        return max(product_db.keys(), default=0) + 1

    @classmethod
    def create(cls, data: ProductCreate) -> ProductItem:
        if not data.name.strip():
            raise HTTPException(status_code=422, detail="Name cannot be empty.")
        new_id = cls._next_id()
        p = ProductItem(new_id, data.name.strip(), data.price, data.stock, data.category.strip(), data.status, data.description)
        product_db[new_id] = p
        return p

    @staticmethod
    def list(category: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[ProductItem]:
        items = list(product_db.values())
        if category:
            items = [i for i in items if i.category.lower() == category.strip().lower()]
        return items[skip : skip + limit]

    @staticmethod
    def get(product_id: int) -> ProductItem:
        if product_id not in product_db:
            raise HTTPException(status_code=404, detail="Product not found.")
        return product_db[product_id]

    @staticmethod
    def update(product_id: int, data: ProductUpdate) -> ProductItem:
        if product_id not in product_db:
            raise HTTPException(status_code=404, detail="Product not found.")
        p = product_db[product_id]
        if data.name is not None:
            if not data.name.strip():
                raise HTTPException(status_code=422, detail="Name cannot be whitespace.")
            p.name = data.name.strip()
        if data.description is not None:
            p.description = data.description.strip() if data.description else None
        if data.price is not None:
            p.price = data.price
        if data.stock is not None:
            p.stock = data.stock
        if data.category is not None:
            p.category = data.category.strip()
        if data.status is not None:
            p.status = data.status
        return p

    @staticmethod
    def delete(product_id: int) -> None:
        if product_id not in product_db:
            raise HTTPException(status_code=404, detail="Product not found.")
        del product_db[product_id]
