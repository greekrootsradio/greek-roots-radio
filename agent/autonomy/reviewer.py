import os
from datetime import datetime


class ReviewerAgent:

    def __init__(self):

        self.proposals = os.path.expanduser(
            "~/cyprus/workspace/proposals"
        )

        self.reports = os.path.expanduser(
            "~/cyprus/workspace/logs"
        )

        os.makedirs(
            self.reports,
            exist_ok=True
        )


    def review(self):

        approved = []
        rejected = []

        for file in os.listdir(self.proposals):

            if file.endswith(".py"):

                if file.startswith("_"):
                    rejected.append(file)

                else:
                    approved.append(file)


        report = {
            "time": str(datetime.now()),
            "approved_for_review": approved,
            "rejected": rejected,
            "status": "Waiting for Andreas approval"
        }


        filename = os.path.join(
            self.reports,
            "review_report.txt"
        )

        with open(filename, "w") as f:
            f.write(str(report))


        print(
            "[ZETA Reviewer] Report:",
            filename
        )

        return report
