# 🤖 Vietnamese AI Chatbot with Gemini API

A modern, feature-rich chatbot application powered by **Google Gemini API**, built with **Streamlit** for a beautiful, interactive web interface. Fully supports Vietnamese language with natural conversation abilities.

**Live Demo:** [Streamlit Cloud Link - Coming Soon]  
**GitHub Repository:** [https://github.com/Tindinhh/vietnamese-chatbot](https://github.com/Tindinhh/vietnamese-chatbot)

---

## ✨ Features

- 🇻🇳 **100% Vietnamese Support** - Native support for Vietnamese conversations
- 🤖 **Multi-Model Support** - Switch between Gemini 1.5 Flash & Pro models
- 💬 **Conversation Memory** - Bot remembers chat history within sessions
- 🎨 **Beautiful UI** - Clean, responsive Streamlit interface
- ⚙️ **Customizable Prompts** - Adjust bot personality and behavior
- ⚡ **Fast & Efficient** - Real-time responses powered by Gemini
- 🔐 **Secure API Key Management** - Environment variable-based configuration
- 📱 **Mobile Friendly** - Works on desktop and mobile devices
- 🚀 **Easy Deployment** - One-click deployment to Streamlit Cloud

---

## 🏗️ Architecture

```
┌──────────────────┐
│   User (Web UI)  │
└────────┬─────────┘
         │ User Input
         ▼
┌──────────────────────┐
│  Streamlit App       │
│  (Frontend)          │
└────────┬─────────────┘
         │ Prompt + Context
         ▼
┌──────────────────────┐
│  Gemini 1.5 API      │
│  (AI Model)          │
└────────┬─────────────┘
         │ Response
         ▼
┌──────────────────────┐
│  Display Response    │
│  Save to History     │
└──────────────────────┘
```

### Message Processing Flow

1. **User Input** → Người dùng nhập tin nhắn vào Streamlit UI
2. **Save History** → Tin nhắn lưu vào session state
3. **Build Context** → Toàn bộ lịch sử trò chuyện được build
4. **Send to Gemini** → Context + system prompt gửi tới API
5. **Generate Response** → Gemini tạo response tiếng Việt
6. **Display & Save** → Hiển thị kết quả và lưu vào memory

---

## 📋 Prerequisites

- Python 3.9+
- Google Gemini API Key (free tier available at [Google AI Studio](https://aistudio.google.com))
- pip (Python package manager)
- Git (optional, for cloning)

---

## 🚀 Quick Start (4 Steps)

### Step 1: Clone Repository
```bash
git clone https://github.com/Tindinhh/vietnamese-chatbot.git
cd vietnamese-chatbot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# GOOGLE_API_KEY=your_actual_api_key_here
```

Or set directly in terminal:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### Step 4: Run Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

---

## 🔑 Getting Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click **"Get API Key"** button
3. Create a new API key
4. Copy the key and paste into `.env` file

**Free tier includes:** 15 requests per minute, 1500 requests per day

---

## 📁 Project Structure

```
vietnamese-chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── docs/                 # Additional documentation
│   ├── setup.md          # Detailed setup guide
│   ├── deployment.md     # Deployment instructions
│   └── examples.md       # Usage examples
└── assets/               # Images, screenshots
    └── demo.png          # Demo screenshot
```

---

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Required
GOOGLE_API_KEY=your_api_key_here

# Optional
DEFAULT_MODEL=gemini-1.5-flash        # or gemini-1.5-pro
TEMPERATURE=0.7                       # 0.0-1.0 (higher = more creative)
MAX_OUTPUT_TOKENS=1024                # Response length limit
```

### Customizing System Prompt

Edit the default system prompt in `app.py`:

```python
DEFAULT_SYSTEM_PROMPT = """
Bạn là TinBot, một trợ lý AI thân thiện và hữu ích.
Bạn nói tiếng Việt một cách tự nhiên và mục tiêu là giúp người dùng.
Hãy luôn lịch sự, tích cực, và cố gắng hết sức để trả lời câu hỏi.
"""
```

---

## 💬 Usage Examples

### Example 1: Learning Assistance
```
User: Giải thích cho tôi về Machine Learning là gì?
Bot: Machine Learning là một lĩnh vực của AI...
```

### Example 2: Coding Help
```
User: Cách để filter list trong Python?
Bot: Bạn có thể sử dụng list comprehension hoặc filter()...
```

### Example 3: Creative Writing
```
User: Viết một bài thơ ngắn về mùa xuân
Bot: [Generates Vietnamese poem]
```

---

## 🎨 Customization

### Change Bot Personality

Modify the system prompt via sidebar:
- Default: Friendly, helpful AI assistant
- Expert Mode: Technical, professional responses
- Creative Mode: Imaginative, artistic responses
- Learning Mode: Educational, detailed explanations

### Switch Models

Use the sidebar dropdown to choose:
- **Gemini 1.5 Flash** ⚡ - Faster, cheaper (recommended for chat)
- **Gemini 1.5 Pro** 🚀 - More powerful, better quality

---

## 📊 Model Comparison

| Feature | Flash | Pro |
|---------|-------|-----|
| Speed | ⚡⚡⚡ Fast | ⚡⚡ Medium |
| Quality | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Cost | 💰 Cheaper | 💰💰 Higher |
| Best For | Real-time chat | Complex tasks |

---

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Push code to GitHub:
```bash
git add .
git commit -m "Deploy Vietnamese Chatbot"
git push origin main
```

2. Go to [Streamlit Cloud](https://share.streamlit.io)

3. Click "New app" and select your repository

4. Add secrets:
   - Go to App settings → Secrets
   - Paste your API key:
   ```
   GOOGLE_API_KEY = "your_api_key"
   ```

5. Deploy! 🚀

### Deploy with Docker

```bash
# Build image
docker build -t vietnamese-chatbot .

# Run container
docker run -e GOOGLE_API_KEY="your_key" -p 8501:8501 vietnamese-chatbot
```

### Deploy to AWS / GCP

See `docs/deployment.md` for cloud deployment guides.

---

## ⚠️ Known Limitations

- **Rate Limiting**: Free tier has 15 req/min limit
- **Session Memory**: Chat history resets when app restarts
- **Offline Mode**: Requires internet connection
- **Hallucinations**: LLM may occasionally generate incorrect info
- **Cost at Scale**: Pricing increases with high usage

---

## 🛠️ Troubleshooting

### Issue: "Invalid API Key"
```
Solution:
1. Verify API key is correct
2. Check .env file formatting
3. Restart app after changing .env
4. Generate new key from Google AI Studio
```

### Issue: "Rate limit exceeded"
```
Solution:
1. Free tier limited to 15 req/min
2. Wait a minute before sending new message
3. Consider upgrading to paid tier
4. Batch queries if possible
```

### Issue: "Module not found"
```
Solution:
1. Install all requirements: pip install -r requirements.txt
2. Use Python 3.9+
3. Use virtual environment: python -m venv venv
4. Activate: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
```

### Issue: "Vietnamese text not displaying"
```
Solution:
1. Ensure UTF-8 encoding in terminal
2. Update system fonts
3. Check browser supports Vietnamese
4. Restart Streamlit app
```

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| Avg Response Time | ~2-3 seconds |
| Token Limit | 1,000,000 tokens/month (free) |
| Concurrent Users | Unlimited (Cloud) |
| Uptime | 99.9% (Streamlit Cloud) |

---

## 🔐 Security Best Practices

✅ **Do's:**
- Store API key in `.env` file
- Never commit `.env` to Git
- Use `.gitignore` to exclude sensitive files
- Regenerate keys if compromised

❌ **Don'ts:**
- Share API key publicly
- Hardcode keys in source code
- Use same key across projects
- Store keys in plain text

---

## 🚀 Future Roadmap

- [ ] Voice input/output support
- [ ] Image upload capability
- [ ] Conversation export (JSON/PDF)
- [ ] Conversation history persistent storage
- [ ] Multi-user authentication
- [ ] Rate limiting dashboard
- [ ] Fine-tuned Vietnamese model
- [ ] Mobile app (React Native)
- [ ] Browser extension
- [ ] Slack integration

---

## 📚 Learning Resources

### Gemini API Documentation
- [Google Generative AI Docs](https://ai.google.dev)
- [Gemini API Reference](https://ai.google.dev/api/python)
- [Prompt Engineering Guide](https://ai.google.dev/docs/prompt_engineering)

### Streamlit Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)

### Related Projects
- [LangChain](https://github.com/langchain-ai/langchain) - LLM framework
- [Ollama](https://ollama.ai) - Local LLM
- [LlamaIndex](https://www.llamaindex.ai) - RAG systems

---

## 🤝 Contributing

Contributions are welcome! 

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see `LICENSE` file for details.

---

## 👤 Author

**Đinh Tin**
- GitHub: [@Tindinhh](https://github.com/Tindinhh)
- LinkedIn: [Tinn Đinh](https://www.linkedin.com/in/tinn-đinh-3523711ab/)
- Email: tindinhh@example.com

---

## ⭐ Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting improvements
- 📢 Sharing with others

---

## 🙏 Acknowledgments

- Google Gemini team for the amazing API
- Streamlit for the beautiful framework
- Community contributors and users
- freeCodeCamp Python course
- Google Gemini Certification program

---

## 📞 Contact & Support

- **Issues/Bugs**: Open GitHub issue
- **Questions**: Start a GitHub discussion
- **Feedback**: Email or LinkedIn message
- **Collaborations**: Always open to partnerships!

---

**Made with ❤️ by Đinh Tin | 2026**

*Last Updated: April 26, 2026*
