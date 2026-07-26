from flask import Flask, request, jsonify

import threading
import time

from agent.brain import ask_ai
from agent.memory.core import get_memory, save_memory
from agent.autonomy.engine import AutonomyEngine

app = Flask(__name__)

print("ZETA AUTONOMY CORE ONLINE")


# -------------------------------------------------
# AUTONOMY ENGINE
# -------------------------------------------------

def start_autonomy():

    print("ZETA Autonomy Engine Started")

    engine = AutonomyEngine()
    engine.start()


threading.Thread(
    target=start_autonomy,
    daemon=True
).start()


# -------------------------------------------------
# HEARTBEAT
# -------------------------------------------------

def heartbeat():

    while True:

        print("[ZETA] autonomous heartbeat active")

        time.sleep(60)


threading.Thread(
    target=heartbeat,
    daemon=True
).start()


# -------------------------------------------------
# HOME
# -------------------------------------------------

@app.route("/")
def home():

    return """
    <h1>ZETA AUTONOMY CORE</h1>

    <p>Status: Online</p>

    <form action="/chat" method="post">

        <input
            name="message"
            style="width:500px"
        >

        <button type="submit">
            Send
        </button>

    </form>
    """


# -------------------------------------------------
# CHAT
# -------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    if request.is_json:

        message = request.json.get(
            "message",
            ""
        )

    else:

        message = request.form.get(
            "message",
            ""
        )

    memory = get_memory()

    reply = ask_ai(
        message,
        memory
    )

    memory.setdefault(
        "conversation_history",
        []
    )

    memory["conversation_history"].append(
        {
            "user": message,
            "assistant": reply
        }
    )

    save_memory(memory)

    if request.is_json:

        return jsonify(
            {
                "reply": reply,
                "memory": memory
            }
        )

    return f"""
    <h2>ZETA</h2>

    <p><b>You:</b> {message}</p>

    <p><b>ZETA:</b> {reply}</p>

    <hr>

    <a href="/">Back</a>
    """


# -------------------------------------------------
# START SERVER
# -------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5050,
        debug=False
    )
