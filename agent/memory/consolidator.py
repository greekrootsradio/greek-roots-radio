from agent.memory import save_memory


class MemoryConsolidator:

    def consolidate(self, memories):

        profile = {
            "user_profile": {},
            "preferences": []
        }


        for item in memories:

            category = item.get(
                "category",
                item.get("type")
            )


            if category == "user_profile":

                profile["user_profile"][
                    item["key"]
                ] = item["value"]


            elif category == "preference":

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



    # compatibility alias
    # allows older pipeline tests
    # to call merge()

    def merge(self, memories):

        return self.consolidate(memories)
