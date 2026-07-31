import time
from datetime import datetime
from agent.autonomy.supervisor import ZetaSupervisor

class AutonomyEngine:
    def __init__(self, sleep_seconds=900):
        self.sleep_seconds = sleep_seconds
        self.supervisor = ZetaSupervisor()
        self.running = False

    def start(self):
        self.running = True
        print(f"[ZETA ENGINE] Online. Safety Throttle Interval: {self.sleep_seconds}s")
        while self.running:
            try:
                self.supervisor.run_cycle()
            except Exception as e:
                print(f"[ZETA ENGINE] Loop Interruption Exception: {e}")
            
            print(f"[ZETA ENGINE] Sleeping for {self.sleep_seconds} seconds...")
            time.sleep(self.sleep_seconds)

    def stop(self):
        self.running = False
        print("[ZETA ENGINE] Safely Stopped.")

if __name__ == "__main__":
    engine = AutonomyEngine(sleep_seconds=900)
    engine.start()
