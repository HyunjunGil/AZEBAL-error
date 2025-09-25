from fastapi import APIRouter
from typing import List
from app.models import Product, UserProfile, RecommendationRequest
from app.data import get_recommendations

router = APIRouter()

@router.post("/recommendations", response_model=List[Product])
async def get_product_recommendations(request: RecommendationRequest):
    """Get personalized product recommendations based on user profile"""
    profile = request.profile
    
    recommendations = get_recommendations(
        sport=profile.sport,
        style=profile.style,
        budget=profile.budget
    )
    
    return recommendations

@router.get("/recommendations/{sport}/{style}/{budget}", response_model=List[Product])
async def get_recommendations_by_params(sport: str, style: str, budget: str):
    """Get recommendations using URL parameters (alternative endpoint)"""
    try:
        # Convert string parameters to enum values
        from app.models import SportType, StyleType, BudgetRange
        
        sport_enum = SportType(sport)
        style_enum = StyleType(style)
        budget_enum = BudgetRange(budget)
        
        recommendations = get_recommendations(
            sport=sport_enum,
            style=style_enum,
            budget=budget_enum
        )
        
        return recommendations
        
    except ValueError as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=f"Invalid parameter value: {str(e)}")
