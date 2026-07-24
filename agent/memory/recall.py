import json

from agent.memory import load_memory


class MemoryRecall:


    def search(self, query):

        results = []

        query = query.lower()


        memories = load_memory()


        for item in memories:


            # -------------------------
            # Structured memories
            # -------------------------

            if (
                item.get("type") == "conversation"
                and isinstance(item.get("memory"), dict)
            ):

                memory = item["memory"]


                if memory.get("type") == "structured_memory":

                    for entry in memory.get(
                        "memory",
                        []
                    ):

                        text = (
                            str(entry.get("key",""))
                            + " "
                            + str(entry.get("value",""))
                        ).lower()


                        if (
                            query in text
                            or "name" in query
                        ):

                            results.append(
                                entry
                            )


                continue



            # -------------------------
            # Old memory compatibility
            # -------------------------

            text = json.dumps(
                item
            ).lower()


            if query in text:

                results.append(
                    item
                )


        return results
