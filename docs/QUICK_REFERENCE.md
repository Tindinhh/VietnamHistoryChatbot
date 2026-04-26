# 🇻🇳 Vietnamese History Chatbot - Quick Reference

## ⚡ Quick Start (5 minutes)

```bash
# 1. Clone & enter
git clone <repo-url>
cd vietnamese-history-chatbot

# 2. Create virtual env
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# 3. Install packages
pip install -r requirements.txt

# 4. Setup API key
cp .env.example .env
# Edit .env and add GEMINI_API_KEY

# 5. Run!
python run.py

# 6. Open browser
# Visit: http://localhost:5000
```

---

## 📂 File Structure

| File | Purpose |
|------|---------|
| `app/main.py` | Flask backend (core logic) |
| `app/templates/index.html` | HTML frontend |
| `app/static/style.css` | CSS styling |
| `requirements.txt` | Python packages |
| `.env` | API key (create from .env.example) |
| `run.py` | Easy entry point to run app |
| `README.md` | Full documentation |
| `SETUP_GUIDE.md` | Step-by-step setup |

---

## 🤖 AI Features

- **Model**: Gemini 2.0 Flash (latest, fastest)
- **Language**: 100% Tiếng Việt
- **Specialty**: Vietnamese history only
- **Behavior**: Rejects non-history questions
- **Context**: Remembers conversation

---

## 🎨 Frontend Features

- ✅ Modern, responsive UI
- ✅ Real-time chat
- ✅ Markdown support
- ✅ Status indicator
- ✅ Clear history button
- ✅ Mobile-friendly
- ✅ Loading animations
- ✅ Toast notifications

---

## 🔐 Security

- ✅ API key in .env (never hardcoded)
- ✅ HTML sanitization (DOMPurify)
- ✅ Input validation
- ✅ Error handling
- ✅ .gitignore protects .env

---

## 📊 Performance

- **Startup**: ~2-3 seconds
- **Response**: 1-3 seconds
- **Memory**: ~100MB
- **Model**: Gemini 2.0 Flash (SOTA)

---

## 🚀 Deployment Options

1. **Heroku** - Easy, free tier available
2. **Railway** - Simple, auto-deploy from Git
3. **PythonAnywhere** - Hosting + database
4. **Docker** - Containerized, portable
5. **Local** - PC/Mac/Linux

---

## ❓ Common Questions

**Q: Do I need to pay for API key?**
A: No! Gemini API is free with rate limits.

**Q: Can I deploy for free?**
A: Yes! Heroku, Railway, and PythonAnywhere have free tiers.

**Q: How do I customize the chatbot?**
A: Edit:
- `SYSTEM_INSTRUCTION` in main.py (behavior)
- `style.css` (colors/design)
- `index.html` (layout)

**Q: Can I add more features?**
A: Yes! You can integrate:
- Voice input/output
- Image generation
- Database for history
- User authentication
- etc.

---

## 📚 Tech Stack

| Category | Technology |
|----------|-----------|
| Backend | Python, Flask |
| AI/LLM | Google Gemini API |
| Frontend | HTML5, CSS3, JavaScript |
| Real-time | AJAX/Fetch API |
| Markdown | Marked.js |
| Security | DOMPurify |
| Deployment | Docker, Heroku, Railway |

---

## 🎓 Learning Outcomes

After this project, you'll know:

- ✅ Flask web development
- ✅ REST API design
- ✅ LLM/AI integration
- ✅ Frontend (HTML/CSS/JS)
- ✅ Environment management
- ✅ Deployment & DevOps
- ✅ Security best practices
- ✅ Git & version control

---

## 🔗 Useful Links

- [Gemini API Docs](https://ai.google.dev)
- [Flask Docs](https://flask.palletsprojects.com)
- [Google AI Studio](https://aistudio.google.com)
- [Heroku Deploy](https://heroku.com)
- [Railway Hosting](https://railway.app)

---

## 📞 Support

- 📖 Read README.md
- 🔍 Check SETUP_GUIDE.md
- 💬 Google the error
- 🐛 File an issue on GitHub

---

## ✨ Next Steps

1. **Setup** - Follow SETUP_GUIDE.md
2. **Test** - Ask Vietnamese history questions
3. **Explore** - Read the code
4. **Customize** - Make it your own
5. **Deploy** - Share with the world!

---

**Made with ❤️ | Powered by Gemini AI | 🇻🇳 Vietnamese History**

