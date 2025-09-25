#!/bin/bash
# Test runner script for Sports Equipment Recommendation API

set -e

echo "🧪 Starting FastAPI Backend Tests..."
echo "======================================="

# Activate conda environment
if command -v conda &> /dev/null; then
    echo "Activating conda environment: sports-api"
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate sports-api
else
    echo "⚠️  Conda not found. Make sure dependencies are installed."
fi

# Run tests with coverage
echo "🔍 Running pytest with coverage..."
python -m pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html

echo ""
echo "✅ All tests completed!"
echo "📊 Coverage report generated in htmlcov/index.html"
echo ""
echo "To run specific test categories:"
echo "  python -m pytest tests/test_main.py -v          # Main app tests"
echo "  python -m pytest tests/test_products.py -v      # Products API tests"  
echo "  python -m pytest tests/test_recommendations.py -v # Recommendations tests"
echo "  python -m pytest tests/test_data.py -v          # Data layer tests"
