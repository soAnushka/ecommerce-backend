from fastapi import APIRouter, Query, HTTPException
from db import product_collection
from models.product import product_serializer, ProductCreate
import re

router = APIRouter()

# ✅ POST /products – Create a new product
@router.post("/products", status_code=201)
def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = product_collection.insert_one(product_dict)
    created_product = product_collection.find_one({"_id": result.inserted_id})
    return product_serializer(created_product)

# ✅ GET /products – List and filter products
@router.get("/products", status_code=200)
def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    query = {}

    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}

    if size:
        query["size"] = size

    products_cursor = product_collection.find(query).skip(offset).limit(limit)
    products = [product_serializer(p) for p in products_cursor]

    return products
