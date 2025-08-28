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

Classes
'''''''

.. automodule:: mattermostautodriver
.. autoclass:: TypedDriver
    :members:
    :undoc-members:

.. autoclass:: Client
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

.. autoclass:: FeatureDisabled


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
