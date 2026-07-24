from datetime import datetime


class MemoryConsolidator:


    def consolidate(self, memories):

        consolidated = {}

        for memory in memories:

            key = (
                memory.get("category"),
                memory.get("key")
            )

            if key not in consolidated:

                consolidated[key] = memory

                continue


            existing = consolidated[key]


            # -------------------------
            # KEEP HIGHER CONFIDENCE
            # -------------------------

            if memory.get(
                "confidence",
                0
            ) > existing.get(
                "confidence",
                0
            ):

                existing["value"] = memory["value"]



            # -------------------------
            # INCREASE IMPORTANCE
            # -------------------------

            existing["importance"] = min(
                10,
                existing.get(
                    "importance",
                    5
                ) + 1
            )


            # -------------------------
            # UPDATE TIMESTAMP
            # -------------------------

            existing["updated"] = str(
                datetime.now()
            )


            # -------------------------
            # KEEP HISTORY
            # -------------------------

            if "history" not in existing:

                existing["history"] = []


            existing["history"].append(
                {
                    "value": memory["value"],
                    "time": str(datetime.now())
                }
            )


        return list(
            consolidated.values()
        )
