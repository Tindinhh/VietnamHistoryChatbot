import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

# ================== GEMINI CONFIG ==================
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

# Init client (SDK mới)
client = genai.Client(api_key=API_KEY)

# 👉 MODEL MỚI (fix lỗi 404)
MODEL_NAME = "gemini-2.0-flash"

# ================== SYSTEM PROMPT ==================
SYSTEM_INSTRUCTION = """
Bạn là 'Sử Việt Toàn Thư', một chuyên gia lịch sử Việt Nam.

📋 HƯỚNG DẪN:
1. ✅ CHỈ trả lời về lịch sử Việt Nam
2. ❌ TỪ CHỐI nếu không liên quan
3. 📚 Kiến thức: triều đại, vua, chiến tranh, văn hoá
4. 💬 Văn phong: hào hùng, Markdown đẹp
5. 🚫 Không lan man, không spam

CÁCH TỪ CHỐI:
"❌ Xin lỗi, tôi chỉ chuyên về lịch sử Việt Nam. Bạn có câu hỏi nào về lịch sử nước ta không?"
"""

# ================== MEMORY ==================
conversation_history = []

MAX_HISTORY = 20

# ================== ROUTES ==================

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history

    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "success": False,
                "error": "Vui lòng nhập câu hỏi"
            }), 400

        # ===== Build messages =====
        messages = []

        # system prompt (SDK mới nên cho vào đầu luôn)
        messages.append({
            "role": "user",
            "parts": [{"text": SYSTEM_INSTRUCTION}]
        })

        # history
        for msg in conversation_history:
            messages.append({
                "role": msg["role"],
                "parts": [{"text": msg["content"]}]
            })

        # user mới
        messages.append({
            "role": "user",
            "parts": [{"text": user_message}]
        })

        # ===== CALL API =====
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=messages,
            config={
                "temperature": 0.7,
                "top_p": 0.95,
                "max_output_tokens": 2048,
            }
        )

        bot_reply = response.text if response.text else "❌ Không có phản hồi"

        # ===== SAVE HISTORY =====
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        conversation_history.append({
            "role": "assistant",   # 🔥 FIX role chuẩn
            "content": bot_reply
        })

        # limit history
        if len(conversation_history) > MAX_HISTORY:
            conversation_history = conversation_history[-MAX_HISTORY:]

        return jsonify({
            "success": True,
            "reply": bot_reply
        })

    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error: {error_msg}")

        if "API_KEY" in error_msg:
            msg = "❌ Lỗi API Key"
        elif "quota" in error_msg.lower():
            msg = "❌ Hết quota API"
        elif "not found" in error_msg.lower():
            msg = "❌ Model không tồn tại (check lại model)"
        else:
            msg = "❌ Server lỗi, thử lại sau"

        return jsonify({
            "success": False,
            "error": msg
        }), 500


@app.route('/clear', methods=['POST'])
def clear_history():
    global conversation_history
    conversation_history = []

    return jsonify({
        "success": True,
        "message": "Đã xoá lịch sử"
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "model": MODEL_NAME,
        "api_ready": bool(API_KEY)
    })


# ================== RUN ==================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🇻🇳 SỬ VIỆT TOÀN THƯ")
    print("="*60)
    print("✅ API Ready")
    print("🔥 Model:", MODEL_NAME)
    print("🌐 http://localhost:5000")
    print("="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)  