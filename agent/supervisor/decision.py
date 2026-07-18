class SupervisorDecision:

    def evaluate(self, health):

        if health.get("core") == "failed":
            return "restart_core"

        if health.get("ollama") == "failed":
            return "restart_ollama"

        if health.get("memory") == "failed":
            return "repair_memory"

        return "healthy"


if __name__ == "__main__":

    decision = SupervisorDecision()

    test = {
        "core": "healthy",
        "ollama": "healthy",
        "memory": "healthy"
    }

    print(
        decision.evaluate(test)
    )
