from fastapi import APIRouter, HTTPException, Query
from models.order import OrderCreate, order_serializer
from db import order_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# POST /orders - Create a new order
@router.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    try:
        product_ids = [str(pid) for pid in order.product_ids]
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid product ID format")

    order_doc = {
        "user_id": order.user_id,
        "product_ids": product_ids,
        "created_at": datetime.utcnow()
    }

    result = order_collection.insert_one(order_doc)
    created_order = order_collection.find_one({"_id": result.inserted_id})

    return order_serializer(created_order)

# GET /orders?user_id=xyz - List orders for a user
@router.get("/orders", status_code=200)
def get_orders_for_user(
    user_id: str = Query(..., description="User ID to filter orders"),
    limit: int = Query(10),
    offset: int = Query(0)
):
    query = {"user_id": user_id}
    orders_cursor = order_collection.find(query).skip(offset).limit(limit)
    orders = [order_serializer(order) for order in orders_cursor]
    return orders
