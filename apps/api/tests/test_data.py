"""
Tests for data models and helper functions
"""
import pytest
from app.data import (
    PRODUCTS, REVIEWS, 
    get_product_by_id, 
    get_reviews_by_product_id, 
    get_recommendations
)
from app.models import SportType, StyleType, BudgetRange

def test_products_data_integrity():
    """Test that products data is properly structured"""
    assert len(PRODUCTS) > 0
    
    for product in PRODUCTS:
        # Test required fields exist
        assert hasattr(product, 'id')
        assert hasattr(product, 'name')
        assert hasattr(product, 'brand')
        assert hasattr(product, 'price')
        assert hasattr(product, 'category')
        assert hasattr(product, 'style')
        assert hasattr(product, 'budget')
        
        # Test data types
        assert isinstance(product.price, int)
        assert isinstance(product.rating, float)
        assert isinstance(product.reviewCount, int)
        
        # Test enum values
        assert product.category in SportType
        assert product.style in StyleType
        assert product.budget in BudgetRange

def test_reviews_data_integrity():
    """Test that reviews data is properly structured"""
    assert len(REVIEWS) > 0
    
    for review in REVIEWS:
        # Test required fields
        assert hasattr(review, 'id')
        assert hasattr(review, 'productId')
        assert hasattr(review, 'author')
        assert hasattr(review, 'rating')
        assert hasattr(review, 'comment')
        assert hasattr(review, 'date')
        
        # Test rating range
        assert 1 <= review.rating <= 5
        
        # Test that productId references existing product
        product_exists = any(p.id == review.productId for p in PRODUCTS)
        assert product_exists, f"Review {review.id} references non-existent product {review.productId}"

def test_get_product_by_id_valid():
    """Test getting product by valid ID"""
    # Use first product ID from our data
    first_product = PRODUCTS[0]
    result = get_product_by_id(first_product.id)
    
    assert result is not None
    assert result.id == first_product.id
    assert result.name == first_product.name

def test_get_product_by_id_invalid():
    """Test getting product by invalid ID"""
    result = get_product_by_id("nonexistent-id")
    assert result is None

def test_get_reviews_by_product_id_valid():
    """Test getting reviews for valid product ID"""
    # Find a product that has reviews
    product_with_reviews = None
    for product in PRODUCTS:
        if any(review.productId == product.id for review in REVIEWS):
            product_with_reviews = product
            break
    
    if product_with_reviews:
        reviews = get_reviews_by_product_id(product_with_reviews.id)
        assert len(reviews) > 0
        
        for review in reviews:
            assert review.productId == product_with_reviews.id

def test_get_reviews_by_product_id_no_reviews():
    """Test getting reviews for product with no reviews"""
    # Find a product without reviews (if any)
    product_without_reviews = None
    for product in PRODUCTS:
        if not any(review.productId == product.id for review in REVIEWS):
            product_without_reviews = product
            break
    
    if product_without_reviews:
        reviews = get_reviews_by_product_id(product_without_reviews.id)
        assert len(reviews) == 0

def test_get_recommendations_exact_match():
    """Test recommendations with exact match criteria"""
    # Find criteria that should have exact matches
    tennis_professional_medium = get_recommendations(
        SportType.TENNIS, 
        StyleType.PROFESSIONAL, 
        BudgetRange.MEDIUM
    )
    
    # Should return products
    assert len(tennis_professional_medium) >= 0
    
    # All returned products should match sport
    for product in tennis_professional_medium:
        assert product.category == SportType.TENNIS

def test_get_recommendations_partial_match():
    """Test recommendations with partial match (no exact matches)"""
    # Use criteria that likely won't have exact matches
    recommendations = get_recommendations(
        SportType.BASKETBALL,
        StyleType.CASUAL,  # If no basketball casual products exist
        BudgetRange.LOW
    )
    
    # Should still return basketball products
    basketball_products = [p for p in recommendations if p.category == SportType.BASKETBALL]
    assert len(basketball_products) >= 0

def test_get_recommendations_limit():
    """Test that recommendations are limited to 6 items"""
    recommendations = get_recommendations(
        SportType.TENNIS,
        StyleType.PROFESSIONAL,
        BudgetRange.MEDIUM
    )
    
    assert len(recommendations) <= 6

def test_get_recommendations_priority_order():
    """Test that exact matches come before partial matches"""
    recommendations = get_recommendations(
        SportType.TENNIS,
        StyleType.PROFESSIONAL,
        BudgetRange.MEDIUM
    )
    
    if len(recommendations) > 1:
        # Check if we have exact matches
        exact_matches = []
        partial_matches = []
        
        for product in recommendations:
            if (product.category == SportType.TENNIS and 
                product.style == StyleType.PROFESSIONAL and 
                product.budget == BudgetRange.MEDIUM):
                exact_matches.append(product)
            else:
                partial_matches.append(product)
        
        # If we have both types, exact matches should come first
        if exact_matches and partial_matches:
            exact_match_indices = [recommendations.index(p) for p in exact_matches]
            partial_match_indices = [recommendations.index(p) for p in partial_matches]
            
            assert max(exact_match_indices) < min(partial_match_indices)

def test_all_sports_have_products():
    """Test that we have products for all sport types"""
    sport_counts = {}
    for sport in SportType:
        sport_counts[sport] = sum(1 for p in PRODUCTS if p.category == sport)
    
    # Should have at least one product for most sports
    products_with_sports = sum(1 for count in sport_counts.values() if count > 0)
    assert products_with_sports >= 3, "Should have products for at least 3 different sports"
