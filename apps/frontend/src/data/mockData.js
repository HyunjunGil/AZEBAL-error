// Mock data for the sports equipment recommendation prototype

export const products = [
  {
    id: 'tennis-racket-001',
    name: 'Wilson Pro Staff 97 v13',
    brand: 'Wilson',
    price: 280000,
    imageUrl: 'https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?w=500',
    description: '프로 선수들이 사용하는 고급 테니스 라켓으로, 정확한 컨트롤과 파워를 제공합니다.',
    category: 'tennis',
    style: 'professional',
    budget: 'medium',
    rating: 4.8,
    reviewCount: 124
  },
  {
    id: 'badminton-racket-001', 
    name: 'Yonex Arcsaber 11',
    brand: 'Yonex',
    price: 180000,
    imageUrl: 'https://images.unsplash.com/photo-1606843046906-8ffa84e7b222?w=500',
    description: '초보자부터 중급자까지 사용하기 좋은 균형잡힌 배드민턴 라켓입니다.',
    category: 'badminton',
    style: 'beginner_friendly',
    budget: 'medium',
    rating: 4.6,
    reviewCount: 89
  },
  {
    id: 'running-shoes-001',
    name: 'Nike Air Zoom Pegasus 40',
    brand: 'Nike',
    price: 140000,
    imageUrl: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500',
    description: '편안한 쿠셔닝과 반응성이 뛰어난 일상 러닝화입니다.',
    category: 'running',
    style: 'casual',
    budget: 'medium',
    rating: 4.7,
    reviewCount: 256
  },
  {
    id: 'tennis-racket-002',
    name: 'Babolat Pure Drive',
    brand: 'Babolat',
    price: 220000,
    imageUrl: 'https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?w=500',
    description: '파워풀한 샷을 원하는 플레이어에게 완벽한 테니스 라켓입니다.',
    category: 'tennis',
    style: 'performance',
    budget: 'medium',
    rating: 4.5,
    reviewCount: 98
  },
  {
    id: 'soccer-cleats-001',
    name: 'Adidas Predator Edge',
    brand: 'Adidas',
    price: 320000,
    imageUrl: 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=500',
    description: '정확한 킥과 볼 컨트롤을 위한 프리미엄 축구화입니다.',
    category: 'soccer',
    style: 'professional',
    budget: 'high',
    rating: 4.9,
    reviewCount: 167
  },
  {
    id: 'basketball-shoes-001',
    name: 'Jordan Air Max Impact 4',
    brand: 'Jordan',
    price: 160000,
    imageUrl: 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5e?w=500',
    description: '농구 코트에서의 점프력과 안정성을 제공하는 농구화입니다.',
    category: 'basketball',
    style: 'performance',
    budget: 'medium',
    rating: 4.4,
    reviewCount: 78
  }
]

export const reviews = [
  {
    id: 'review-001',
    productId: 'tennis-racket-001',
    author: '테니스초보',
    rating: 5,
    comment: '처음 테니스를 시작하는데 코치님이 추천해주셔서 구매했어요. 생각보다 무겁지 않고 컨트롤이 잘 되네요!',
    videoUrl: null,
    date: '2025-09-15'
  },
  {
    id: 'review-002',
    productId: 'tennis-racket-001',
    author: '직장인테니스',
    rating: 4,
    comment: '회사 동호회에서 사용중인데 만족도가 높습니다. 가격대비 성능이 좋아요.',
    videoUrl: null,
    date: '2025-09-10'
  },
  {
    id: 'review-003',
    productId: 'badminton-racket-001',
    author: '배드민턴러버',
    rating: 5,
    comment: '동호회 선배가 추천해줘서 샀는데 정말 좋네요. 스매시할 때 시원하게 날아가요!',
    videoUrl: 'https://sample-videos.com/sample-badminton-review.mp4',
    date: '2025-09-12'
  },
  {
    id: 'review-004',
    productId: 'running-shoes-001',
    author: '마라토너',
    rating: 5,
    comment: '매일 5km씩 뛰는데 발이 전혀 아프지 않아요. 쿠셔닝이 정말 좋습니다.',
    videoUrl: null,
    date: '2025-09-08'
  }
]

export const userProfiles = [
  {
    sport: 'tennis',
    style: 'beginner_friendly',
    budget: 'medium',
    preferences: ['가벼운 무게', '컨트롤 중심', '브랜드 신뢰성']
  },
  {
    sport: 'badminton',
    style: 'casual',
    budget: 'low',
    preferences: ['가성비', '내구성', '색상']
  },
  {
    sport: 'running',
    style: 'performance',
    budget: 'high',
    preferences: ['쿠셔닝', '통기성', '디자인']
  }
]

// Helper function to get recommendations based on user profile
export function getRecommendations(profile) {
  return products.filter(product => {
    const matchesSport = product.category === profile.sport
    const matchesStyle = product.style === profile.style
    const matchesBudget = product.budget === profile.budget
    
    // Return products that match sport and either style or budget
    return matchesSport && (matchesStyle || matchesBudget)
  })
}

// Helper function to get reviews for a product
export function getProductReviews(productId) {
  return reviews.filter(review => review.productId === productId)
}
