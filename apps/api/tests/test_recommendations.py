"""
Tests for recommendations API endpoints
"""
import pytest
from fastapi import status

def test_get_recommendations_valid_profile(client, sample_user_profile):
    """Test getting recommendations with valid user profile"""
    response = client.post("/api/recommendations", json={"profile": sample_user_profile})
    assert response.status_code == status.HTTP_200_OK
    
    recommendations = response.json()
    assert isinstance(recommendations, list)
    assert len(recommendations) >= 0  # May be empty but should be valid
    
    # If recommendations exist, validate structure
    if recommendations:
        product = recommendations[0]
        required_fields = ["id", "name", "brand", "price", "category", "style", "budget"]
        for field in required_fields:
            assert field in product

def test_get_recommendations_invalid_profile(client, invalid_user_profile):
    """Test getting recommendations with invalid user profile"""
    response = client.post("/api/recommendations", json={"profile": invalid_user_profile})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_get_recommendations_missing_profile(client):
    """Test getting recommendations without profile data"""
    response = client.post("/api/recommendations", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_get_recommendations_by_params_valid(client):
    """Test getting recommendations using URL parameters"""
    response = client.get("/api/recommendations/tennis/professional/medium")
    assert response.status_code == status.HTTP_200_OK
    
    recommendations = response.json()
    assert isinstance(recommendations, list)
    
    # Validate that returned products match the criteria (if any)
    for product in recommendations:
        assert product["category"] == "tennis"
        # Should match either style or budget (based on our algorithm)
        assert product["style"] == "professional" or product["budget"] == "medium"

def test_get_recommendations_by_params_invalid_sport(client):
    """Test getting recommendations with invalid sport parameter"""
    response = client.get("/api/recommendations/invalid_sport/professional/medium")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_get_recommendations_by_params_invalid_style(client):
    """Test getting recommendations with invalid style parameter"""
    response = client.get("/api/recommendations/tennis/invalid_style/medium")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_get_recommendations_by_params_invalid_budget(client):
    """Test getting recommendations with invalid budget parameter"""
    response = client.get("/api/recommendations/tennis/professional/invalid_budget")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_recommendation_algorithm_logic(client):
    """Test the recommendation algorithm returns relevant products"""
    # Test tennis professional medium profile
    response = client.post("/api/recommendations", json={
        "profile": {
            "sport": "tennis",
            "style": "professional", 
            "budget": "medium"
        }
    })
    
    recommendations = response.json()
    
    # Should return tennis products
    tennis_products = [p for p in recommendations if p["category"] == "tennis"]
    assert len(tennis_products) > 0
    
    # Should prioritize exact matches (professional style + medium budget)
    exact_matches = [p for p in recommendations 
                    if p["category"] == "tennis" 
                    and p["style"] == "professional" 
                    and p["budget"] == "medium"]
    
    # If exact matches exist, they should be first in the list
    if exact_matches:
        assert recommendations[0] in exact_matches

def test_recommendation_different_sports(client):
    """Test recommendations for different sports return different products"""
    sports = ["tennis", "badminton", "running"]
    
    results = {}
    for sport in sports:
        response = client.post("/api/recommendations", json={
            "profile": {
                "sport": sport,
                "style": "casual",
                "budget": "medium"
            }
        })
        results[sport] = response.json()
    
    # Each sport should return products of that category
    for sport in sports:
        sport_products = [p for p in results[sport] if p["category"] == sport]
        assert len(sport_products) > 0, f"No products found for {sport}"

def test_recommendation_limit(client):
    """Test that recommendations are limited to reasonable number"""
    response = client.post("/api/recommendations", json={
        "profile": {
            "sport": "tennis",
            "style": "professional",
            "budget": "high"
        }
    })
    
    recommendations = response.json()
    # Should not return more than 6 products (as per business logic)
    assert len(recommendations) <= 6
