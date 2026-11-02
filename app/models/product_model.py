from datetime import datetime
from enum import Enum
from typing import Dict, Optional

class ProductStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class ProductItem:
    def __init__(self, product_id: int, name: str, price: float, stock: int, category: str, status: ProductStatus, description: Optional[str] = None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.status = status
        self.created_at = datetime.utcnow()

product_db: Dict[int, ProductItem] = {}
