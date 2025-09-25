<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 flex items-center justify-center py-12">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <!-- Success Animation -->
      <div class="mb-8">
        <div class="text-8xl mb-4 animate-bounce">🎉</div>
        <div class="text-6xl text-green-500 mb-6">✅</div>
      </div>
      
      <!-- Success Message -->
      <div class="bg-white rounded-lg shadow-lg p-8 mb-8">
        <h1 class="text-3xl font-bold text-neutral-900 mb-4">
          주문이 완료되었습니다!
        </h1>
        <p class="text-lg text-neutral-600 mb-6">
          선택하신 상품이 곧 배송될 예정입니다
        </p>
        
        <!-- Order Summary -->
        <div v-if="selectedProduct" class="border-t border-neutral-200 pt-6">
          <h3 class="text-lg font-semibold text-neutral-900 mb-4">주문 상품</h3>
          <div class="flex items-center gap-4 p-4 bg-neutral-50 rounded-lg">
            <img
              :src="selectedProduct.imageUrl"
              :alt="selectedProduct.name"
              class="w-16 h-16 object-cover rounded"
            />
            <div class="flex-1 text-left">
              <div class="font-medium text-neutral-900">{{ selectedProduct.name }}</div>
              <div class="text-sm text-neutral-600">{{ selectedProduct.brand }}</div>
              <div class="text-lg font-bold text-primary">
                {{ formatPrice(selectedProduct.price) }}원
              </div>
            </div>
          </div>
        </div>
        
        <!-- Order Details -->
        <div class="border-t border-neutral-200 pt-6 mt-6">
          <div class="grid grid-cols-2 gap-4 text-sm">
            <div>
              <div class="text-neutral-600">주문번호</div>
              <div class="font-medium">{{ orderNumber }}</div>
            </div>
            <div>
              <div class="text-neutral-600">주문일시</div>
              <div class="font-medium">{{ orderDate }}</div>
            </div>
            <div>
              <div class="text-neutral-600">배송예정일</div>
              <div class="font-medium">{{ deliveryDate }}</div>
            </div>
            <div>
              <div class="text-neutral-600">배송방법</div>
              <div class="font-medium">무료배송</div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Prototype Notice -->
      <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-8">
        <div class="flex items-center justify-center gap-2 text-yellow-700">
          <span class="text-xl">⚠️</span>
          <span class="font-medium">프로토타입 안내</span>
        </div>
        <p class="text-sm text-yellow-600 mt-2">
          이는 프로토타입 화면으로, 실제 결제나 배송이 이루어지지 않습니다.
        </p>
      </div>
      
      <!-- Action Buttons -->
      <div class="space-y-4">
        <button
          @click="continueShopping"
          class="w-full btn-primary text-lg py-3"
        >
          계속 쇼핑하기
        </button>
        
        <button
          @click="goHome"
          class="w-full bg-white border-2 border-neutral-300 text-neutral-700 px-6 py-3 rounded-lg font-medium hover:bg-neutral-50 transition-colors"
        >
          처음으로 돌아가기
        </button>
      </div>
      
      <!-- Feedback Section -->
      <div class="mt-12 bg-white rounded-lg p-6">
        <h3 class="text-lg font-semibold text-neutral-900 mb-4">
          프로토타입 체험은 어떠셨나요?
        </h3>
        <div class="flex justify-center gap-2 mb-4">
          <button
            v-for="rating in [1, 2, 3, 4, 5]"
            :key="rating"
            @click="setFeedbackRating(rating)"
            :class="[
              'text-2xl transition-transform hover:scale-110',
              feedbackRating >= rating ? 'text-yellow-400' : 'text-neutral-300'
            ]"
          >
            ⭐
          </button>
        </div>
        <textarea
          v-model="feedbackComment"
          placeholder="사용 경험에 대한 의견을 자유롭게 작성해주세요..."
          class="w-full p-3 border border-neutral-300 rounded-lg resize-none"
          rows="3"
        ></textarea>
        <button
          @click="submitFeedback"
          class="mt-3 px-4 py-2 bg-secondary text-white rounded font-medium hover:bg-green-600 transition-colors"
        >
          피드백 제출
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore.js'

export default {
  name: 'PurchaseComplete',
  setup() {
    const router = useRouter()
    const userStore = useUserStore()
    
    // Reactive state
    const feedbackRating = ref(0)
    const feedbackComment = ref('')
    const orderNumber = ref('')
    const orderDate = ref('')
    const deliveryDate = ref('')
    
    // Computed
    const selectedProduct = computed(() => userStore.selectedProduct)
    
    // Methods
    const generateOrderInfo = () => {
      // Generate mock order number
      orderNumber.value = 'ORD' + Date.now().toString().slice(-8)
      
      // Set order date to now
      const now = new Date()
      orderDate.value = now.toLocaleDateString('ko-KR')
      
      // Set delivery date to 2 days from now
      const delivery = new Date(now)
      delivery.setDate(delivery.getDate() + 2)
      deliveryDate.value = delivery.toLocaleDateString('ko-KR')
    }
    
    const formatPrice = (price) => {
      return new Intl.NumberFormat('ko-KR').format(price)
    }
    
    const setFeedbackRating = (rating) => {
      feedbackRating.value = rating
    }
    
    const submitFeedback = () => {
      // In a real app, this would send feedback to the server
      alert('피드백을 제출해주셔서 감사합니다! 🙏')
      feedbackRating.value = 0
      feedbackComment.value = ''
    }
    
    const continueShopping = () => {
      // Clear current selection and go back to profile selection
      router.push('/')
    }
    
    const goHome = () => {
      // Clear all store data and go to home
      userStore.clearProfile()
      router.push('/')
    }
    
    onMounted(() => {
      generateOrderInfo()
    })
    
    return {
      selectedProduct,
      feedbackRating,
      feedbackComment,
      orderNumber,
      orderDate,
      deliveryDate,
      formatPrice,
      setFeedbackRating,
      submitFeedback,
      continueShopping,
      goHome
    }
  }
}
</script>

<style scoped>
@keyframes bounce {
  0%, 20%, 53%, 80%, 100% {
    transform: translateY(0);
  }
  40%, 43% {
    transform: translateY(-30px);
  }
  70% {
    transform: translateY(-15px);
  }
  90% {
    transform: translateY(-4px);
  }
}

.animate-bounce {
  animation: bounce 2s infinite;
}
</style>
