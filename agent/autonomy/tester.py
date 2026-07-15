import os
import py_compile
from datetime import datetime


class TesterAgent:

    def __init__(self):

        self.workspace = os.path.expanduser(
            "~/cyprus/workspace/proposals"
        )

        self.logs = os.path.expanduser(
            "~/cyprus/workspace/tests"
        )

        os.makedirs(
            self.logs,
            exist_ok=True
        )


    def test_all(self):

        results = []

        for file in os.listdir(self.workspace):

            if file.endswith(".py"):

                path = os.path.join(
                    self.workspace,
                    file
                )

                try:

                    py_compile.compile(
                        path,
                        doraise=True
                    )

                    result = (
                        f"{file}: PASS"
                    )

                except Exception as e:

                    result = (
                        f"{file}: FAIL {e}"
                    )


                results.append(result)


        report = "\n".join(results)

        filename = os.path.join(
            self.logs,
            "test_report.txt"
        )

        with open(filename, "w") as f:
            f.write(
                "ZETA TEST REPORT\n"
                + str(datetime.now())
                + "\n\n"
                + report
            )


        print(
            "[ZETA Tester] Report:",
            filename
        )

        return results
