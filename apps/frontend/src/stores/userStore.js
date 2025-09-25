import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { apiService } from '../services/api.js'

export const useUserStore = defineStore('user', () => {
  // State
  const userProfile = ref(null)
  const recommendations = ref([])
  const selectedProduct = ref(null)
  
  // Actions
  async function setProfile(profile) {
    userProfile.value = profile
    try {
      recommendations.value = await apiService.getRecommendations(profile)
    } catch (error) {
      console.error('Failed to get recommendations:', error)
      // Fallback to empty array if API fails
      recommendations.value = []
    }
  }
  
  function selectProduct(product) {
    selectedProduct.value = product
  }
  
  function clearProfile() {
    userProfile.value = null
    recommendations.value = []
    selectedProduct.value = null
  }
  
  // Getters
  const hasProfile = computed(() => userProfile.value !== null)
  const hasRecommendations = computed(() => recommendations.value.length > 0)
  
  return {
    // State
    userProfile,
    recommendations,
    selectedProduct,
    // Actions
    setProfile,
    selectProduct,
    clearProfile,
    // Getters
    hasProfile,
    hasRecommendations
  }
})
