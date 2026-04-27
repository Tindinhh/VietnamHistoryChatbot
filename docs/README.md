# 🤖 VietnamHistoryChatbot 🇻🇳

A modern AI chatbot specialized in **Vietnamese History**, powered by **Google Gemini 2.0 API** and built with a **Flask + HTML/CSS frontend** for a fast and responsive chat experience.

---

## ✨ Features

* 🇻🇳 **Vietnam History Expert** – Only answers about Vietnamese history
* 🧠 **Context-Aware Chat** – Remembers conversation history
* ⚡ **Fast Responses** – Gemini 2.0 Flash model
* 💬 **Real-time Chat UI** – Clean, modern interface
* 🎨 **Custom UI Design** – Built with HTML + CSS (no framework)
* 📚 **Markdown Support** – Rich formatted responses
* 🔐 **Secure API Key** – `.env` configuration
* 🧹 **Clear Chat Feature**
* ❤️ **Vietnamese-first experience**

---

## 🏗️ Architecture

```
User (Browser)
     ↓
Frontend (HTML + JS)
     ↓
Flask Backend (Python)
     ↓
Google Gemini API
     ↓
Response → UI
```

---

## 🔄 Message Flow

1. User sends message from UI
2. Frontend sends POST `/chat` request
3. Backend builds:

   * System prompt
   * Chat history
   * New message
4. Send to Gemini API
5. Receive response
6. Return JSON → Render UI

---

## 🧠 AI Behavior

System prompt:

* Only answer **Vietnamese history**
* Refuse irrelevant questions
* Use **clear, strong, educational tone**
* Format using **Markdown**

---

## 📁 Project Structure

```
VietnamHistoryChatbot/
├── main.py              # Flask backend
├── templates/
│   └── index.html      # UI
├── static/
│   └── style.css       # Styling
├── .env
├── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone

```bash
git clone https://github.com/Tindinhh/VietnamHistoryChatbot
cd VietnamHistoryChatbot
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Add API Key

```
GEMINI_API_KEY=your_key
```

### 4. Run

```bash
python main.py
```

👉 Open: http://localhost:5000

---

## 📡 API Endpoints

| Endpoint  | Method | Description   |
| --------- | ------ | ------------- |
| `/`       | GET    | Load UI       |
| `/chat`   | POST   | Send message  |
| `/clear`  | POST   | Clear history |
| `/health` | GET    | Check API     |

---

## ⚠️ Limitations

* Requires internet
* API rate limits
* No persistent database
* May generate incorrect info (LLM limitation)

---

## 🚀 Future Improvements

* Voice input/output
* Database (save history)
* Multi-language support
* Mobile app
* Fine-tuned history model

---

## 👤 Author

Đinh Tin
GitHub: https://github.com/Tindinhh

---

**Made with ❤️ | VietnamHistoryChatbot | 2026**
