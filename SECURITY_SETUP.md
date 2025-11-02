# 🔐 RegScope - Local Setup Instructions

## Setting Up Your API Key

Your Gemini API key has been secured and is **NOT** pushed to GitHub. Here's how to set it up locally:

### 1️⃣ **Create Your Local Environment File**

```bash
cd backend
cp .env.example .env
```

### 2️⃣ **Add Your API Key**

Open `backend/.env` and replace the placeholder:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**Your API key has been backed up to:** `~/.regscope_api_key_backup.txt`

You can retrieve it:
```bash
cat ~/.regscope_api_key_backup.txt
```

### 3️⃣ **Verify Setup**

```bash
cd backend
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✅ API Key loaded' if os.getenv('GEMINI_API_KEY') and os.getenv('GEMINI_API_KEY') != 'your_gemini_api_key_here' else '❌ API Key not set')"
```

---

## 🔒 Security Best Practices

✅ **DO:**
- Keep `.env` file in `.gitignore` (already done)
- Use environment variables on Render
- Share `.env.example` template (no secrets)
- Store API keys securely locally

❌ **DON'T:**
- Commit `.env` to GitHub
- Share API keys in public repositories
- Hardcode API keys in source code
- Include API keys in documentation

---

## 🚀 For Render Deployment

When deploying to Render, add your API key in the dashboard:
1. Go to your service settings
2. Click "Environment"
3. Add: `GEMINI_API_KEY` = `your_actual_key`
4. Save changes

See `RENDER_DEPLOYMENT_GUIDE.md` for complete instructions.

---

## 🆘 Lost Your API Key?

If you need a new Gemini API key:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Update your `backend/.env` file
4. Update Render environment variables

---

**Your API key is safe and not in version control! ✅**
