from agent.memory import save_memory


class MemoryConsolidator:

    def consolidate(self, memories):

        profile = {
            "user_profile": {},
            "preferences": []
        }

        for item in memories:

            if item["type"] == "user_profile":

                profile["user_profile"][
                    item["key"]
                ] = item["value"]


            elif item["type"] == "preference":

                if item["value"] not in profile["preferences"]:
                    profile["preferences"].append(
                        item["value"]
                    )


        save_memory(
            {
                "type": "profile",
                "memory": profile
            }
        )


        return profile


    def merge(self, memories):

        return self.consolidate(memories)
