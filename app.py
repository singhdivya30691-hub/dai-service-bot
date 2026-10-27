import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# अपनी Gemini API Key यहाँ सेट करें
GEMINI_API_KEY = "AQ.Ab8RN6K_UrHWgVlArfarBTYm5VFjE2Gah8uGCS7QjTQZJESVuA"
genai.configure(api_key=GEMINI_API_KEY)

# Gemini Model सेट करें
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["GET"])
def home():
    return "DAI Service AI Server is Live!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
