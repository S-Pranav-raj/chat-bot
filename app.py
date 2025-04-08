from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Setup Gemini model
def setup_gemini(api_key, model_name='models/gemini-1.5-pro-001'):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

# Replace this with your actual Gemini API key
API_KEY = "AIzaSyDihlZ6QQ3FyCb7vKWPF21J7cNMkqaZCxQ"
model = setup_gemini(API_KEY)

prompt = (
    "Write a complete, correct Python function to check if a number is prime. "
    "Only return code, no explanation."
)
response = model.generate_content(prompt)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    try:
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"}), 500
    
    

if __name__ == "__main__":
    app.run(debug=True)
