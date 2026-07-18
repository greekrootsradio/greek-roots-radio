import re


class NamingEngine:

    def clean_module_name(self, name):

        name = name.lower()

        name = re.sub(
            r'[^a-z0-9]+',
            '_',
            name
        )

        return name.strip("_")


def clean_module_name(name):

    engine = NamingEngine()

    return engine.clean_module_name(name)
