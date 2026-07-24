class MemoryExtractor:

    def extract(self, user_input):

        memories = []

        text = user_input.lower()

        if "my name is" in text:
            name = user_input.split("my name is",1)[1].strip()

            memories.append(
                {
                    "type": "user_profile",
                    "key": "name",
                    "value": name
                }
            )

        if "i like" in text:
            item = user_input.split("i like",1)[1].strip()

            memories.append(
                {
                    "type": "preference",
                    "key": "likes",
                    "value": item
                }
            )

        if "i am building" in text:
            project = user_input.split("i am building",1)[1].strip()

            memories.append(
                {
                    "type": "project",
                    "key": "building",
                    "value": project
                }
            )

        return memories
