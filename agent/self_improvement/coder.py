import os
import datetime


class ZetaCoder:

    def __init__(self):
        self.proposals = os.path.expanduser(
            "~/cyprus/workspace/proposals"
        )

        os.makedirs(self.proposals, exist_ok=True)


    def create_proposal(self, title, request):

        filename = datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S_"
        ) + title.replace(" ", "_") + ".txt"

        path = os.path.join(
            self.proposals,
            filename
        )

        with open(path, "w") as f:
            f.write(
                "ZETA DEVELOPMENT PROPOSAL\n\n"
                f"REQUEST:\n{request}\n\n"
                "STATUS:\nWaiting for review\n"
            )

        return path
