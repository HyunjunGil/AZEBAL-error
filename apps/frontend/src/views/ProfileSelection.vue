<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 py-12">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold text-neutral-900 mb-4">
          나에게 딱 맞는 스포츠 용품을 찾아보세요!
        </h1>
        <p class="text-xl text-neutral-600">
          간단한 질문에 답하면 맞춤형 추천을 받으실 수 있어요
        </p>
      </div>

      <!-- Sport Selection -->
      <div class="mb-8">
        <h2 class="text-2xl font-semibold text-neutral-900 mb-6 text-center">
          어떤 스포츠를 시작하시나요?
        </h2>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          <div
            v-for="sport in sportOptions"
            :key="sport.value"
            :class="[
              'card-hover text-center py-6',
              selectedSport === sport.value ? 'ring-2 ring-primary bg-blue-50' : ''
            ]"
            @click="selectedSport = sport.value"
          >
            <div class="text-4xl mb-3">{{ sport.emoji }}</div>
            <div class="font-medium">{{ sport.label }}</div>
          </div>
        </div>
      </div>

      <!-- Style Selection -->
      <div class="mb-8" v-if="selectedSport">
        <h2 class="text-2xl font-semibold text-neutral-900 mb-6 text-center">
          어떤 스타일을 원하시나요?
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div
            v-for="style in styleOptions"
            :key="style.value"
            :class="[
              'card-hover text-center py-6',
              selectedStyle === style.value ? 'ring-2 ring-secondary bg-green-50' : ''
            ]"
            @click="selectedStyle = style.value"
          >
            <div class="text-3xl mb-3">{{ style.emoji }}</div>
            <div class="font-medium mb-2">{{ style.label }}</div>
            <div class="text-sm text-neutral-600">{{ style.description }}</div>
          </div>
        </div>
      </div>

      <!-- Budget Selection -->
      <div class="mb-8" v-if="selectedStyle">
        <h2 class="text-2xl font-semibold text-neutral-900 mb-6 text-center">
          예산은 어느 정도로 생각하고 계시나요?
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div
            v-for="budget in budgetOptions"
            :key="budget.value"
            :class="[
              'card-hover text-center py-6',
              selectedBudget === budget.value ? 'ring-2 ring-primary bg-blue-50' : ''
            ]"
            @click="selectedBudget = budget.value"
          >
            <div class="text-3xl mb-3">{{ budget.emoji }}</div>
            <div class="font-medium mb-2">{{ budget.label }}</div>
            <div class="text-sm text-neutral-600">{{ budget.description }}</div>
          </div>
        </div>
      </div>

      <!-- Submit Button -->
      <div class="text-center" v-if="canProceed">
        <button
          @click="getRecommendations"
          :disabled="!canProceed"
          class="btn-primary text-lg px-8 py-4 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          맞춤 추천 받기 ✨
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore.js'
import { SportTypes, StyleTypes, BudgetRanges } from '../types/index.js'

export default {
  name: 'ProfileSelection',
  setup() {
    const router = useRouter()
    const userStore = useUserStore()
    
    // Reactive state
    const selectedSport = ref('')
    const selectedStyle = ref('')
    const selectedBudget = ref('')
    
    // Options data
    const sportOptions = [
      { value: SportTypes.TENNIS, label: '테니스', emoji: '🎾' },
      { value: SportTypes.BADMINTON, label: '배드민턴', emoji: '🏸' },
      { value: SportTypes.SOCCER, label: '축구', emoji: '⚽' },
      { value: SportTypes.BASKETBALL, label: '농구', emoji: '🏀' },
      { value: SportTypes.RUNNING, label: '러닝', emoji: '🏃‍♂️' }
    ]
    
    const styleOptions = [
      { 
        value: StyleTypes.CASUAL, 
        label: '캐주얼', 
        emoji: '😊',
        description: '편안하고 일상적인 운동'
      },
      { 
        value: StyleTypes.PROFESSIONAL, 
        label: '프로페셔널', 
        emoji: '💪',
        description: '진지하고 전문적인 운동'
      },
      { 
        value: StyleTypes.BEGINNER_FRIENDLY, 
        label: '초보자 친화', 
        emoji: '🌱',
        description: '처음 시작하는 분들께'
      },
      { 
        value: StyleTypes.PERFORMANCE, 
        label: '퍼포먼스', 
        emoji: '🔥',
        description: '최고의 성능을 추구'
      }
    ]
    
    const budgetOptions = [
      { 
        value: BudgetRanges.LOW, 
        label: '합리적인 가격', 
        emoji: '💰',
        description: '~50만원' 
      },
      { 
        value: BudgetRanges.MEDIUM, 
        label: '중간 가격대', 
        emoji: '💳',
        description: '50~100만원' 
      },
      { 
        value: BudgetRanges.HIGH, 
        label: '프리미엄', 
        emoji: '💎',
        description: '100만원+' 
      }
    ]
    
    // Computed
    const canProceed = computed(() => 
      selectedSport.value && selectedStyle.value && selectedBudget.value
    )
    
    // Methods
    const getRecommendations = async () => {
      const profile = {
        sport: selectedSport.value,
        style: selectedStyle.value,
        budget: selectedBudget.value
      }
      
      await userStore.setProfile(profile)
      router.push('/recommendations')
    }
    
    return {
      selectedSport,
      selectedStyle,
      selectedBudget,
      sportOptions,
      styleOptions,
      budgetOptions,
      canProceed,
      getRecommendations
    }
  }
}
</script>
