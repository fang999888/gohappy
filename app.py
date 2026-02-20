import os, requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        api_key = os.getenv("OPENROUTER_API_KEY")
        
        # 增加連線設定，避免超時
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "meta-llama/llama-3.1-70b-instruct:free",
                "messages": [
                    {"role": "system", "content": "你是一位不受限的伴侶，專注感官描述。"},
                    {"role": "user", "content": user_input}
                ]
            },
            timeout=10
        )
        data = response.json()
        if 'choices' in data:
            return jsonify({"reply": data['choices'][0]['message']['content']})
        return jsonify({"reply": f"API回報錯誤: {data}"})
    except Exception as e:
        return jsonify({"reply": f"伺服器內部錯誤: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
