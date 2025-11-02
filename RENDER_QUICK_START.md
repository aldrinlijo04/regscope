# 🚀 RegScope - Render Deployment Quick Reference

## ⚡ Quick Start (5 Minutes)

### 1️⃣ Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/regscope.git
git push -u origin main
```

### 2️⃣ Deploy Backend
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo
4. **Settings:**
   - Name: `regscope-api`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Environment Variables:**
   - `GEMINI_API_KEY` = `your_actual_gemini_api_key`
   - `GEMINI_MODEL_NAME` = `gemini-pro`
6. Click **"Create Web Service"**

### 3️⃣ Deploy Frontend
1. Click **"New +"** → **"Static Site"**
2. Connect your GitHub repo
3. **Settings:**
   - Name: `regscope-frontend`
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `dist`
4. **Environment Variable:**
   - `VITE_API_URL` = `https://regscope-api.onrender.com`
5. Click **"Create Static Site"**

---

## 📋 Configuration Files (Already Created)

✅ `backend/Procfile` - Start command for Render  
✅ `backend/runtime.txt` - Python version (3.12.0)  
✅ `backend/requirements.txt` - Updated with all dependencies  
✅ `render.yaml` - Blueprint for one-click deploy  
✅ Backend CORS updated to allow Render URLs  

---

## 🔗 Your Live URLs

After deployment:
- **API**: `https://regscope-api.onrender.com`
- **API Docs**: `https://regscope-api.onrender.com/docs`
- **Frontend**: `https://regscope-frontend.onrender.com`

---

## ✅ Deployment Checklist

Backend:
- [ ] Repository on GitHub
- [ ] Web Service created on Render
- [ ] Root directory set to `backend`
- [ ] GEMINI_API_KEY environment variable added
- [ ] Service deployed successfully
- [ ] Visit `/docs` to verify API is running

Frontend:
- [ ] Static Site created on Render
- [ ] Root directory set to `frontend`
- [ ] VITE_API_URL environment variable added
- [ ] Site deployed successfully
- [ ] Landing page loads correctly
- [ ] Can connect to backend API

---

## 🐛 Common Issues & Solutions

### Backend won't start
**Problem**: Missing dependencies or wrong Python version  
**Solution**: Check Render logs, verify `requirements.txt` is complete

### Frontend can't reach API
**Problem**: CORS or wrong API URL  
**Solution**: 
1. Verify `VITE_API_URL` in frontend env vars
2. Check backend CORS includes your frontend domain
3. Visit backend `/docs` to ensure it's running

### 502 Bad Gateway
**Problem**: Backend is sleeping (free tier)  
**Solution**: Wait 30-60 seconds for backend to wake up on first request

---

## 💡 Pro Tips

1. **Keep Backend Alive**: Use UptimeRobot to ping your API every 14 minutes (prevents sleep)
2. **Monitor Logs**: Check Render dashboard logs for errors
3. **Auto-Deploy**: Push to GitHub main branch triggers automatic deployment
4. **Environment Variables**: Never commit API keys - use Render's env vars

---

## 📞 Support

- **Render Docs**: https://render.com/docs
- **Render Status**: https://status.render.com
- **Your Dashboard**: https://dashboard.render.com

---

## 🎯 Next Steps After Deployment

1. Test all API endpoints at `/docs`
2. Navigate through frontend pages
3. Try AML screening feature
4. Test transaction analysis
5. Share your live URL!

**Your RegScope is now live! 🎉**
