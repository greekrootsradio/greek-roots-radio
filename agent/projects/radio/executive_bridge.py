from agent.projects.radio.supervisor import RadioSupervisor


class RadioExecutiveBridge:

    def __init__(self):
        self.radio = RadioSupervisor()


    def status(self):

        return {
            "project": "Greek Roots Radio",
            "system": "radio_subsystem",
            "status": "connected"
        }


    def evaluate(self):

        return self.radio.run_cycle()


if __name__ == "__main__":

    bridge = RadioExecutiveBridge()

    print(
        bridge.status()
    )

    print(
        bridge.evaluate()
    )
