"""
Tests for products API endpoints
"""
import pytest
from fastapi import status

def test_get_all_products(client):
    """Test getting all products"""
    response = client.get("/api/products")
    assert response.status_code == status.HTTP_200_OK
    
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0
    
    # Test product structure
    product = products[0]
    required_fields = ["id", "name", "brand", "price", "imageUrl", "description", 
                      "category", "style", "budget", "rating", "reviewCount"]
    for field in required_fields:
        assert field in product

def test_get_product_detail_valid_id(client, sample_product_id):
    """Test getting product detail with valid ID"""
    response = client.get(f"/api/products/{sample_product_id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert "product" in data
    assert "reviews" in data
    
    # Test product structure
    product = data["product"]
    assert product["id"] == sample_product_id
    assert "name" in product
    assert "brand" in product
    
    # Test reviews structure
    reviews = data["reviews"]
    assert isinstance(reviews, list)
    if reviews:  # If there are reviews
        review = reviews[0]
        required_review_fields = ["id", "productId", "author", "rating", "comment", "date"]
        for field in required_review_fields:
            assert field in review

def test_get_product_detail_invalid_id(client):
    """Test getting product detail with invalid ID"""
    response = client.get("/api/products/nonexistent-product")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    
    data = response.json()
    assert data["detail"] == "Product not found"

def test_product_data_validation(client):
    """Test that product data meets business requirements"""
    response = client.get("/api/products")
    products = response.json()
    
    for product in products:
        # Price should be positive
        assert product["price"] > 0
        
        # Rating should be between 0 and 5
        assert 0 <= product["rating"] <= 5
        
        # Review count should be non-negative
        assert product["reviewCount"] >= 0
        
        # Required string fields should not be empty
        assert len(product["name"]) > 0
        assert len(product["brand"]) > 0
        assert len(product["description"]) > 0
        
        # Category should be valid sport type
        valid_categories = ["tennis", "badminton", "soccer", "basketball", "running"]
        assert product["category"] in valid_categories
        
        # Style should be valid
        valid_styles = ["casual", "professional", "beginner_friendly", "performance"]
        assert product["style"] in valid_styles
        
        # Budget should be valid
        valid_budgets = ["low", "medium", "high"]
        assert product["budget"] in valid_budgets
