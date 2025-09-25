from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Product, ProductDetail
from app.data import PRODUCTS, get_product_by_id, get_reviews_by_product_id

router = APIRouter()

@router.get("/products", response_model=List[Product])
async def get_all_products():
    """Get all available products"""
    return PRODUCTS

@router.get("/products/{product_id}", response_model=ProductDetail)
async def get_product_detail(product_id: str):
    """Get detailed information about a specific product including reviews"""
    product = get_product_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    reviews = get_reviews_by_product_id(product_id)
    
    return ProductDetail(product=product, reviews=reviews)
