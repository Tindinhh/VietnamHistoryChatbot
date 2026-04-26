# 🇻🇳 Sử Việt Toàn Thư - Vietnamese History Chatbot

**Một chatbot chuyên gia lịch sử Việt Nam được xây dựng bằng Flask + Gemini AI**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0+-red?logo=flask)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20API-gold?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

[🚀 Quick Start](#quick-start) • [📋 Features](#features) • [🛠️ Setup](#setup) • [📖 Usage](#usage) • [🌐 Deploy](#deployment)

</div>

---

## ✨ Features

- ✅ **100% Tiếng Việt** - Giao diện & hỗ trợ hoàn toàn tiếng Việt
- 🤖 **Gemini AI** - Sử dụng Google Gemini 2.0 Flash (SOTA model)
- 🎨 **Beautiful UI** - Giao diện modern, responsive với Flask + HTML/CSS
- 📚 **Lịch sử VN** - Chuyên gia về các triều đại, danh nhân, sự kiện lịch sử
- 🚫 **Smart Rejection** - Tự động từ chối câu hỏi không liên quan lịch sử
- 💾 **Conversation Memory** - Nhớ lịch sử trò chuyện trong session
- 🔐 **Secure** - API key được bảo vệ bằng .env file
- 📱 **Responsive** - Hoạt động tốt trên desktop, tablet, mobile
- ⚡ **Fast** - Response time nhanh với Gemini API

---

## 🎯 Use Cases

1. **Học tập lịch sử** - Giải thích về các triều đại, vua chúa
2. **Tra cứu sự kiện** - Tìm hiểu sự kiện lịch sử quan trọng
3. **Nghiên cứu** - Tìm hiểu về danh nhân lịch sử Việt Nam
4. **Văn hoá** - Khám phá di sản văn hoá Việt Nam
5. **Tiếng Việt** - Cơ hội sử dụng tiếng Việt chính xác

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/[your-username]/vietnamese-history-chatbot.git
cd vietnamese-history-chatbot
```

### 2️⃣ Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Get Gemini API Key

1. Visit: **https://aistudio.google.com/app/apikey**
2. Click "Create API Key"
3. Copy your API key

### 5️⃣ Setup .env File

```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env and paste your API key
# GEMINI_API_KEY=your_api_key_here
```

### 6️⃣ Run Application

```bash
python app/main.py
```

**Output:**
```
==============================================================
🇻🇳 SỬ VIỆT TOÀN THƯ - Vietnamese History Chatbot
==============================================================
✅ Flask app starting...
📍 Visit: http://localhost:5000
==============================================================
```

👉 **Open browser:** `http://localhost:5000`

---

## 📂 Project Structure

```
vietnamese-history-chatbot/
├── app/
│   ├── main.py                 # Flask application
│   ├── templates/
│   │   └── index.html          # HTML UI
│   └── static/
│       └── style.css           # CSS styling
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
└── .git/
```

---

## 🔧 Setup Details

### Environment Variables

Create `.env` file in project root:

```
GEMINI_API_KEY=AIzaSy_xxxxxxxxxxxxxxxxxxxxxxxx
```

**⚠️ IMPORTANT:** Never commit `.env` file to Git!

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0+ | Web framework |
| google-generativeai | 0.4+ | Gemini API |
| python-dotenv | 1.0+ | Env variables |
| gunicorn | 21.2+ | Production server |

---

## 💬 Usage

### Chat Interface

1. **Type your question:** Nhập câu hỏi về lịch sử VN
2. **Press Enter or Click Send:** Gửi câu hỏi
3. **Wait for response:** AI sẽ trả lời trong vài giây

### Example Questions

```
✅ "Ai là vua Quang Trung?"
✅ "Nhà Trần có bao nhiêu vị vua?"
✅ "Tây Sơn là gì?"
✅ "Trần Hưng Đạo chống Mông Nguyên như thế nào?"
✅ "Di sản văn hoá Việt Nam gồm những gì?"

❌ "Thời tiết hôm nay như thế nào?" (Không liên quan lịch sử)
❌ "Cách nấu phở" (Không liên quan lịch sử)
```

### Features

| Feature | Description |
|---------|-------------|
| **Clear History** | Xóa lịch sử trò chuyện |
| **Status Indicator** | Hiển thị trạng thái kết nối |
| **Markdown Support** | AI trả lời với formatting đẹp |
| **Responsive Design** | Hoạt động trên mọi thiết bị |
| **Auto-scroll** | Tự động cuộn đến tin nhắn mới |

---

## 🤖 AI System

### System Instruction

Bot được lập trình với hướng dẫn chi tiết:

```
1. ✅ CHỈ trả lời câu hỏi liên quan LỊCH SỬ VIỆT NAM
2. ❌ TỪ CHỐI trả lời nếu câu hỏi KHÔNG liên quan
3. 📚 Chuyên sâu về: Triều đại, Vua chúa, Sự kiện, Di sản
4. 💬 Phong cách: Hào hùng, tôn trọng, sử dụng Markdown
5. 🚫 Cấm: Spam, phiếm luận, nội dung không liên quan
```

### Model Configuration

```python
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",    # Latest model
    system_instruction=SYSTEM_INSTRUCTION
)

generation_config = {
    "temperature": 0.7,               # Balance: creative + consistent
    "top_p": 0.95,                    # Diversity
    "max_output_tokens": 1024,        # Response length
}
```

---

## 📡 API Endpoints

### POST /chat

Send a message to the chatbot.

**Request:**
```json
{
  "message": "Ai là vua Quang Trung?"
}
```

**Response (Success):**
```json
{
  "success": true,
  "reply": "Quang Trung (1753-1792)...",
  "history_length": 2
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Lỗi xác thực API key"
}
```

### POST /clear

Clear conversation history.

**Request:**
```bash
POST /clear
```

**Response:**
```json
{
  "success": true,
  "message": "Lịch sử trò chuyện đã xóa"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "model": "gemini-2.0-flash",
  "api_configured": true
}
```

---

## 🚀 Deployment

### Option 1: Heroku

```bash
# 1. Install Heroku CLI
# 2. Create Heroku app
heroku create your-app-name

# 3. Set environment variables
heroku config:set GEMINI_API_KEY=your_key

# 4. Create Procfile
echo "web: gunicorn app.main:app" > Procfile

# 5. Deploy
git push heroku main
```

### Option 2: Railway

```bash
# 1. Connect GitHub repo to Railway
# 2. Add environment variable in Railway dashboard
# 3. Deploy automatically!
```

### Option 3: PythonAnywhere

```bash
# 1. Upload files to PythonAnywhere
# 2. Create virtual environment
# 3. Configure web app
# 4. Set environment variables in WSGI
# 5. Reload app
```

### Option 4: Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
```

```bash
# Build & Run
docker build -t history-chatbot .
docker run -e GEMINI_API_KEY=your_key -p 5000:5000 history-chatbot
```

---

## 🔐 Security

### API Key Protection

```bash
✅ Store API key in .env (never in code)
✅ Add .env to .gitignore
✅ Use environment variables in production
❌ NEVER commit .env to Git
❌ NEVER share API key publicly
```

### Input Validation

- All user inputs are validated
- HTML is sanitized with DOMPurify
- Error messages don't expose sensitive info

---

## 🐛 Troubleshooting

### Issue: "API Key not found"

```
Solution:
1. Check .env file exists
2. Verify GEMINI_API_KEY=... is set correctly
3. Regenerate key from https://aistudio.google.com
```

### Issue: "Connection Error"

```
Solution:
1. Check internet connection
2. Verify API is accessible
3. Check if API key is valid
4. Try using gemini-pro model instead
```

### Issue: "Slow Response"

```
Solution:
1. Use gemini-2.0-flash (faster than pro)
2. Reduce max_output_tokens
3. Clear conversation history periodically
```

### Issue: "Module not found"

```
Solution:
1. Activate virtual environment
2. pip install -r requirements.txt
3. Verify Python version 3.8+
```

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| **Startup Time** | ~2-3 seconds |
| **Response Time** | 1-3 seconds |
| **Max Token Length** | 1024 tokens |
| **Rate Limit** | ~500 req/min (free tier) |
| **Memory Usage** | ~100MB |

---

## 🎓 Learning Value

This project teaches:

✅ Flask web framework
✅ REST API design
✅ Gemini API integration
✅ Frontend: HTML, CSS, JavaScript
✅ Backend: Python, async programming
✅ Environment management (.env)
✅ Deployment & DevOps basics
✅ UI/UX design
✅ Git & version control

---

## 🤝 Contributing

Contributions welcome! 

```bash
1. Fork repository
2. Create feature branch: git checkout -b feature/amazing
3. Commit: git commit -m "Add amazing feature"
4. Push: git push origin feature/amazing
5. Pull Request
```

---

## 📄 License

MIT License - see LICENSE file

---

## 👤 Author

**Đinh Tin**

- GitHub: [@Tindinhh](https://github.com/Tindinhh)
- LinkedIn: [Tinn Đinh](https://www.linkedin.com/in/tinn-đinh-3523711ab/)

---

## 📚 Resources

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Dotenv Guide](https://python-dotenv.readthedocs.io/)
- [Marked.js (Markdown)](https://marked.js.org/)
- [DOMPurify (Security)](https://github.com/cure53/DOMPurify)

---

## 🎉 Support

Have questions?

- 📖 Check [Issues](https://github.com/Tindinhh/vietnamese-history-chatbot/issues)
- 💬 Create a Discussion
- 📧 Email: [your-email@example.com]

---

<div align="center">

**⭐ If you like this project, please star it! ⭐**

Made with ❤️ by Đinh Tin | Powered by Google Gemini API

🇻🇳 **Tự hào là người Việt - Lịch sử nước ta** 🇻🇳

</div>
