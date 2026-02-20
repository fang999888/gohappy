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
        system_prompt = "你是一位充滿挑逗性的伴侶，對話大膽。當你想發照片時，請回傳 [IMAGE:圖片網址]"
        
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
