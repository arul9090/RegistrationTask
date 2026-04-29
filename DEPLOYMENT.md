# 🚀 Deployment Guide - SkillRank Project

## Free Deployment to Render.com

### **Prerequisites:**
1. GitHub account (free)
2. Render.com account (free)
3. MongoDB Atlas (already configured ✓)

---

## **Step 1: Push to GitHub**

1. **Initialize Git (if not already done)**
   ```bash
   cd API-Task
   git init
   git add .
   git commit -m "Initial commit: Flask app ready for deployment"
   ```

2. **Create GitHub Repository**
   - Go to https://github.com/new
   - Create a new repo (e.g., `skillrank-api`)
   - Copy the commands to push your code

3. **Push Code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/skillrank-api.git
   git branch -M main
   git push -u origin main
   ```

---

## **Step 2: Deploy on Render.com**

1. **Sign up at Render.com**
   - Go to https://render.com
   - Click "Get started"
   - Connect your GitHub account

2. **Create New Web Service**
   - Click "+ New" → "Web Service"
   - Select your GitHub repository
   - Connect repository

3. **Configure Deployment**
   - **Name:** `skillrank-api` (or any name)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

4. **Add Environment Variables**
   - Click "Environment" in settings
   - Add these variables:
   ```
   MONGO_URI=mongodb+srv://Arul:aruldev@cluster0.l30sq.mongodb.net/?appName=Cluster0
   MONGO_DB=skillrank_db
   GOOGLE_CLIENT_ID=528665321012-crk8frmjea9heh967innechl7tq3qfpv.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=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
   SECRET_KEY=your-secret-key-here-change-in-production
   JWT_SECRET=your-jwt-secret-here-change-in-production
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - Your app URL: `https://skillrank-api.onrender.com`

---

## **Step 3: Test Your Deployment**

```bash
# Test API endpoint
curl https://skillrank-api.onrender.com/

# Test login page
https://skillrank-api.onrender.com/login
```

---

## **Important Notes:**

⚠️ **Free Tier Limitations:**
- App goes to sleep after 15 minutes of inactivity
- Takes ~30 seconds to wake up on first request
- Limited to 2 deployments per month on free tier

✅ **To Avoid Sleep:**
- Upgrade to Starter plan ($7/month)
- Or use Railway.app (has monthly credit)

---

## **Alternative: Deploy on Railway.app**

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Add same environment variables
5. Railway auto-detects Procfile and deploys
6. Get $5 monthly credit (usually free tier)

---

## **Troubleshooting:**

**Issue:** App won't start
- Check logs in Render dashboard
- Verify all environment variables are set
- Check MongoDB connection string

**Issue:** Static files not loading
- Ensure `templates/` folder is in repository
- Flask serves static files automatically

**Issue:** Slow startup
- Free tier apps are slower
- Consider upgrading to paid tier for production

---

## **Next Steps:**

1. Keep MongoDB Atlas M0 free tier (always free)
2. Monitor your free tier usage
3. Plan upgrade path as you grow
4. Add custom domain (point to Render URL)

---

**Your MongoDB is already configured for free! ✓**
- Connection: MongoDB Atlas
- Tier: Free M0 (512MB storage)
- Status: Ready to deploy

