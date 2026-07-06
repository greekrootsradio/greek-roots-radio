from flask import Flask, request, jsonify
from agent.brain import ask_ai
import threading
import time

app = Flask(__name__)

print("ZETA AUTONOMY CORE ONLINE")


# ---- BACKGROUND LOOP (SAFE) ----
def autonomy_loop():
    while True:
        print("[ZETA] autonomous heartbeat active")
        time.sleep(60)

threading.Thread(target=autonomy_loop, daemon=True).start()


@app.route("/")
def home():
    return "ZETA AUTONOMY ACTIVE"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    reply = ask_ai(data["message"], {})

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5050,
        debug=False
    )
