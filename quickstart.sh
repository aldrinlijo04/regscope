#!/bin/bash

# RegScope - Quick Start Setup Script
# AI-Powered Global Legal Compliance Intelligence for FinTechs

echo "========================================="
echo "🌐 RegScope Setup"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

echo "✅ Python and Node.js found"
echo ""

# Backend Setup
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Backend setup complete!"
echo ""

# Frontend Setup
echo "📦 Setting up Frontend..."
cd ../frontend

# Install dependencies
echo "Installing Node dependencies..."
npm install

echo "✅ Frontend setup complete!"
echo ""

# Configuration check
echo "🔧 Configuration Check..."
cd ../backend

if [ -f ".env" ]; then
    echo "✅ Environment file (.env) exists"
    if grep -q "GEMINI_API_KEY" .env; then
        echo "✅ Gemini API key configured"
    else
        echo "⚠️  Gemini API key not found in .env"
    fi
else
    echo "⚠️  .env file not found. Creating template..."
    cat > .env << EOF
# RegScope Configuration
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL_NAME=gemini-pro
API_HOST=0.0.0.0
API_PORT=8000
EOF
    echo "✅ .env template created. Please add your Gemini API key."
fi

echo ""
echo "========================================="
echo "🎉 Setup Complete!"
echo "========================================="
echo ""
echo "To start RegScope:"
echo ""
echo "1️⃣  Start Backend (Terminal 1):"
echo "   cd backend"
echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "   uvicorn main:app --reload --port 8000"
echo ""
echo "2️⃣  Start Frontend (Terminal 2):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "3️⃣  Access RegScope:"
echo "   Frontend: http://localhost:5173"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📚 See TRANSFORMATION_SUMMARY.md for detailed information"
echo "========================================="
