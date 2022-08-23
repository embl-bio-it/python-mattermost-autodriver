#!/usr/bin/env python

import os

template = """
{name_title}
{title_under}

.. automodule:: mattermostautodriver.endpoints.{endpoint}
    :members:
    :undoc-members:
    :show-inheritance:

"""

with open("endpoints.rst", "w") as fh:
    fh.write("Endpoints\n=========\n\n")

    for endpoint in sorted(os.listdir("../src/mattermostautodriver/endpoints/")):
        if endpoint.startswith("_"):
            continue

        name = os.path.splitext(endpoint)[0]

        name_title = name.replace("_", " ").title()
        title_under = len(name_title) * "-"

        fh.write(template.format(**{
            "name_title": name_title,
            "title_under": title_under,
            "endpoint": name,
        }))
