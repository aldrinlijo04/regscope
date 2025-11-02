# RegScope Deployment to Render - Complete Guide

## 🚀 Deploy RegScope on Render (Free Tier)

This guide will help you deploy both the **backend API** and **frontend** on Render.

---

## 📋 Prerequisites

1. **GitHub Account** - Your code needs to be in a GitHub repository
2. **Render Account** - Sign up at https://render.com (free tier available)
3. **Gemini API Key** - AIzaSyDMRPwXhqpdIheKagDCUKJSdPso8byMF78

---

## 🔧 Step 1: Prepare Your Code for Deployment

### Backend Preparation (Already Done!)
✅ `Procfile` created - tells Render how to start the app
✅ `runtime.txt` created - specifies Python version
✅ `requirements.txt` updated - all dependencies listed

### Frontend Preparation
The frontend is already configured with Vite - no changes needed!

---

## 📤 Step 2: Push Code to GitHub

If you haven't already, push your code to GitHub:

```bash
cd /Users/aldrinlijo/Developer/personal/legal-guard-regtech-master

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "RegScope - Ready for deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/regscope.git
git branch -M main
git push -u origin main
```

---

## 🎯 Step 3: Deploy Backend API on Render

### 3.1 Create Web Service

1. **Go to Render Dashboard**: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. **Connect GitHub Repository**:
   - Authorize Render to access your GitHub
   - Select your `regscope` repository

### 3.2 Configure Backend Service

Fill in the following settings:

| Setting | Value |
|---------|-------|
| **Name** | `regscope-api` |
| **Region** | Choose closest to you (e.g., Oregon, Singapore) |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` |

### 3.3 Add Environment Variables

Click **"Advanced"** and add these environment variables:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | `AIzaSyDMRPwXhqpdIheKagDCUKJSdPso8byMF78` |
| `GEMINI_MODEL_NAME` | `gemini-pro` |
| `PYTHON_VERSION` | `3.12.0` |

### 3.4 Deploy Backend

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. Your API will be available at: `https://regscope-api.onrender.com`

### 3.5 Test Backend

Once deployed, test your API:
- Visit: `https://regscope-api.onrender.com/docs`
- You should see the FastAPI interactive documentation

---

## 🎨 Step 4: Deploy Frontend on Render

### 4.1 Update Frontend API URL

Before deploying frontend, update the API URL:

**File: `frontend/src/services/api.ts` (or similar)**

Create/Update the API base URL configuration:

```typescript
// Use environment variable or fallback to Render backend URL
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://regscope-api.onrender.com';
```

### 4.2 Create Frontend Service

1. Click **"New +"** → **"Static Site"**
2. Select your `regscope` repository

### 4.3 Configure Frontend Service

| Setting | Value |
|---------|-------|
| **Name** | `regscope-frontend` |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | `npm install && npm run build` |
| **Publish Directory** | `dist` |

### 4.4 Add Frontend Environment Variables

Click **"Advanced"** and add:

| Key | Value |
|-----|-------|
| `VITE_API_URL` | `https://regscope-api.onrender.com` |

### 4.5 Deploy Frontend

1. Click **"Create Static Site"**
2. Wait 3-5 minutes for deployment
3. Your frontend will be available at: `https://regscope-frontend.onrender.com`

---

## 🔐 Step 5: Update CORS Settings

After deployment, update backend CORS to allow frontend:

**File: `backend/main.py`**

Update the CORS origins to include your Render URLs:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173", 
        "http://localhost:5174", 
        "http://localhost:5175",
        "https://regscope-frontend.onrender.com",  # Add this
        "https://*.onrender.com"  # Allow all Render preview URLs
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Commit and push this change - Render will auto-deploy!

---

## 📊 Step 6: Verify Deployment

### Backend Checks:
1. ✅ Visit `https://regscope-api.onrender.com`
2. ✅ Visit `https://regscope-api.onrender.com/docs` - Should show API docs
3. ✅ Test endpoint: `https://regscope-api.onrender.com/api/v1/fintech/health`

### Frontend Checks:
1. ✅ Visit `https://regscope-frontend.onrender.com`
2. ✅ Landing page should load with RegScope branding
3. ✅ Try navigating to different pages
4. ✅ Test API connection (try analyze or compliance features)

---

## 🎯 Quick Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Backend web service created on Render
- [ ] Backend environment variables added (GEMINI_API_KEY)
- [ ] Backend deployed successfully
- [ ] Backend API tested via `/docs`
- [ ] Frontend static site created on Render
- [ ] Frontend environment variable added (VITE_API_URL)
- [ ] Frontend deployed successfully
- [ ] CORS updated in backend
- [ ] Full application tested end-to-end

---

## ⚠️ Important Notes

### Free Tier Limitations:
- **Backend**: Spins down after 15 minutes of inactivity (first request will be slow)
- **Database**: Not included in free tier (you're using JSON files, so this is fine)
- **Build Time**: Limited to 500 build minutes/month
- **Bandwidth**: 100GB/month

### Performance Tips:
1. **Keep Backend Warm**: Use a service like UptimeRobot to ping your API every 14 minutes
2. **Optimize Build**: Frontend builds are cached by Render
3. **Monitor Logs**: Check Render dashboard for any errors

### Upgrading to Paid:
If you need better performance:
- **Starter Plan** ($7/month): No spin-down, faster deployments
- **Standard Plan** ($25/month): More resources, faster response times

---

## 🔄 Auto-Deploy on Git Push

Render automatically deploys when you push to GitHub:

```bash
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main

# Render will automatically:
# 1. Detect the push
# 2. Rebuild your services
# 3. Deploy new versions
```

---

## 🐛 Troubleshooting

### Backend Won't Start:
```bash
# Check Render logs in dashboard
# Common issues:
# - Missing environment variables
# - Incorrect Python version
# - Missing dependencies in requirements.txt
```

### Frontend Can't Connect to Backend:
```bash
# Check:
# 1. VITE_API_URL is correct in frontend environment variables
# 2. CORS allows your frontend domain in backend
# 3. Backend is running (visit /docs endpoint)
```

### Gemini API Not Working:
```bash
# Verify:
# 1. GEMINI_API_KEY is set in backend environment variables
# 2. API key is valid (test locally first)
# 3. Check backend logs for API errors
```

---

## 📱 Custom Domain (Optional)

To use your own domain:

1. Go to your service settings on Render
2. Click **"Custom Domain"**
3. Add your domain (e.g., `regscope.yourdomain.com`)
4. Update DNS records as instructed
5. Render provides free SSL certificates!

---

## 🎉 You're Live!

Once deployed, you'll have:

- **API**: `https://regscope-api.onrender.com`
- **Frontend**: `https://regscope-frontend.onrender.com`
- **Auto-deployment**: On every git push
- **Free SSL**: Automatic HTTPS
- **Logs**: Available in Render dashboard

---

## 📚 Additional Resources

- **Render Docs**: https://render.com/docs
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Vite Deployment**: https://vitejs.dev/guide/static-deploy.html

---

## 🆘 Need Help?

If you encounter issues:

1. **Check Render Logs**: Dashboard → Your Service → Logs
2. **Test Locally First**: Make sure everything works on localhost
3. **Verify Environment Variables**: Double-check all API keys
4. **Check Build Logs**: Look for errors during deployment

---

**Congratulations! RegScope is now live on Render! 🚀**
