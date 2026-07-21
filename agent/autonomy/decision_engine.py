import json
import os
from datetime import datetime

from agent.memory.memory_manager import MemoryManager


class DecisionEngine:


    def __init__(self):

        self.goals_file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        self.memory = MemoryManager()



    def load_goals(self):

        with open(
            self.goals_file,
            "r"
        ) as f:

            return json.load(f)



    def score_goal(self, goal, memory):

        score = goal.get(
            "priority",
            0
        )


        name = goal.get(
            "goal",
            ""
        ).lower()



        # Core autonomy always wins

        if "memory" in name:
            score += 30


        if "goal" in name:
            score += 20


        if "task" in name:
            score += 20


        if "experience" in name:
            score += 10



        # User goal influence

        for user_goal in memory.get(
            "goals",
            []
        ):

            if "autonomous" in user_goal.lower():

                if "automation" in name:
                    score += 40


                if "memory" in name:
                    score += 40



        return score



    def choose_priority(self):


        memory = self.memory.summary()


        goals = self.load_goals()


        active = goals.get(
            "active",
            []
        )



        ranked = []


        for goal in active:

            ranked.append(
                {
                    "goal": goal,
                    "score": self.score_goal(
                        goal,
                        memory
                    )
                }
            )



        ranked.sort(
            key=lambda x:x["score"],
            reverse=True
        )


        winner = ranked[0] if ranked else None



        decision = {

            "chosen_goal":
                winner["goal"]["goal"]
                if winner
                else None,


            "score":
                winner["score"]
                if winner
                else 0,


            "projects":
                list(
                    memory.get(
                        "projects",
                        {}
                    ).keys()
                ),


            "user_goals":
                memory.get(
                    "goals",
                    []
                ),


            "reason":
                "selected using autonomy priority model",


            "time":
                str(datetime.now())

        }



        print(
            "[ZETA DECISION ENGINE]"
        )

        print(
            decision
        )


        return decision
