# 📖 Vietnamese History Chatbot - Setup Guide

## 🎯 Complete Setup Instructions

This guide will walk you through setting up the Vietnamese History Chatbot on your computer.

---

## 📋 Prerequisites

Before starting, make sure you have:

- ✅ Python 3.8 or higher installed
- ✅ Git installed
- ✅ A Gemini API key (free from https://aistudio.google.com)
- ✅ Terminal/Command Prompt access

**Check Python version:**
```bash
python --version
# Should show: Python 3.8.0 or higher
```

---

## 🚀 Step-by-Step Setup

### Step 1: Get Gemini API Key

1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with Google account (free!)
3. Click **"Create API Key"**
4. Copy the key shown
5. Keep it safe - you'll need it later

### Step 2: Clone the Repository

```bash
# Choose a folder where you want to download the project
cd ~/Desktop  # or any folder you prefer

# Clone the repository
git clone https://github.com/Tindinhh/vietnamese-history-chatbot.git

# Enter the project folder
cd vietnamese-history-chatbot
```

Or download as ZIP and extract.

### Step 3: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**You should see `(venv)` at the start of your terminal line.**

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask
- google-generativeai
- python-dotenv
- gunicorn

### Step 5: Setup Environment Variables

**Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
# Then edit .env and add your API key
```

**macOS/Linux:**
```bash
cp .env.example .env
# Then edit .env and add your API key
```

**Edit .env file:**
Open `.env` in a text editor and replace:
```
GEMINI_API_KEY=your_api_key_here
```

With your actual API key:
```
GEMINI_API_KEY=AIzaSy_xxxxxxxxxxxxxxxxxxxxx
```

**⚠️ IMPORTANT:**
- Never share your API key!
- Never commit .env to Git!
- Keep it private!

### Step 6: Run the Application

```bash
# Method 1: Using run.py (recommended)
python run.py

# Method 2: Using main.py directly
python app/main.py

# Method 3: Using gunicorn (production)
gunicorn --bind 0.0.0.0:5000 app.main:app
```

**Expected output:**
```
============================================================
🇻🇳 SỬ VIỆT TOÀN THƯ - Vietnamese History Chatbot
============================================================
✅ Flask app starting...
📍 Visit: http://localhost:5000
⚠️  Press CTRL+C to stop the server
============================================================
```

### Step 7: Open in Browser

1. Open your web browser (Chrome, Firefox, Safari, Edge, etc.)
2. Go to: **http://localhost:5000**
3. You should see the Vietnamese History Chatbot! 🎉

---

## 💬 Test the Chatbot

Try these questions:

**✅ Valid Questions (related to Vietnamese History):**
- "Ai là vua Quang Trung?"
- "Nhà Trần có bao nhiêu vị vua?"
- "Tây Sơn là gì?"
- "Trần Hưng Đạo chống Mông Nguyên như thế nào?"

**❌ Invalid Questions (not about Vietnamese History):**
- "Thời tiết hôm nay thế nào?" (Weather)
- "2+2 bằng bao nhiêu?" (Math)
- "Cách nấu phở" (Cooking)

The chatbot will only answer questions about Vietnamese history!

---

## 🛑 Stop the Application

Press **CTRL + C** in the terminal to stop the server.

```bash
^C  # Press Ctrl+C
Shutting down...
```

---

## ⚙️ Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Then reinstall:
pip install -r requirements.txt
```

### Problem: "GEMINI_API_KEY not found in .env file"

**Solution:**
1. Check that `.env` file exists in the project root
2. Make sure `GEMINI_API_KEY=...` is in the file
3. Make sure you added your actual API key
4. Restart the application

### Problem: "Connection refused on localhost:5000"

**Solution:**
1. Make sure the Flask app is running (you should see the startup message)
2. Try a different port: `python run.py` then set `PORT=8000 python run.py`
3. Check if port 5000 is already in use
4. Try: `python -m flask run --host 0.0.0.0 --port 5000`

### Problem: "API Error" when asking questions

**Solution:**
1. Verify your API key is correct
2. Check your internet connection
3. Regenerate API key from aistudio.google.com
4. Wait a few seconds and try again

### Problem: "No module named 'google.generativeai'"

**Solution:**
```bash
# Reinstall the package
pip uninstall google-generativeai
pip install google-generativeai
```

---

## 📁 Project Structure

```
vietnamese-history-chatbot/
├── app/
│   ├── main.py                    ← Flask application (core)
│   ├── templates/
│   │   └── index.html             ← Frontend HTML
│   └── static/
│       └── style.css              ← CSS styling
├── requirements.txt               ← Python dependencies
├── run.py                         ← Entry point (easier to run)
├── .env.example                   ← API key template
├── .env                           ← Your actual API key (NEVER commit!)
├── .gitignore                     ← Git ignore rules
└── README.md                      ← Full documentation
```

---

## 🔄 Update the Application

To update with latest changes:

```bash
# Save your changes
git add .
git commit -m "My changes"

# Pull latest updates
git pull origin main

# Reinstall dependencies (in case they changed)
pip install -r requirements.txt
```

---

## 🌐 Deploy to the Internet

### Deploy to Heroku (Free for small projects)

```bash
# 1. Create Heroku account at https://www.heroku.com
# 2. Install Heroku CLI
# 3. Login
heroku login

# 4. Create app
heroku create your-app-name

# 5. Set API key
heroku config:set GEMINI_API_KEY=your_key

# 6. Deploy
git push heroku main

# 7. Open your app
heroku open
```

### Deploy to Railway (Also free)

1. Go to https://railway.app
2. Connect your GitHub account
3. Import your repository
4. Add environment variables in dashboard
5. Deploy!

---

## 📞 Need Help?

1. **Check README.md** - Full documentation
2. **Check troubleshooting above** - Common issues
3. **Google the error** - Usually has a solution
4. **Check API status** - Visit https://aistudio.google.com
5. **Ask on Stack Overflow** - Tag: flask, python, gemini-api

---

## ✅ Verification Checklist

Before considering setup complete:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] .env file created with API key
- [ ] Application runs without errors
- [ ] Can access http://localhost:5000 in browser
- [ ] Can ask Vietnamese history questions
- [ ] Can see responses from AI

If all items are checked, you're ready to go! 🎉

---

## 🎓 Next Steps

Once setup is complete:

1. **Explore the code:**
   - Read `app/main.py` to understand Flask backend
   - Read `app/templates/index.html` to understand frontend
   - Read `app/static/style.css` to understand styling

2. **Customize:**
   - Change colors in style.css
   - Modify system prompt in main.py
   - Add new features!

3. **Deploy:**
   - Share your chatbot with the world
   - Deploy to Heroku/Railway/etc.
   - Get feedback from others

4. **Improve:**
   - Add voice input/output
   - Add image generation
   - Integrate with more APIs
   - Add more features

---

## 🙌 Congratulations!

You've successfully set up the Vietnamese History Chatbot! 🎉🇻🇳

Enjoy learning about Vietnamese history! 📚

---

**Made with ❤️ by Đinh Tin**

For issues, feedback, or contributions, visit the GitHub repository!
