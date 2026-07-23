import json
import os
from datetime import datetime


class ExperienceEngine:

    def __init__(self):

        self.history_file = os.path.expanduser(
            "~/cyprus/data/development_history.json"
        )

        self.goals_file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        os.makedirs(
            os.path.dirname(self.history_file),
            exist_ok=True
        )

        if not os.path.exists(self.history_file):

            with open(self.history_file, "w") as f:
                json.dump([], f, indent=4)



    def _load_json(self, path, default):

        if not os.path.exists(path):
            return default

        try:

            with open(path, "r") as f:
                return json.load(f)

        except Exception:

            return default



    def _save_json(self, path, data):

        with open(path, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )



    def record_cycle(self, event):

        history = self._load_json(
            self.history_file,
            []
        )


        event["time"] = str(
            datetime.now()
        )


        history.append(
            event
        )


        self._save_json(
            self.history_file,
            history
        )


        print(
            "[Experience] Cycle recorded"
        )


        return event



    def record(self, event):

        """
        Compatibility interface.

        Supervisor expects:
            experience.record()

        Existing engine uses:
            record_cycle()

        This keeps both interfaces working.
        """

        print(
            "[Experience] Recording experience"
        )


        return self.record_cycle(
            event
        )



    def summarize(self):

        history = self._load_json(
            self.history_file,
            []
        )


        summary = {

            "total_cycles": len(history),

            "last_event": (
                history[-1]
                if history
                else None
            ),

            "time": str(
                datetime.now()
            )

        }


        print(
            "[Experience] Summary ready"
        )


        return summary



    def completed_modules(self):

        history = self._load_json(
            self.history_file,
            []
        )


        completed = set()


        for event in history:

            module = event.get(
                "module"
            )


            if module and event.get(
                "result"
            ) == "passed":

                completed.add(
                    module
                )


        return completed



if __name__ == "__main__":

    engine = ExperienceEngine()


    test = engine.record(
        {
            "module": "experience_engine",
            "result": "passed"
        }
    )


    print(test)


    print(
        engine.summarize()
    )
