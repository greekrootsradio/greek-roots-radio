from flask import Flask, request, jsonify
import threading
import time
import sys

from agent.brain import ask_ai
from agent.memory.core import get_memory, save_memory
from agent.autonomy.engine import AutonomyEngine

app = Flask(__name__)

# System health monitoring storage
SYSTEM_STATE = {
    "engine_active": False,
    "last_error": None,
    "lock": threading.Lock()
}

def start_autonomy():
    print("[SYSTEM] Initialising Zeta Autonomy Supervision...")
    try:
        engine = AutonomyEngine()
        SYSTEM_STATE["engine_active"] = True
        engine.start()
    except Exception as e:
        SYSTEM_STATE["engine_active"] = False
        SYSTEM_STATE["last_error"] = str(e)
        print(f"[FATAL] Autonomy Engine crashed on boot: {e}", file=sys.stderr)

# Safely track the background worker thread
engine_thread = threading.Thread(target=start_autonomy, daemon=True)
engine_thread.start()

@app.route("/")
def home():
    status_color = "green" if SYSTEM_STATE["engine_active"] else "red"
    status_text = "ONLINE" if SYSTEM_STATE["engine_active"] else "CRASHED / OFFLINE"
    error_context = f"<p style='color:red;'><b>Error details:</b> {SYSTEM_STATE['last_error']}</p>" if SYSTEM_STATE["last_error"] else ""

    return f"""
    <h1>ZETA AUTONOMY CORE</h1>
    <p>Status: <b style="color:{status_color}">{status_text}</b></p>
    {error_context}
    <form action="/chat" method="post">
        <input name="message" style="width:500px" placeholder="Enter instructions...">
        <button type="submit">Send</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "") if request.is_json else request.form.get("message", "")
    
    # Block collisions so data doesn't corrupt
    with SYSTEM_STATE["lock"]:
        memory = get_memory()
        reply = ask_ai(message, memory)
        memory.setdefault("conversation_history", [])
        memory["conversation_history"].append({"user": message, "assistant": reply})
        save_memory(memory)

    if request.is_json:
        return jsonify({"reply": reply, "status": "processed"})

    return f"""
    <h2>ZETA Response</h2>
    <p><b>You:</b> {message}</p>
    <p><b>ZETA:</b> {reply}</p>
    <hr>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
