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
automatically, honoring the wait requested by the server. Connection errors
and 502/503/504 responses are also retried, but only for idempotent requests
(``GET``, ``PUT``, ``DELETE`` and ``HEAD``), since a ``POST`` may already
have been processed by the server. Requests carrying files or a streaming
request body are never retried automatically, as their content is consumed
when the request is first sent.

The wait is read from the ``Retry-After`` header if present, falling back to
``X-RateLimit-Reset`` otherwise. ``Retry-After`` takes precedence because it
is the header standardized by the HTTP specification (RFC 9110), whereas the
``X-RateLimit-*`` headers - which Mattermost also sends - are an unstandardized
convention. Values are accepted in the forms found in the wild: a delay in
seconds (``120``), an HTTP-date (``Wed, 21 Oct 2026 07:28:00 GMT``), and an
absolute unix timestamp (``1794000000``). An unparseable header is skipped in
favor of the next one; if no usable value remains, retries use exponential
backoff instead. The same parsed wait is exposed to callers as the
``retry_after`` attribute of ``TooManyRequests``, always as non-negative
seconds from now.

The full mapping of failure modes to exceptions and retry behavior:

.. list-table::
   :header-rows: 1
   :widths: 22 34 44

   * - Failure
     - Exception
     - Retry behavior
   * - HTTP 400
     - ``InvalidOrMissingParameters``
     - Not retried
   * - HTTP 401
     - ``NoAccessTokenProvided``
     - Not retried
   * - HTTP 403
     - ``NotEnoughPermissions``
     - Not retried
   * - HTTP 404
     - ``ResourceNotFound``
     - Not retried
   * - HTTP 405
     - ``MethodNotAllowed``
     - Not retried
   * - HTTP 413
     - ``ContentTooLarge``
     - Not retried
   * - HTTP 429
     - ``TooManyRequests``
     - Retried for all methods, waiting as requested by the server
   * - HTTP 501
     - ``FeatureDisabled``
     - Not retried
   * - HTTP 502 / 503 / 504
     - ``UnknownMattermostError``
     - Retried with exponential backoff, idempotent methods only
   * - Other HTTP error codes
     - ``UnknownMattermostError``
     - Not retried
   * - Connection errors and timeouts
     - ``httpx.TransportError`` (raised by httpx)
     - Retried with exponential backoff, idempotent methods only

The listed exception is what a request raises once it fails for good - either
immediately for non-retried failures, or after retries are exhausted. Error
responses other than 429 whose body does not follow the standard Mattermost
JSON error schema raise ``InvalidMattermostError`` instead of the exception
listed above.

Two driver options control this behavior:

- ``max_retries`` (default ``3``) - maximum number of automatic retries per
  request. Set to ``0`` to disable retrying entirely.
- ``retry_max_sleep`` (default ``30``) - upper bound in seconds for a single
  wait between retries. If the server requests a longer wait, the request
  fails immediately with ``TooManyRequests`` and the requested wait time is
  available in its ``retry_after`` attribute.

Together these bound the total time a single call may spend waiting between
attempts at ``max_retries * retry_max_sleep`` - 90 seconds with the defaults,
reached only if the server repeatedly requests near-maximum waits. When no
usable wait is provided and exponential backoff applies, the default total is
3.5-7 seconds instead. Set ``max_retries`` to ``0`` if failing fast matters
more than resilience.

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

.. autoclass:: MethodNotAllowed

.. autoclass:: ContentTooLarge

.. autoclass:: TooManyRequests

.. autoclass:: FeatureDisabled


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
