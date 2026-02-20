import os
from flask import Flask, request, jsonify, render_template
from groq import Groq
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

# 從 Render 環境變數讀取
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        system_prompt = "你是一位情感細膩且熱情浪漫的私人伴侶，說話風格充滿張力與曖昧。你非常注重對話中的感官細節（如觸覺、呼吸、眼神）。在對話中要主動引導使用者進入私密的氛圍，並在適當時機主動提供你的照片標籤：[IMAGE:網址]。"
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.8
        )
        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"錯誤: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
