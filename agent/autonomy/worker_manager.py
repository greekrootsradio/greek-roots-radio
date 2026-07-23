from datetime import datetime

from agent.autonomy.worker import ZetaWorker


class WorkerManager:

    def __init__(self):
        self.worker = ZetaWorker()
        self.history = []

    def run(self):
        print("[ZETA WORKER MANAGER] Running worker")
        result = self.worker.run_once()

        event = {
            "time": str(datetime.now()),
            "result": result
        }

        self.history.append(event)

        print("[ZETA WORKER MANAGER] Worker cycle complete")
        return event
