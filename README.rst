
.. image:: https://img.shields.io/pypi/v/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

.. image:: https://img.shields.io/pypi/l/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

.. image:: https://img.shields.io/pypi/pyversions/mattermostautodriver.svg
    :target: https://pypi.python.org/pypi/mattermostautodriver

Python Mattermost Auto Driver (APIv4)
=====================================

Info
----

The repository will try to keep up with the ``api`` specification in https://github.com/mattermost/mattermost/ (subfolder ``api``)
Changes in API of ``mattermostautodriver`` will likely be due to a change in the reference mattermost API documentation.

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
    You can make api calls by using calling `TypedDriver.endpointofchoice`.
    Using api[''] is deprecated for 5.0.0!

    So, for example, if you used `TypedDriver.api['users'].get_user('me')` before,
    you now just do `TypedDriver.users.get_user('me')`.
    The names of the endpoints and requests are almost identical to
    the names on the api.mattermost.com/v4 page.
    API calls always return the json the server send as a response.
    """
    foo.users.get_user_by_username('another.name')

    """
    If the api request needs additional parameters
    you can pass them to the function in the following way:
    - Path parameters are always simple parameters you pass to the function
    """
    foo.users.get_user(user_id='me')

    # - Query parameters are always passed by passing a `params` dict to the function
    foo.teams.get_teams(params={...})

    # - Request Bodies are always passed by passing an `options` dict or array to the function
    foo.channels.create_channel(options={...})

    # See the mattermost api documentation to see which parameters you need to pass.
    foo.channels.create_channel(options={
        'team_id': 'some_team_id',
        'name': 'awesome-channel',
        'display_name': 'awesome channel',
        'type': 'O'
    })

    """
    If you want to make a websocket connection to the mattermost server
    you can call the init_websocket method, passing an event_handler.
    Every Websocket event send by mattermost will be send to that event_handler.
    See the API documentation for which events are available.
    """
    foo.init_websocket(event_handler)

    # Use `disconnect()` to disconnect the websocket
    foo.disconnect()

    # To upload a file you will need to pass a `files` dictionary
    channel_id = foo.channels.get_channel_by_name_and_team_name('team', 'channel')['id']
    file_id = foo.files.upload_file(
        channel_id=channel_id,
        files={'files': (filename, open(filename, 'rb'))}
    )['file_infos'][0]['id']


    # track the file id and pass it in `create_post` options, to attach the file
    foo.posts.create_post(options={
        'channel_id': channel_id,
        'message': 'This is the important file',
        'file_ids': [file_id]})

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
