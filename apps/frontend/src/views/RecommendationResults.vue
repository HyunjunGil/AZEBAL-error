<template>
  <div class="min-h-screen bg-neutral-100 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="mb-8">
        <div class="text-center mb-6">
          <h1 class="text-3xl font-bold text-neutral-900 mb-2">
            맞춤 추천 결과
          </h1>
          <p class="text-neutral-600">
            {{ userProfile?.sport && getSportLabel(userProfile.sport) }} · 
            {{ userProfile?.style && getStyleLabel(userProfile.style) }} · 
            {{ userProfile?.budget && getBudgetLabel(userProfile.budget) }}
          </p>
        </div>
        
        <div class="flex justify-center">
          <router-link 
            to="/" 
            class="text-primary hover:text-blue-600 transition-colors"
          >
            ← 다시 선택하기
          </router-link>
        </div>
      </div>

      <!-- No Results -->
      <div v-if="!hasRecommendations" class="text-center py-12">
        <div class="text-6xl mb-4">🤔</div>
        <h2 class="text-2xl font-semibold text-neutral-900 mb-2">
          아직 추천할 상품이 없어요
        </h2>
        <p class="text-neutral-600 mb-6">
          다른 조건으로 다시 시도해보세요
        </p>
        <router-link to="/" class="btn-primary">
          다시 선택하기
        </router-link>
      </div>

      <!-- Results Grid -->
      <div v-else>
        <div class="mb-6">
          <h2 class="text-xl font-semibold text-neutral-900">
            추천 상품 {{ recommendations.length }}개
          </h2>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="product in recommendations"
            :key="product.id"
            class="card-hover"
            @click="viewProduct(product)"
          >
            <div class="relative">
              <img
                :src="product.imageUrl"
                :alt="product.name"
                class="w-full h-48 object-cover rounded-t-lg"
              />
              <div class="absolute top-2 right-2 bg-white px-2 py-1 rounded-full text-sm font-medium">
                ⭐ {{ product.rating }}
              </div>
            </div>
            
            <div class="p-4">
              <div class="text-sm text-neutral-600 mb-1">{{ product.brand }}</div>
              <h3 class="font-semibold text-neutral-900 mb-2 line-clamp-2">
                {{ product.name }}
              </h3>
              <p class="text-sm text-neutral-600 mb-3 line-clamp-2">
                {{ product.description }}
              </p>
              
              <div class="flex justify-between items-center">
                <div class="text-lg font-bold text-primary">
                  {{ formatPrice(product.price) }}원
                </div>
                <div class="text-sm text-neutral-600">
                  리뷰 {{ product.reviewCount }}개
                </div>
              </div>
              
              <div class="mt-3 flex gap-2">
                <span class="px-2 py-1 bg-neutral-100 text-neutral-600 text-xs rounded-full">
                  {{ getCategoryLabel(product.category) }}
                </span>
                <span class="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-full">
                  {{ getStyleLabel(product.style) }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore.js'
import { SportTypes, StyleTypes, BudgetRanges } from '../types/index.js'

export default {
  name: 'RecommendationResults',
  setup() {
    const router = useRouter()
    const userStore = useUserStore()
    
    // Computed
    const userProfile = computed(() => userStore.userProfile)
    const recommendations = computed(() => userStore.recommendations)
    const hasRecommendations = computed(() => userStore.hasRecommendations)
    
    // Methods
    const viewProduct = (product) => {
      userStore.selectProduct(product)
      router.push(`/product/${product.id}`)
    }
    
    const formatPrice = (price) => {
      return new Intl.NumberFormat('ko-KR').format(price)
    }
    
    const getSportLabel = (sport) => {
      const labels = {
        [SportTypes.TENNIS]: '테니스',
        [SportTypes.BADMINTON]: '배드민턴',
        [SportTypes.SOCCER]: '축구',
        [SportTypes.BASKETBALL]: '농구',
        [SportTypes.RUNNING]: '러닝'
      }
      return labels[sport] || sport
    }
    
    const getStyleLabel = (style) => {
      const labels = {
        [StyleTypes.CASUAL]: '캐주얼',
        [StyleTypes.PROFESSIONAL]: '프로페셔널',
        [StyleTypes.BEGINNER_FRIENDLY]: '초보자 친화',
        [StyleTypes.PERFORMANCE]: '퍼포먼스'
      }
      return labels[style] || style
    }
    
    const getBudgetLabel = (budget) => {
      const labels = {
        [BudgetRanges.LOW]: '합리적인 가격',
        [BudgetRanges.MEDIUM]: '중간 가격대',
        [BudgetRanges.HIGH]: '프리미엄'
      }
      return labels[budget] || budget
    }
    
    const getCategoryLabel = (category) => {
      return getSportLabel(category)
    }
    
    // Redirect if no profile
    if (!userStore.hasProfile) {
      router.push('/')
    }
    
    return {
      userProfile,
      recommendations,
      hasRecommendations,
      viewProduct,
      formatPrice,
      getSportLabel,
      getStyleLabel,
      getBudgetLabel,
      getCategoryLabel
    }
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
