from datetime import datetime


def execute_action(decision):

    action = {
        "time": datetime.now().isoformat(),
        "decision": decision,
        "action": None,
        "result": None
    }


    if "task list" in decision.lower():

        action["action"] = "Create development checklist"
        action["result"] = "Planning checklist generated"


    elif "project status" in decision.lower():

        action["action"] = "Review project"
        action["result"] = "Project review completed"


    else:

        action["action"] = "Analyse decision"
        action["result"] = "No automated action available"


    return action



if __name__ == "__main__":

    print("ZETA ACTION ENGINE")

    decisions = [
        "Analyse requirements and create task list",
        "Review project status and identify improvements"
    ]


    for decision in decisions:

        result = execute_action(decision)

        print(result)
