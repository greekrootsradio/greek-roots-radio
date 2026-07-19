from datetime import datetime


class RadioDecisionGovernor:

    def __init__(self):
        self.station = "Greek Roots Radio"
        self.mode = "supervised_autonomy"


    def evaluate(self, request):

        if request == "start_stream":
            return {
                "request": request,
                "decision": "approved",
                "reason": "systems_ready",
                "time": str(datetime.now())
            }

        if request == "prepare_show":
            return {
                "request": request,
                "decision": "approved",
                "reason": "show_preparation_allowed",
                "time": str(datetime.now())
            }

        return {
            "request": request,
            "decision": "requires_review",
            "reason": "unknown_action"
        }


if __name__ == "__main__":

    governor = RadioDecisionGovernor()

    print(
        governor.evaluate("start_stream")
    )

    print(
        governor.evaluate("prepare_show")
    )
