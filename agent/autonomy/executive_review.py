from datetime import datetime


class ExecutiveReview:


    def __init__(self):

        self.history = []



    def review_cycle(self, cycle):

        review = {

            "time": str(datetime.now()),

            "decision":
                cycle.get(
                    "decision",
                    {}
                ),

            "result":
                cycle.get(
                    "status",
                    "unknown"
                ),

            "assessment":
                "cycle completed",

            "lesson":
                "future decisions should use previous experience"

        }


        self.history.append(
            review
        )


        print(
            "[ZETA REVIEW]"
        )

        print(
            review
        )


        return review
