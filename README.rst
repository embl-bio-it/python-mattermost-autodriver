
.. image:: https://img.shields.io/pypi/v/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

.. image:: https://img.shields.io/pypi/l/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

.. image:: https://img.shields.io/pypi/pyversions/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

Python Mattermost Auto Driver (APIv4)
=====================================

This project maintains an auto-generated Python-based interface to `the Mattermost API <https://developers.mattermost.com/api-documentation/>`_ that follows official Mattermost releases.

.. note::

    2026-06-01 - The lead maintenance of this project changed. Further details at the bottom of this document.

Info
----

The endpoint code in this repository follows the ``api`` specification from https://github.com/mattermost/mattermost/ (subfolder ``api``).
API changes of ``mattermostautodriver`` follow the reference mattermost API documentation.

This project is forked from https://github.com/Vaelor/python-mattermost-driver but uses an automatic approach to generate all Python endpoint files from the mattermost OpenAPI specification.

Starting with version 10.8.2, Python 3.10 or greater is required. Previous versions needed Python 3.8+.

Warning
^^^^^^^

This repository generates code in a fully automated fashion based on the API specification provided by mattermost developers.
No additional effort of backwards compatibility is made.

Versions and Releases
---------------------

.. warning::

    Starting with version 10.8.2 this project now follows releases of
    `the official Mattermost server <https://docs.mattermost.com/about/mattermost-server-releases.html>`_.

See `pull request #21 <https://github.com/embl-bio-it/python-mattermost-autodriver/issues/21>`_ for additional context.

In production environments you are advised to keep this package in sync with Mattermost server updates.

Note that we only release with the latest Mattermost minor (MAJOR.MINOR.PATCH) version.
As an example, if Mattermost  ``1.3.1`` is released after we already have ``mattermostautodriver`` ``1.4.0`` out, we will only see a new driver release when Mattermost ``1.4.1`` or ``1.5.0`` is out.

.. note::

    Version ``11.8.1`` removes the deprecated dictionary-based ``Driver`` and ``AsyncDriver``
    classes. Use ``TypedDriver`` / ``AsyncTypedDriver`` with explicit keyword arguments instead.
    See the `migration guide <https://embl-bio-it.github.io/python-mattermost-autodriver/api_deprecation.html>`_
    for details. Because this project follows the Mattermost server version, this
    backwards-incompatible change is not signalled by the version number.

Installation
------------

.. inclusion-marker-start-install

``pip install mattermostautodriver``

.. inclusion-marker-end-install

Documentation
-------------

Documentation can be found at https://embl-bio-it.github.io/python-mattermost-autodriver/ .

Usage
-----

.. inclusion-marker-start-usage

