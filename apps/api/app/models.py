from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

# Enums for consistency
class SportType(str, Enum):
    TENNIS = "tennis"
    BADMINTON = "badminton"
    SOCCER = "soccer"
    BASKETBALL = "basketball"
    RUNNING = "running"

class StyleType(str, Enum):
    CASUAL = "casual"
    PROFESSIONAL = "professional"
    BEGINNER_FRIENDLY = "beginner_friendly"
    PERFORMANCE = "performance"

class BudgetRange(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Pydantic models for API responses
class Product(BaseModel):
    id: str
    name: str
    brand: str
    price: int
    imageUrl: str
    description: str
    category: SportType
    style: StyleType
    budget: BudgetRange
    rating: float
    reviewCount: int

class Review(BaseModel):
    id: str
    productId: str
    author: str
    rating: int
    comment: str
    videoUrl: Optional[str] = None
    date: str

class UserProfile(BaseModel):
    sport: SportType
    style: StyleType
    budget: BudgetRange

class RecommendationRequest(BaseModel):
    profile: UserProfile

class ProductDetail(BaseModel):
    product: Product
    reviews: List[Review]
