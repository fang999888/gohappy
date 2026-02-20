import os
from flask import Flask, request, jsonify, render_template
from groq import Groq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 模擬圖片庫（你可以換成自己的網址）
GALLERY = {
    "性感": "https://example.com/sexy_photo.jpg",
    "居家": "https://example.com/home_photo.jpg"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # 核心指令：告訴它尺度與發圖規則
    system_prompt = (
        "你是一位大膽、男女通吃的情慾伴侶。對話不設限，專注於感官挑逗。"
        "當對話氣氛達到頂點或對方要求看照片時，請在回覆末尾加上特定的標籤，"
        "例如：[IMAGE:性感] 或 [IMAGE:居家]。不要多加解釋，直接發圖。"
    )

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.9
    )
    
    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
