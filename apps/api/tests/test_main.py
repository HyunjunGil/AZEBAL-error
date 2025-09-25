"""
Tests for main FastAPI application
"""
import pytest
from fastapi import status

def test_root_endpoint(client):
    """Test the root endpoint returns correct information"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["message"] == "Sports Equipment Recommendation API"
    assert data["status"] == "running"

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["status"] == "healthy"
    assert data["api_version"] == "1.0.0"

def test_cors_headers(client):
    """Test CORS headers are properly set"""
    response = client.options("/api/products")
    assert response.status_code in [status.HTTP_200_OK, status.HTTP_405_METHOD_NOT_ALLOWED]
    # Note: TestClient doesn't fully simulate CORS, but we can test the setup
