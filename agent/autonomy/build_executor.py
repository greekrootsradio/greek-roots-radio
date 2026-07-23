from datetime import datetime
import os


class BuildExecutor:


    def __init__(self):

        self.name = "ZETA Build Executor"



    def execute(self, package):

        print(
            "[ZETA BUILD EXECUTOR] Checking permission"
        )


        if not package.get(
            "execution_allowed",
            False
        ):

            return {

                "executor": self.name,

                "status": "blocked",

                "reason":
                    "execution approval missing",

                "time":
                    str(datetime.now())

            }



        files = package.get(
            "approved_files",
            []
        )


        created = []


        for file in files:

            path = os.path.expanduser(
                "~/cyprus/" + file
            )


            directory = os.path.dirname(
                path
            )


            os.makedirs(
                directory,
                exist_ok=True
            )


            if not os.path.exists(path):

                open(
                    path,
                    "w"
                ).close()


                created.append(
                    file
                )



        return {

            "executor": self.name,

            "status":
                "completed",

            "files_created":
                created,

            "time":
                str(datetime.now())

        }

