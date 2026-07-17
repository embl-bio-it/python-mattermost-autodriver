.. mattermostautodriver documentation master file, created by
   sphinx-quickstart on Thu Jun 29 10:38:30 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mattermostautodriver documentation
==================================

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Contents:

   endpoints
   api_deprecation
   changelog
   contributing


See https://github.com/embl-bio-it/python-mattermost-autodriver for the github repository.

You interact with this module mainly by using the ``TypedDriver`` class.
If you want to access information about the logged in user, like the user id,
you can access them by using ``TypedDriver.client.userid``.

Installation
''''''''''''
.. include:: ../README.rst
    :start-after: inclusion-marker-start-install
    :end-before: inclusion-marker-end-install

Usage
'''''
.. include:: ../README.rst
    :start-after: inclusion-marker-start-usage
    :end-before: inclusion-marker-end-usage

.. include:: auth.rst

Retries
'''''''

Requests that fail due to server side rate limiting (HTTP 429) are retried
automatically, honoring the ``Retry-After`` / ``X-RateLimit-Reset`` response
headers. Connection errors and 502/503/504 responses are also retried, but
only for idempotent requests (``GET``, ``PUT``, ``DELETE`` and ``HEAD``),
since a ``POST`` may already have been processed by the server. Requests
uploading files are never retried automatically.

Two driver options control this behavior:

- ``max_retries`` (default ``3``) - maximum number of automatic retries per
  request. Set to ``0`` to disable retrying entirely.
- ``retry_max_sleep`` (default ``30``) - upper bound in seconds for a single
  wait between retries. If the server requests a longer wait, the request
  fails immediately with ``TooManyRequests`` and the requested wait time is
  available in its ``retry_after`` attribute.

Classes
'''''''

.. automodule:: mattermostautodriver
.. autoclass:: TypedDriver
    :members:
    :undoc-members:

.. autoclass:: Client
    :members:

Constants
'''''''''

.. automodule:: mattermostautodriver.constants
    :members:

Exceptions that api requests can throw
''''''''''''''''''''''''''''''''''''''

.. automodule:: mattermostautodriver.exceptions

.. autoclass:: InvalidMattermostError

.. autoclass:: UnknownMattermostError

.. autoclass:: InvalidOrMissingParameters

.. autoclass:: NoAccessTokenProvided

.. autoclass:: NotEnoughPermissions

.. autoclass:: ResourceNotFound

.. autoclass:: ContentTooLarge

.. autoclass:: TooManyRequests

.. autoclass:: FeatureDisabled


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
