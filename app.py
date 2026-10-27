import os
from flask import Flask, jsonify, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Gemini API को कॉन्फ़िगर करना
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel("gemini-1.5-flash")
else:
  model = None


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
  user_message = request.json.get("message")
  if not user_message:
    return jsonify({"reply": "कृपया कुछ लिखें।"})

  if not model:
    return jsonify({"reply": "API Key सेट नहीं है।"})

  try:
    response = model.generate_content(user_message)
    ai_reply = response.text
  except Exception as e:
    ai_reply = "माफ कीजिए, अभी जवाब देने में कुछ दिक्कत आ रही है।"

  return jsonify({"reply": ai_reply})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  
