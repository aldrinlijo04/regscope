#!/bin/bash

# RegScope - Deploy to Render Helper Script

echo "========================================="
echo "🚀 RegScope - Render Deployment Helper"
echo "========================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git initialized"
else
    echo "✅ Git repository already initialized"
fi

# Check if remote is set
if ! git remote | grep -q "origin"; then
    echo ""
    echo "⚠️  No GitHub remote found."
    echo "Please create a repository on GitHub and add it:"
    echo ""
    echo "   git remote add origin https://github.com/YOUR_USERNAME/regscope.git"
    echo ""
else
    echo "✅ GitHub remote configured"
fi

# Add all files
echo ""
echo "📝 Adding files to git..."
git add .

# Show status
echo ""
echo "📊 Git Status:"
git status --short

# Prompt for commit
echo ""
read -p "Enter commit message (or press Enter for default): " commit_msg

if [ -z "$commit_msg" ]; then
    commit_msg="Update RegScope for deployment"
fi

git commit -m "$commit_msg"

echo ""
echo "========================================="
echo "✅ Ready to Push!"
echo "========================================="
echo ""
echo "To push to GitHub:"
echo "   git push origin main"
echo ""
echo "Then follow these steps:"
echo ""
echo "1️⃣  Go to https://dashboard.render.com"
echo "2️⃣  Click 'New +' → 'Web Service' for Backend"
echo "3️⃣  Click 'New +' → 'Static Site' for Frontend"
echo ""
echo "📚 See RENDER_DEPLOYMENT_GUIDE.md for detailed instructions"
echo ""
