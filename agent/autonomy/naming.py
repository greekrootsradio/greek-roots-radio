import re


def clean_module_name(name):

    name = name.lower()

    name = re.sub(
        r'[^a-z0-9]+',
        '_',
        name
    )

    return name.strip("_")
