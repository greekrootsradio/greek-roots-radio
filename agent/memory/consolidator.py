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

                consolidated[key] = memory.copy()

                continue



            existing = consolidated[key]


            old_value = existing.get(
                "value"
            )


            new_value = memory.get(
                "value"
            )


            # -------------------------
            # UPDATE TO NEW INFORMATION
            # -------------------------

            if new_value != old_value:

                existing["value"] = new_value


                if "history" not in existing:

                    existing["history"] = []


                existing["history"].append(
                    {
                        "old_value": old_value,
                        "updated": str(
                            datetime.now()
                        )
                    }
                )



            # -------------------------
            # BOOST CONFIDENCE
            # -------------------------

            existing["confidence"] = min(
                1.0,
                existing.get(
                    "confidence",
                    0
                ) + 0.1
            )


            # -------------------------
            # BOOST IMPORTANCE
            # -------------------------

            existing["importance"] = min(
                10,
                existing.get(
                    "importance",
                    5
                ) + 1
            )


            existing["updated"] = str(
                datetime.now()
            )


        return list(
            consolidated.values()
        )
