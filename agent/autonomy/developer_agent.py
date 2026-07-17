from agent.autonomy.coder import CodeWriter
from agent.autonomy.tester import TesterAgent


class DeveloperAgent:

    def __init__(self):

        self.coder = CodeWriter()
        self.tester = TesterAgent()


    def build(self, task):

        print("[ZETA DEVELOPER] Building:", task)


        name = (
            task.lower()
            .replace(" ", "_")
        )


        self.coder.create_module(
            name,
            task
        )


        tests = self.tester.test_all()


        result = {

            "task": task,

            "module": name,

            "tests": tests,

            "status": "complete"

        }


        print(
            "[ZETA DEVELOPER] Build complete"
        )


        return result
