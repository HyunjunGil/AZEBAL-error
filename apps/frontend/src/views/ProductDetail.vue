<template>
  <div class="min-h-screen bg-neutral-100 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Breadcrumb -->
      <div class="mb-6">
        <nav class="flex text-sm text-neutral-600">
          <router-link to="/" class="hover:text-primary">홈</router-link>
          <span class="mx-2">></span>
          <router-link to="/recommendations" class="hover:text-primary">추천 결과</router-link>
          <span class="mx-2">></span>
          <span class="text-neutral-900">{{ product?.name }}</span>
        </nav>
      </div>

      <div v-if="loading" class="text-center py-12">
        <div class="text-6xl mb-4">⏳</div>
        <h2 class="text-2xl font-semibold text-neutral-900">
          상품 정보를 불러오는 중...
        </h2>
      </div>

      <div v-else-if="error" class="text-center py-12">
        <div class="text-6xl mb-4">❌</div>
        <h2 class="text-2xl font-semibold text-neutral-900 mb-2">
          상품을 불러올 수 없습니다
        </h2>
        <p class="text-neutral-600 mb-4">{{ error }}</p>
        <router-link to="/recommendations" class="btn-primary">
          추천 목록으로 돌아가기
        </router-link>
      </div>

      <div v-else-if="!product" class="text-center py-12">
        <h2 class="text-2xl font-semibold text-neutral-900">
          상품을 찾을 수 없습니다
        </h2>
        <router-link to="/recommendations" class="btn-primary mt-4">
          추천 목록으로 돌아가기
        </router-link>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
        <!-- Product Image -->
        <div class="space-y-4">
          <div class="bg-white rounded-lg overflow-hidden">
            <img
              :src="product.imageUrl"
              :alt="product.name"
              class="w-full h-96 object-cover"
            />
          </div>
        </div>

        <!-- Product Info -->
        <div class="space-y-6">
          <div>
            <div class="text-lg text-neutral-600 mb-2">{{ product.brand }}</div>
            <h1 class="text-3xl font-bold text-neutral-900 mb-4">
              {{ product.name }}
            </h1>
            <div class="flex items-center gap-4 mb-4">
              <div class="flex items-center">
                <span class="text-yellow-400 text-xl">⭐</span>
                <span class="font-semibold ml-1">{{ product.rating }}</span>
              </div>
              <div class="text-neutral-600">
                리뷰 {{ product.reviewCount }}개
              </div>
            </div>
            <div class="text-3xl font-bold text-primary mb-6">
              {{ formatPrice(product.price) }}원
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold text-neutral-900 mb-3">상품 설명</h3>
            <p class="text-neutral-600 leading-relaxed">
              {{ product.description }}
            </p>
          </div>

          <div class="flex gap-3">
            <span class="px-3 py-1 bg-neutral-100 text-neutral-700 rounded-full">
              {{ getCategoryLabel(product.category) }}
            </span>
            <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full">
              {{ getStyleLabel(product.style) }}
            </span>
          </div>

          <!-- Purchase Button -->
          <div class="pt-6">
            <button
              @click="purchaseProduct"
              class="w-full btn-primary text-lg py-4 mb-3"
            >
              구매하기 🛒
            </button>
            <p class="text-sm text-neutral-600 text-center">
              * 프로토타입에서는 실제 결제가 진행되지 않습니다
            </p>
          </div>
        </div>
      </div>

      <!-- Reviews Section -->
      <div v-if="reviews.length > 0" class="bg-white rounded-lg p-6">
        <h2 class="text-2xl font-bold text-neutral-900 mb-6">
          고객 리뷰 ({{ reviews.length }})
        </h2>
        
        <div class="space-y-6">
          <div
            v-for="review in reviews"
            :key="review.id"
            class="border-b border-neutral-200 pb-6 last:border-b-0"
          >
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-primary text-white rounded-full flex items-center justify-center font-semibold">
                  {{ review.author.charAt(0) }}
                </div>
                <div>
                  <div class="font-medium text-neutral-900">{{ review.author }}</div>
                  <div class="text-sm text-neutral-600">{{ formatDate(review.date) }}</div>
                </div>
              </div>
              <div class="flex items-center">
                <span v-for="i in 5" :key="i" class="text-yellow-400">
                  {{ i <= review.rating ? '⭐' : '☆' }}
                </span>
              </div>
            </div>
            
            <p class="text-neutral-700 leading-relaxed mb-3">
              {{ review.comment }}
            </p>
            
            <div v-if="review.videoUrl" class="bg-neutral-100 rounded-lg p-4">
              <div class="flex items-center gap-2 text-neutral-600">
                <span>🎥</span>
                <span class="text-sm">동영상 리뷰가 있습니다</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore.js'
import { apiService } from '../services/api.js'
import { SportTypes, StyleTypes } from '../types/index.js'

export default {
  name: 'ProductDetail',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const userStore = useUserStore()
    
    // Reactive state
    const product = ref(null)
    const reviews = ref([])
    const loading = ref(true)
    const error = ref(null)
    
    // Methods
    const loadProductDetail = async () => {
      try {
        loading.value = true
        const productId = route.params.id
        
        // First try to use product from store if available
        if (userStore.selectedProduct && userStore.selectedProduct.id === productId) {
          product.value = userStore.selectedProduct
        }
        
        // Always fetch detailed data from API (including reviews)
        const productDetail = await apiService.getProductDetail(productId)
        product.value = productDetail.product
        reviews.value = productDetail.reviews
        
        // Update store if needed
        if (!userStore.selectedProduct || userStore.selectedProduct.id !== productId) {
          userStore.selectProduct(productDetail.product)
        }
        
      } catch (err) {
        console.error('Failed to load product detail:', err)
        error.value = 'Failed to load product details'
      } finally {
        loading.value = false
      }
    }
    
    // Methods
    const formatPrice = (price) => {
      return new Intl.NumberFormat('ko-KR').format(price)
    }
    
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString('ko-KR')
    }
    
    const getCategoryLabel = (category) => {
      const labels = {
        [SportTypes.TENNIS]: '테니스',
        [SportTypes.BADMINTON]: '배드민턴',
        [SportTypes.SOCCER]: '축구',
        [SportTypes.BASKETBALL]: '농구',
        [SportTypes.RUNNING]: '러닝'
      }
      return labels[category] || category
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
    
    const purchaseProduct = () => {
      // Navigate to purchase complete page
      router.push('/purchase-complete')
    }
    
    onMounted(() => {
      loadProductDetail()
    })
    
    return {
      product,
      reviews,
      loading,
      error,
      formatPrice,
      formatDate,
      getCategoryLabel,
      getStyleLabel,
      purchaseProduct
    }
  }
}
</script>
