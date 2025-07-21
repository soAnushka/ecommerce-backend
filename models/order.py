from pydantic import BaseModel
from typing import List
from datetime import datetime

# Pydantic model for request validation
class OrderCreate(BaseModel):
    user_id: str
    product_ids: List[str]  # list of product _id values

# Serializer for MongoDB document
def order_serializer(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "product_ids": order["product_ids"],
        "created_at": order["created_at"].isoformat() if order.get("created_at") else None
    }
