from agent.memory.core import (
    get_memory,
    save_memory
)

from datetime import datetime


class MemoryManager:


    def __init__(self):

        self.memory = get_memory()



    def remember_fact(self, category, key, value):

        if category not in self.memory:

            self.memory[category] = {}


        if isinstance(self.memory[category], dict):

            self.memory[category][key] = value


        save_memory(self.memory)


        return {
            "status": "stored",
            "category": category,
            "key": key,
            "value": value
        }



    def add_goal(self, goal):

        if goal not in self.memory["goals"]:

            self.memory["goals"].append(goal)


        save_memory(self.memory)


        return {
            "status": "goal added",
            "goal": goal
        }



    def add_task(self, task):

        self.memory["tasks"].append(
            {
                "task": task,
                "status": "pending",
                "created": str(datetime.now())
            }
        )


        save_memory(self.memory)


        return {
            "status": "task added",
            "task": task
        }



    def summary(self):

        return {

            "user": self.memory.get(
                "user_profile",
                {}
            ),

            "projects": self.memory.get(
                "projects",
                {}
            ),

            "goals": self.memory.get(
                "goals",
                []
            ),

            "tasks": self.memory.get(
                "tasks",
                []
            )

        }
