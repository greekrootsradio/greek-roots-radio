from flask import Flask, request, jsonify

import threading
import time

from agent.brain import ask_ai
from agent.memory import get_memory, save_memory
from agent.autonomy.engine import AutonomyEngine

# -------------------------------------------------
# PROJECT MANAGERS
# -------------------------------------------------

try:
    from agent.projects.radio_project_manager import RadioProjectManager
except Exception:
    RadioProjectManager = None


app = Flask(__name__)


print("==============================================")
print("           ZETA AUTONOMY CORE ONLINE")
print("==============================================")


# -------------------------------------------------
# LOAD ACTIVE PROJECTS
# -------------------------------------------------

def load_projects():

    if RadioProjectManager is None:
        print("Project Manager not available.")
        return

    try:

        radio = RadioProjectManager()

        report = radio.analyse()

        print()
        print("==============================================")
        print(" ACTIVE PROJECT")
        print("==============================================")

        print(f"Project : {report.get('project')}")
        print(f"Status  : {report.get('status')}")
        print()

        print("Mission")

        for item in report.get("mission", []):
            print(f"  • {item}")

        print()

        print("Next Tasks")

        for task in report.get("next_tasks", []):
            print(f"  • {task}")

        print("==============================================")
        print()

    except Exception as e:

        print("Unable to load project manager")
        print(e)


load_projects()


# -------------------------------------------------
# START AUTONOMY ENGINE
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

    <p>Online</p>

    <form action="/chat" method="post">

        <input
            name="message"
            style="width:400px">

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
# SERVER
# -------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5050,
        debug=False
    )
