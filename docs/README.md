# 🤖 VietnamHistoryChatbot 🇻🇳

A modern, feature-rich AI chatbot focused on **Vietnamese History**, powered by **Google Gemini API**, built with **Streamlit** for a beautiful and interactive web interface. This chatbot is designed to help users explore, learn, and understand Vietnamese history in a natural, conversational way.

It can explain historical events, analyze timelines, describe important figures, and even compare dynasties — all in fluent Vietnamese.

**Live Demo:** Coming Soon
**GitHub Repository:** [https://github.com/Tindinhh/vietnamese-chatbot](https://github.com/Tindinhh/vietnamese-chatbot)

---

## ✨ Features

* 🇻🇳 **Vietnamese History Specialist** – Focused entirely on Vietnam history
* 📚 **Educational AI** – Structured explanations for students and learners
* 🧠 **Context-Aware Responses** – Understands previous conversation
* 🤖 **Multi-Model Support** – Gemini Flash & Pro
* 💬 **Conversation Memory** – Session-based chat history
* 🎨 **Modern UI** – Built with Streamlit
* ⚙️ **Customizable Prompts** – Change teaching style
* ⚡ **Fast Response Time** – Real-time AI replies
* 🔐 **Secure API Key Handling**
* 📱 **Responsive Design**

---

## 🏗️ Architecture

```
User → Streamlit UI → Context Builder → Gemini API → Response → Display + Memory
```

### Flow Detail

1. User enters a history question
2. App stores it in session state
3. Builds full conversation context
4. Sends request to Gemini API
5. AI generates answer
6. Response displayed and saved

---

## 📚 Advanced Capabilities

* 🧭 **Timeline Analysis** – Ask by historical period
* 🔎 **Cause–Effect Breakdown** – Analyze events deeply
* 🧑‍🏫 **Adaptive Teaching** – Adjusts difficulty level
* 📖 **Storytelling Mode** – Explain like a history narrative
* 🎯 **Exam Mode** – Short, key-point answers
* 🧠 **Memory Context** – Follow-up questions handled smoothly

---

## 💬 Usage Examples

### Basic Question

User: Trận Bạch Đằng 938 là gì?

### Deep Analysis

User: Vì sao nhà Hồ thất bại?

### Comparison

User: So sánh nhà Trần và nhà Lý

### Timeline

User: Lịch sử Việt Nam từ 938 đến 1945

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

## 🚀 Setup

```bash
git clone https://github.com/Tindinhh/vietnamese-chatbot.git
cd vietnamese-chatbot
pip install -r requirements.txt
cp .env.example .env
```

Add API key:

```
GOOGLE_API_KEY=your_key
```

Run app:

```bash
streamlit run app.py
```

---

## ⚙️ Configuration

```env
DEFAULT_MODEL=gemini-1.5-flash
TEMPERATURE=0.7
MAX_OUTPUT_TOKENS=1024
```

---

## 🧠 System Prompt (History Bot)

```python
Bạn là VietnamHistoryBot.
Bạn chuyên về lịch sử Việt Nam.
Trả lời rõ ràng, có mốc thời gian.
Giải thích dễ hiểu như giáo viên.
```

---

## 📊 Model Comparison

| Feature | Flash | Pro           |
| ------- | ----- | ------------- |
| Speed   | Fast  | Medium        |
| Quality | Good  | Very High     |
| Use     | Chat  | Deep analysis |

---

## ⚠️ Limitations

* API free có giới hạn
* Không lưu lâu dài
* Có thể sai nếu prompt không rõ

---

## 🛠️ Troubleshooting

**API lỗi** → kiểm tra key
**Rate limit** → chờ
**Module lỗi** → cài lại requirements

---

## 🚀 Roadmap

* Voice hỏi đáp
* Quiz lịch sử
* Timeline UI
* Mobile app

---

## 👤 Author

Đinh Tin
GitHub: [https://github.com/Tindinhh](https://github.com/Tindinhh)

---

## ⭐ Support

* Star repo
* Report bug
* Suggest feature

---

## 🙏 Credits

* Google Gemini
* Streamlit

---

**Made with ❤️ | VietnamHistoryChatbot | 2026**