.. code:: python

    from mattermostautodriver import TypedDriver

    foo = TypedDriver({
        """
        Required options

        Instead of the login/password, you can also use a personal access token.
        If you have a token, you don't need to pass login/pass.
        It is also possible to use 'auth' to pass a auth header in directly,
        for an example, see:
        https://embl-bio-it.github.io/python-mattermost-autodriver/#authentication
        """
        'url': 'mattermost.server.com',
        'login_id': 'user.name',
        'password': 'verySecret',
        'token': 'YourPersonalAccessToken',

        """
        Optional options

        These options already have useful defaults or are just not needed in every case.
        In most cases, you won't need to modify these.
        If you can only use a self signed/insecure certificate, you should set
        verify to your CA file or to False. Please double check this if you have any errors while
        using a self signed certificate!
        """
        'scheme': 'https',
        'port': 8065,
        'verify': True,  # Or /path/to/file.pem
        'mfa_token': 'YourMFAToken',
        """
        Setting this will pass the your auth header directly to
        the request libraries 'auth' parameter.
        You probably only want that, if token or login/password is not set or
        you want to set a custom auth header.
        """
        'auth': None,
        """
        If for some reasons you get regular timeouts after a while, try to decrease
        this value. The websocket will ping the server in this interval to keep the connection
        alive.
        If you have access to your server configuration, you can of course increase the timeout
        there.
        """
        'timeout': 30,

        """
        This value controls the request timeout.
        See https://python-requests.org/en/master/user/advanced/#timeouts
        for more information.
        The default value is None here, because it is the default in the
        request library, too.
        """
        'request_timeout': None,

        """
        To keep the websocket connection alive even if it gets disconnected for some reason you
        can set the  keepalive option to True. The keepalive_delay defines how long to wait in seconds
        before attempting to reconnect the websocket.
        """
        'keepalive': False,
        'keepalive_delay': 5,

        """
        This option allows you to provide additional keyword arguments when calling websockets.connect()
        By default it is None, meaning we will not add any additional arguments. An example of an
        additional argument you can pass is one used to  disable the client side pings:
        'websocket_kw_args': {"ping_interval": None},
        """
        'websocket_kw_args': None,

        """
        Setting debug to True, will activate a very verbose logging.
        This also activates the logging for the requests package,
        so you can see every request you send.

        Be careful. This SHOULD NOT be active in production, because this logs a lot!
        Even the password for your account when doing driver.login()!
        """
        'debug': False
    })

    """
    Most of the requests need you to be logged in, so calling login()
    should be the first thing you do after you created your TypedDriver instance.
    login() returns the raw response.
    If using a personal access token, you still need to run login().
    In this case, does not make a login request, but a `get_user('me')`
    and sets everything up in the client.
    """
    foo.login()

    """
    You can make api calls by calling `TypedDriver.endpointofchoice`.

    The endpoints and their arguments closely follow the official Mattermost
    API documentation at https://developers.mattermost.com/api-documentation/ .
    API calls return the JSON the server sent as a response.
    """
    foo.users.get_user_by_username('another.name')

    """
    All request parameters - path parameters, query parameters and request
    body fields - are passed as explicit keyword arguments, named exactly as
    in the Mattermost API documentation.
    """
    # Path parameter
    foo.users.get_user(user_id='me')

    # Query parameters
    foo.users.get_users(page=0, per_page=60)

    # Request body fields
    foo.channels.create_channel(
        team_id='some_team_id',
        name='awesome-channel',
        display_name='Awesome Channel',
        type='O',
    )

    """
    If you want to make a websocket connection to the mattermost server
    you can call the init_websocket method, passing an event_handler.
    Every Websocket event send by mattermost will be send to that event_handler.
    See the API documentation for which events are available.
    """
    foo.init_websocket(event_handler)

    # Use `disconnect()` to disconnect the websocket
    foo.disconnect()

    # To upload a file, pass the opened file object as the `files` argument
    channel_id = foo.channels.get_channel_by_name_for_team_name('team', 'channel')['id']
    file_id = foo.files.upload_file(
        channel_id=channel_id,
        files=open(filename, 'rb'),
    )['file_infos'][0]['id']

    # Track the file id and pass it to `create_post` to attach the file
    foo.posts.create_post(
        channel_id=channel_id,
        message='This is the important file',
        file_ids=[file_id],
    )

    # If needed, you can make custom requests by calling `make_request`
    foo.client.make_request('post', '/endpoint', options=None, params=None, data=None, files=None)

    # If you want to call a webhook/execute it use the `call_webhook` method.
    # This method does not exist on the mattermost api AFAIK, I added it for ease of use.
    foo.client.call_webhook('myHookId', options) # Options are optional

    # Finally, logout the user if using login/password authentication.
    foo.logout()

    # And close the client once done with it.
    foo.close()

.. inclusion-marker-end-usage

Updating OpenAPI specification
------------------------------

First we need to obtain Mattermost's API in an OpenAPI JSON.

.. code:: shell

    git clone --depth=1 --filter=tree:0 https://github.com/mattermost/mattermost
    cd mattermost/api
    make build
    ./node_modules/.bin/swagger-cli bundle --outfile openapi.json v4/html/static/mattermost-openapi-v4.yaml
    cd -

With the above commands you will have cloned and created an ``openapi.json`` file that will be used by the conversion script.

First install all required dependencies in a virtual environment.

.. code:: shell

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Finally, with the virtual environment still loaded execute

.. code:: shell

    ./scripts/generate_endpoints.sh

to generate the updated endpoint definition.
This script will also update the documentation by running:

.. code:: shell

    cd docs
    ./update_endpoints.py

The current API conversion code was designed for Python 3.13.
As it uses Python's AST parser and generator, alongside with `Black <https://github.com/psf/black>`_ different versions of Python may result in some differences in the generated code. Double check with a ``git diff`` once complete.

History of contributions and lead maintenance
---------------------------------------------

- Bertie (@bertie-sektorcert) - Enhancements and maintenance. Lead maintainer 2026-...
- Renato Alves (@unode) - `Proof-of-Concept auto-driver <https://github.com/Vaelor/python-mattermost-driver/pull/100>`_, launch of ``python-mattermost-autodriver``, maintenance and enhancements. Lead maintainer 2022-2026.
- Christian (@Vaelor) and others - Original `python-mattermost-driver <https://github.com/Vaelor/python-mattermost-driver>`_ and `idea for autodriver project <https://github.com/Vaelor/python-mattermost-driver/issues/60>`_.
