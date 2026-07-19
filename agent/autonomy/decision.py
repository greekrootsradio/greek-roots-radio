from datetime import datetime


def make_decision(plans):

    decisions = []

    for item in plans:

        decision = {
            "time": datetime.now().isoformat(),
            "type": item.get("type"),
            "decision": item.get("next_action"),
            "status": "approved"
        }

        decisions.append(decision)

    return decisions


if __name__ == "__main__":

    from agent.autonomy.planner import generate_plan

    plans = generate_plan()

    print("ZETA DECISION ENGINE")

    for decision in make_decision(plans):
        print(decision)
