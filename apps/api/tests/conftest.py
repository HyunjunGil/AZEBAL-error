"""
Pytest configuration and fixtures for FastAPI testing
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def sample_product_id():
    """Sample product ID for testing"""
    return "tennis-racket-001"

@pytest.fixture
def sample_user_profile():
    """Sample user profile for testing recommendations"""
    return {
        "sport": "tennis",
        "style": "professional", 
        "budget": "medium"
    }

@pytest.fixture
def invalid_user_profile():
    """Invalid user profile for testing error cases"""
    return {
        "sport": "invalid_sport",
        "style": "invalid_style",
        "budget": "invalid_budget"
    }
