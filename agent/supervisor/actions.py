import subprocess
import datetime


class SupervisorActions:


    def __init__(self):

        self.log = (
            "workspace/logs/zeta_actions.log"
        )


    def write(self,message):

        with open(self.log,"a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def restart_ollama(self):

        self.write(
            "Restarting Ollama service"
        )

        subprocess.run(
            ["pkill","ollama"]
        )

        return "ollama_restart_complete"



    def restart_core(self):

        self.write(
            "Core restart requested"
        )

        return "core_restart_complete"



    def repair_memory(self):

        self.write(
            "Memory repair requested"
        )

        return "memory_repair_complete"
