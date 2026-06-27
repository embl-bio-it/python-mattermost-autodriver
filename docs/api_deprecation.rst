Migrating from the dictionary-based API
=======================================

For historical context refer to `pull request #23 <https://github.com/embl-bio-it/python-mattermost-autodriver/pull/23>`_.

.. note::
    The dictionary-based ``Driver`` / ``AsyncDriver`` interface was removed in version
    ``11.8.1``. This page describes how to migrate existing code to ``TypedDriver`` /
    ``AsyncTypedDriver``.

The typed API exposes all arguments explicitly instead of encapsulating them in a
dictionary. This change affects most endpoints that accept optional arguments, including
file uploads.

Calls that take no options behave the same way; only the driver class name changes:

.. code:: python

    dri = TypedDriver({
        "scheme": "https",
        "url": "mattermost.server.com",
        "port": 443,
        "token": "YourPersonalAccessToken",
    })

    dri.login()
    team_id = dri.teams.get_team_by_name("default")["id"]
    channel_id = dri.channels.get_channel_by_name(team_id, "town-square")

Endpoint calls that previously passed an ``options`` dictionary, the **old syntax**:

.. code:: python

    dri.channels.create_channel(options={
        "team_id": team_id,
        "name": "awesome-channel",
        "display_name": "Awesome Channel",
        "type": "O",
    })

require an expansion of the options dictionary:

.. code:: python

    dri.channels.create_channel(**{
        "team_id": team_id,
        "name": "awesome-channel",
        "display_name": "Awesome Channel",
        "type": "O",
    })

This shortcut works so long as none of the arguments clashes with a python keyword.
Examples of clashes include ``from``.

Alternatively, pass the arguments explicitly:

.. code:: python

    dri.channels.create_channel(
        team_id=team_id,
        name="awesome-channel",
        display_name="Awesome Channel",
        type="O",
    )

The old dictionary-based API has been removed
---------------------------------------------

Earlier versions allowed continued use of the deprecated interface through ``Driver`` /
``AsyncDriver``, which raised a ``DeprecationWarning`` on instantiation. These classes,
and the underlying ``endpoints_old`` interface, were removed in version ``11.8.1`` and are
no longer importable from ``mattermostautodriver``. Code must use ``TypedDriver`` /
``AsyncTypedDriver`` instead.
