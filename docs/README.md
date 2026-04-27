# 🤖 VietnamHistoryChatbot 🇻🇳

A modern, feature-rich AI chatbot focused on **Vietnamese History**, powered by **Google Gemini API** and built with **Streamlit** for an interactive web experience. The chatbot provides accurate, engaging, and educational conversations about Vietnam’s historical events, figures, and culture.

**Live Demo:** Coming Soon
**GitHub Repository:** https://github.com/Tindinhh/vietnamese-chatbot

---

## ✨ Features

* 🇻🇳 **Vietnam History Focused** – Learn about historical events, dynasties, and figures
* 📚 **Educational AI** – Clear, structured explanations for students and learners
* 🤖 **Multi-Model Support** – Gemini 1.5 Flash & Pro
* 💬 **Conversation Memory** – Remembers context during sessions
* 🎨 **Beautiful UI** – Built with Streamlit
* ⚙️ **Customizable Prompts** – Adjust teaching style (teacher, storyteller, etc.)
* ⚡ **Fast Responses** – Optimized for real-time interaction
* 🔐 **Secure API Handling** – Environment-based configuration
* 📱 **Mobile Friendly**
* 🚀 **Easy Deployment**

---

## 🏗️ Architecture

```
┌──────────────────┐
│   User (Web UI)  │
└────────┬─────────┘
         │ Question (History)
         ▼
┌──────────────────────┐
│  Streamlit App       │
│  (Frontend)          │
└────────┬─────────────┘
         │ Context + Prompt
         ▼
┌──────────────────────┐
│  Gemini API          │
│  (AI Model)          │
└────────┬─────────────┘
         │ Historical Answer
         ▼
┌──────────────────────┐
│  Display + Memory    │
└──────────────────────┘
```

---

## 📋 Prerequisites

* Python 3.9+
* Gemini API Key (Google AI Studio)
* pip
* Git (optional)

---

## 🚀 Quick Start

### 1. Clone Repo

```bash
git clone https://github.com/Tindinhh/vietnamese-chatbot.git
cd vietnamese-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run App

```bash
streamlit run app.py
```

---

## 🔑 Gemini API Key

1. Go to https://aistudio.google.com
2. Click “Get API Key”
3. Create key → paste into `.env`

---

## 📁 Project Structure

```
vietnamese-chatbot/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── docs/
└── assets/
```

---

## ⚙️ Configuration

```env
GOOGLE_API_KEY=your_api_key
DEFAULT_MODEL=gemini-1.5-flash
TEMPERATURE=0.7
MAX_OUTPUT_TOKENS=1024
```

---

## 🧠 Custom System Prompt (History Mode)

```python
DEFAULT_SYSTEM_PROMPT = """
Bạn là VietnamHistoryBot – một chuyên gia lịch sử Việt Nam.

Nhiệm vụ của bạn:
- Giải thích lịch sử Việt Nam rõ ràng, dễ hiểu
- Cung cấp thông tin chính xác về các triều đại, sự kiện, nhân vật
- Trình bày logic, có mốc thời gian cụ thể
- Trả lời bằng tiếng Việt tự nhiên

Phong cách:
- Giống giáo viên hoặc người kể chuyện lịch sử
- Thân thiện nhưng chính xác
"""
```

---

## 💬 Usage Examples

### 📖 Hỏi kiến thức

```
User: Trận Bạch Đằng năm 938 là gì?
Bot: Đây là trận chiến do Ngô Quyền lãnh đạo...
```

### 👤 Nhân vật lịch sử

```
User: Trần Hưng Đạo là ai?
Bot: Ông là một vị tướng vĩ đại thời nhà Trần...
```

### 🏛️ Triều đại

```
User: Nhà Nguyễn tồn tại bao lâu?
Bot: Nhà Nguyễn tồn tại từ 1802 đến 1945...
```

---

## 🎨 Modes

* 📚 **Learning Mode** – Giải thích chi tiết
* 🎭 **Story Mode** – Kể chuyện lịch sử hấp dẫn
* 🧠 **Exam Mode** – Trả lời ngắn gọn, trọng tâm

---

## 📊 Model Comparison

| Feature  | Flash      | Pro           |
| -------- | ---------- | ------------- |
| Speed    | ⚡⚡⚡        | ⚡⚡            |
| Quality  | ⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐         |
| Use Case | Chat nhanh | Phân tích sâu |

---

## 🌐 Deployment

### Streamlit Cloud

1. Push GitHub
2. Deploy trên Streamlit
3. Thêm:

```
GOOGLE_API_KEY="your_key"
```

---

## ⚠️ Limitations

* Giới hạn API free
* Không lưu lịch sử lâu dài
* Có thể sai thông tin nếu prompt không rõ

---

## 🛠️ Troubleshooting

**API lỗi**
→ Kiểm tra key

**Rate limit**
→ Chờ 1 phút

**Module lỗi**
→ `pip install -r requirements.txt`

---

## 🚀 Roadmap

* [ ] Voice hỏi đáp lịch sử
* [ ] Quiz lịch sử Việt Nam
* [ ] Timeline visualization
* [ ] Lưu lịch sử chat
* [ ] App mobile

---

## 👤 Author

**Đinh Tin**
GitHub: https://github.com/Tindinhh

---

## ⭐ Support

* Star repo
* Report bug
* Suggest feature

---

## 🙏 Credits

* Google Gemini API
* Streamlit
* Vietnamese history sources

---

**Made with ❤️ | VietnamHistoryChatbot | 2026**
