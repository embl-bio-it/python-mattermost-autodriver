from httpx import HTTPError


class MattermostError(HTTPError):
    """
    Base class for all mattermost errors
    """

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class InvalidOrMissingParameters(MattermostError):
    """
    Raised when mattermost returns a
    400 Invalid or missing parameters in URL or request body
    """

    def __init__(self, message):
        super().__init__(message, 400)


class NoAccessTokenProvided(MattermostError):
    """
    Raised when mattermost returns a
    401 No access token provided
    """

    def __init__(self, message):
        super().__init__(message, 401)


class NotEnoughPermissions(MattermostError):
    """
    Raised when mattermost returns a
    403 Do not have appropriate permissions
    """

    def __init__(self, message):
        super().__init__(message, 403)


class ResourceNotFound(MattermostError):
    """
    Raised when mattermost returns a
    404 Resource not found
    """

    def __init__(self, message):
        super().__init__(message, 404)


class MethodNotAllowed(MattermostError):
    """
    Raised when mattermost returns a
    405 Method Not Allowed
    """

    def __init__(self, message):
        super().__init__(message, 405)


class ContentTooLarge(MattermostError):
    """
    Raised when mattermost returns a
    413 Content too large
    """

    def __init__(self, message):
        super().__init__(message, 413)


class FeatureDisabled(MattermostError):
    """
    Raised when mattermost returns a
    501 Feature is disabled
    """

    def __init__(self, message):
        super().__init__(message, 501)
