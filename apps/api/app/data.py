# Mock data for the sports equipment recommendation API
# This matches the frontend mock data structure

from typing import List
from app.models import Product, Review, SportType, StyleType, BudgetRange

# Mock Products Data
PRODUCTS = [
    Product(
        id="tennis-racket-001",
        name="Wilson Pro Staff 97 v13",
        brand="Wilson",
        price=280000,
        imageUrl="https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?w=500",
        description="프로 선수들이 사용하는 고급 테니스 라켓으로, 정확한 컨트롤과 파워를 제공합니다.",
        category=SportType.TENNIS,
        style=StyleType.PROFESSIONAL,
        budget=BudgetRange.MEDIUM,
        rating=4.8,
        reviewCount=124
    ),
    Product(
        id="badminton-racket-001",
        name="Yonex Arcsaber 11",
        brand="Yonex",
        price=180000,
        imageUrl="https://images.unsplash.com/photo-1606843046906-8ffa84e7b222?w=500",
        description="초보자부터 중급자까지 사용하기 좋은 균형잡힌 배드민턴 라켓입니다.",
        category=SportType.BADMINTON,
        style=StyleType.BEGINNER_FRIENDLY,
        budget=BudgetRange.MEDIUM,
        rating=4.6,
        reviewCount=89
    ),
    Product(
        id="running-shoes-001",
        name="Nike Air Zoom Pegasus 40",
        brand="Nike",
        price=140000,
        imageUrl="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
        description="편안한 쿠셔닝과 반응성이 뛰어난 일상 러닝화입니다.",
        category=SportType.RUNNING,
        style=StyleType.CASUAL,
        budget=BudgetRange.MEDIUM,
        rating=4.7,
        reviewCount=256
    ),
    Product(
        id="tennis-racket-002",
        name="Babolat Pure Drive",
        brand="Babolat",
        price=220000,
        imageUrl="https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?w=500",
        description="파워풀한 샷을 원하는 플레이어에게 완벽한 테니스 라켓입니다.",
        category=SportType.TENNIS,
        style=StyleType.PERFORMANCE,
        budget=BudgetRange.MEDIUM,
        rating=4.5,
        reviewCount=98
    ),
    Product(
        id="soccer-cleats-001",
        name="Adidas Predator Edge",
        brand="Adidas",
        price=320000,
        imageUrl="https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=500",
        description="정확한 킥과 볼 컨트롤을 위한 프리미엄 축구화입니다.",
        category=SportType.SOCCER,
        style=StyleType.PROFESSIONAL,
        budget=BudgetRange.HIGH,
        rating=4.9,
        reviewCount=167
    ),
    Product(
        id="basketball-shoes-001",
        name="Jordan Air Max Impact 4",
        brand="Jordan",
        price=160000,
        imageUrl="https://images.unsplash.com/photo-1544966503-7cc5ac882d5e?w=500",
        description="농구 코트에서의 점프력과 안정성을 제공하는 농구화입니다.",
        category=SportType.BASKETBALL,
        style=StyleType.PERFORMANCE,
        budget=BudgetRange.MEDIUM,
        rating=4.4,
        reviewCount=78
    )
]

# Mock Reviews Data
REVIEWS = [
    Review(
        id="review-001",
        productId="tennis-racket-001",
        author="테니스초보",
        rating=5,
        comment="처음 테니스를 시작하는데 코치님이 추천해주셔서 구매했어요. 생각보다 무겁지 않고 컨트롤이 잘 되네요!",
        videoUrl=None,
        date="2025-09-15"
    ),
    Review(
        id="review-002",
        productId="tennis-racket-001",
        author="직장인테니스",
        rating=4,
        comment="회사 동호회에서 사용중인데 만족도가 높습니다. 가격대비 성능이 좋아요.",
        videoUrl=None,
        date="2025-09-10"
    ),
    Review(
        id="review-003",
        productId="badminton-racket-001",
        author="배드민턴러버",
        rating=5,
        comment="동호회 선배가 추천해줘서 샀는데 정말 좋네요. 스매시할 때 시원하게 날아가요!",
        videoUrl="https://sample-videos.com/sample-badminton-review.mp4",
        date="2025-09-12"
    ),
    Review(
        id="review-004",
        productId="running-shoes-001",
        author="마라토너",
        rating=5,
        comment="매일 5km씩 뛰는데 발이 전혀 아프지 않아요. 쿠셔닝이 정말 좋습니다.",
        videoUrl=None,
        date="2025-09-08"
    )
]

# Helper functions
def get_product_by_id(product_id: str) -> Product:
    """Get a product by its ID"""
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    return None

def get_reviews_by_product_id(product_id: str) -> List[Review]:
    """Get all reviews for a specific product"""
    return [review for review in REVIEWS if review.productId == product_id]

def get_recommendations(sport: SportType, style: StyleType, budget: BudgetRange) -> List[Product]:
    """Get product recommendations based on user profile"""
    recommendations = []
    
    # First, find exact matches (all criteria match)
    exact_matches = [
        product for product in PRODUCTS
        if product.category == sport and product.style == style and product.budget == budget
    ]
    recommendations.extend(exact_matches)
    
    # Then, find partial matches (sport + style OR sport + budget)
    if len(recommendations) < 6:  # If we need more recommendations
        partial_matches = [
            product for product in PRODUCTS
            if product.category == sport and (product.style == style or product.budget == budget)
            and product not in recommendations
        ]
        recommendations.extend(partial_matches)
    
    # Finally, add any remaining products from the same sport
    if len(recommendations) < 6:
        sport_matches = [
            product for product in PRODUCTS
            if product.category == sport and product not in recommendations
        ]
        recommendations.extend(sport_matches)
    
    # Limit to top 6 recommendations
    return recommendations[:6]
