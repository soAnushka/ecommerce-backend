from pydantic import BaseModel
from typing import Optional

# For request validation
class ProductCreate(BaseModel):
    name: str
    price: float
    size: Optional[str] = None

# For response formatting
def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "size": product["size"]
    }
