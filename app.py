import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

API_KEY = "AQ.Ab8RN6Kgcrf6WuLR6VVvkXgoKV3H4TETN2Cb9EOWdH8sXSZ5ZQ"

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
else:
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if not model:
        return jsonify({"reply": "API Key सेट नहीं है!"})
    
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "कृपया कुछ लिखें।"})
    
    try:
        response = model.generate_content(user_message)
        bot_reply = response.text
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"एरर आ गया: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  
