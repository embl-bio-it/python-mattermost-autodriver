API Deprecation
===============

For historical context refer to `pull request #23 <https://github.com/embl-bio-it/python-mattermost-autodriver/pull/23>`_.

The new API exposes all arguments explicitly instead of encapsulated in a dictionary.
This change affects most endpoints that accept optional arguments including file uploads.

You won't need to modify your code for calls such as these:

.. code:: python

    dri = Driver({
        "scheme": "https",
        "url": "mattermost.server.com",
        "port": 443,
        "token": "YourPersonalAccessToken",

    dri.login()
    team_id = dri.teams.get_team_by_name("default")["id"]
    channel_id = dri.channels.get_channel_by_name(team_id, "town-square")

but for endpoint calls with options the **old syntax**:

.. code:: python

    dri.channels.create_channel(options={
        "team_id": team_id,
        "name": "awesome-channel",
        "display_name": "Awesome Channel",
        "type": "O",
    })

requires an expansion of the options dictionary:

.. code:: python

    dri.channels.create_channel(**{
        "team_id": team_id,
        "name": "awesome-channel",
        "display_name": "Awesome Channel",
        "type": "O",
    })

This shortcut works so long as none of the arguments clashes with python keywords.
Examples from clashes include ``from``

or that arguments are passed explicitly:

.. code:: python

    dri.channels.create_channel(
        team_id=team_id,
        name="awesome-channel",
        display_name="Awesome Channel",
        type="O",
    )

I want to continue using the old API
------------------------------------

If you want to continue using the deprecated API you can do so by initializing ``Driver(options)`` with ``Driver(options, old_api=True)`` which will allow you to use the old interface but will raise a ``DeprecationWarning``.

Please note that this interface will be removed in the future so we recommend that you update your code as soon as possible.
