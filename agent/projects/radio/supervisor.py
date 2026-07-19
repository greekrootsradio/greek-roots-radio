from datetime import datetime

from agent.projects.radio.commander import RadioCommander


class RadioSupervisor:

    def __init__(self):

        self.name = "ZETA Radio Supervisor"
        self.commander = RadioCommander()


    def status(self):

        return {
            "supervisor": self.name,
            "time": str(datetime.now()),
            "radio": "Greek Roots Radio",
            "state": "monitoring"
        }


    def evaluate(self):

        station = self.commander.assess_station()

        return {
            "decision": "review_station",
            "assessment": station
        }


    def run_cycle(self):

        return {
            "status": self.status(),
            "evaluation": self.evaluate(),
            "next": self.commander.execute_next_step()
        }


if __name__ == "__main__":

    supervisor = RadioSupervisor()

    print(
        supervisor.run_cycle()
    )
