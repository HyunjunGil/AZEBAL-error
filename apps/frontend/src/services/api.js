// API service for communicating with the FastAPI backend

const API_BASE_URL = 'http://localhost:8000/api'

class ApiService {
  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`
    
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    }
    
    try {
      const response = await fetch(url, config)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      return await response.json()
    } catch (error) {
      console.error('API request failed:', error)
      throw error
    }
  }
  
  // Get all products
  async getProducts() {
    return this.request('/products')
  }
  
  // Get product details with reviews
  async getProductDetail(productId) {
    return this.request(`/products/${productId}`)
  }
  
  // Get recommendations based on user profile
  async getRecommendations(profile) {
    return this.request('/recommendations', {
      method: 'POST',
      body: JSON.stringify({ profile })
    })
  }
  
  // Alternative recommendations endpoint using URL parameters
  async getRecommendationsByParams(sport, style, budget) {
    return this.request(`/recommendations/${sport}/${style}/${budget}`)
  }
}

// Create and export a singleton instance
export const apiService = new ApiService()
export default apiService
