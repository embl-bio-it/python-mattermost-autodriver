Unreleased
""""""""""

Code
''''

-

Documentation
'''''''''''''

-

Maintenance
'''''''''''

-

2.1.0
"""""

Code
''''

- New endpoints ``Bookmarks``, ``OutgoingConnections``, ``OutgoingOauthConnections`` and ``Reports``
- Modified ``oauth.Oauth`` endpoints extensively
- Renamed ``posts.save_acknowledgement_for_post`` to ``posts.delete_acknowledgement_for_post``
- Add ``posts.move_thread``
- Add option ``use_rest_semantics`` to ``system.get_ping``
- Remove ``system.get_warn_metrics_status``
- Remove ``system.send_warn_metric_ack``
- Remove ``system.send_trial_license_warn_metric_ack``
- Add ``users.get_users_for_reporting``
- Add ``users.get_user_count_for_reporting``
- Add ``users.get_user_limits``

Documentation
'''''''''''''

- Minor typos corrected and slight reformatting

2.0.0
"""""

Code
''''

- Remove non-standard "TRACE" debug level in httpx code
- Fix logging output when passing ``debug=True`` to ``Driver()``
- Include API cnanges as of 2023-12-01
- Add ``cloud.get_endpoint_for_installation_information``
- Add ``emoji.get_emojis_by_names``
- Add ``groups.restore_group``
- Add ``users.get_users_with_invalid_emails``
- Fix URL of ``commands.list_command_autocomplete_suggestions``
- Fix URL of ``files.get_file_public``
- Remove ``insights`` and ``opengraph`` endpoints
- New endpoints ``filtering`` and ``ip``
- ``threads.set_thread_unread_by_post_id`` now uses POST

Documentation
'''''''''''''

- Updated README API clone instructions. API is now part of main mattermost repository.

Maintenance
'''''''''''

- Rename GitHub Actions for clarity
- Force upgrade of pip in sphinx build GitHub Action - fixes docutils incompatibility resolution

1.3.0
"""""

Release 1.2.3 and 1.2.4 should have been made under a new minor digit.
This release addresses this mistake.

Code
''''

- Minor refactor to avoid using basepath in hook calls
- Fix missing /api/v4 in websocket handcrafted URL

Maintenance
'''''''''''

- Update GitHub Actions to resolve deprecation warnings
- Fix GitHub Action Python 3.10 related failures
- Add possiblity to manually release to PyPi

1.2.4
"""""

Code
''''

- Include playbook API interface changes as of 2023-05-31
- Remove basepath to accomodate API changes due to the inclusion of playbook endpoints
- Endpoint root paths now include the full API path

Documentation
'''''''''''''

- Hide table of contents from index page

Maintenance
'''''''''''

- GitHub action renamed to clarify purpose and action taken
- Restart CHANGELOG.md to reflect mattermostautodriver changes and releases
- Add Python 3.11 to list of supported versions


1.2.3
"""""

Code
''''

- Include playbook API interface changes as of 2023-03-21
- Fix syntax problem in install_requires

Maintenance
'''''''''''

- Update deployment python version in GitHub action

1.2.2
"""""

Code
''''

- Endpoints updated to reflect Mattermost API status as of 2022-10-11
- Logout API endpoint renamed - endpoint is logout() not logout_user()
- Thread-specific API endpoints are now available
- Mattermost API documentation is now linked from method docstrings
- The dependency ``inflection`` was pinned to at least version 0.5.1

Documentation
'''''''''''''

- Documentation was reworked to include links to Mattermost API docs

Maintenance
'''''''''''

- Missing operationId is now fatal when converting

1.2.1
"""""

Code
''''

- Only documentation changes occurred in this release.

Documentation
'''''''''''''

- Several style formatting changes
- Sphinx now specifies english as documentation language

Maintenance
'''''''''''

- Fix indentation alignment issues
- Reduce number of line breaks around titles

1.2.0
"""""

Code
''''

- Only documentation changes occurred in this release

Documentation
'''''''''''''

- Several style formatting changes
- Sphinx now specifies english as documentation language

Maintenance
'''''''''''

- Update API according to upload semantics
- Add files attribute to any API call involving uploads
- Update command as swagget2openapi isn't always available
- Update API spec as of 2022-08-25
- Update location of call_webhook

1.1.5
"""""

- Don't check hostname when using ssl.CERT_NONE
- Update endpoints docs

1.1.4
"""""

- Re-fix __new__ signature

1.1.3
"""""

- Fix __new__ signature

1.1.2
"""""

- Fix version require

1.1.1
"""""

- Change auth method
- Fixing commas in README

1.1.0
"""""

- Re-add call_webhook previous webhooks.call_webhook
- Add get_last_trial_license endpoint
- Replace hardcoded property endpoints with dynamic ones
- Add doc about (re)generating API spec
- Update API spec to latest
- Use CamelCase for class names in API
- Add black and inflection to dependencies
- Use CamelCase for class names

1.0.0
"""""

- Clarify relation to mattermostdriver
- Rename driver to mattermostautodriver
- Bump version to 8.0.0 due to many API renames and backwards incompatibility
- Add self-generated endpoints
- Use pyproject.toml as black config
- Add helper script to generate updated endpoints
- Format all files with black in a single invocation
- Use lowecase names for modules
- Avoid adding f-strings when containing no attributes
- Remove unused logging configuration
- Implement OpenAPI conversion using Python AST
