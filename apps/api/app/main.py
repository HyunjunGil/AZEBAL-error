from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products, recommendations

# Create FastAPI instance
app = FastAPI(
    title="Sports Equipment Recommendation API",
    description="Mock API for sports equipment recommendation prototype",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(recommendations.router, prefix="/api", tags=["recommendations"])

@app.get("/")
async def root():
    return {"message": "Sports Equipment Recommendation API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "api_version": "1.0.0"}