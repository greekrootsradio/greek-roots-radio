import os


class SafetyManager:


    def __init__(self):

        self.project_root = os.path.expanduser(
            "~/cyprus"
        )


    def allowed_path(self, path):

        full_path = os.path.abspath(
            path
        )

        return full_path.startswith(
            self.project_root
        )


    def approve_change(self, file_path):

        if not self.allowed_path(file_path):

            return {
                "approved": False,
                "reason": "Outside project boundary"
            }


        return {
            "approved": True,
            "reason": "Inside project boundary"
        }


    def check_action(self, action):

        blocked = [

            "delete system files",

            "modify outside project",

            "remove git history"

        ]


        for item in blocked:

            if item in action.lower():

                return False


        return True
