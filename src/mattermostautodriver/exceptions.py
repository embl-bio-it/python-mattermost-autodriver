from httpx import HTTPError


class InvalidMattermostError(Exception):
    """
    Raised when mattermost returns an invalid error
    """

    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code: int = status_code


class MattermostError(HTTPError):
    """
    Base class for all known mattermost errors
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        error_id: str,
        request_id: str,
        is_oauth_error: bool,
    ):
        super().__init__(message)
        self.status_code: int = status_code
        self.error_id: str = error_id
        self.request_id: str = request_id
        self.is_oauth_error: bool = is_oauth_error


class UnknownMattermostError(MattermostError):
    """
    Raised when mattermost returns a status code that is not known
    """


class InvalidOrMissingParameters(MattermostError):
    """
    Raised when mattermost returns a
    400 Invalid or missing parameters in URL or request body
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=400,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class NoAccessTokenProvided(MattermostError):
    """
    Raised when mattermost returns a
    401 No access token provided
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=401,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class NotEnoughPermissions(MattermostError):
    """
    Raised when mattermost returns a
    403 Do not have appropriate permissions
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=403,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class ResourceNotFound(MattermostError):
    """
    Raised when mattermost returns a
    404 Resource not found
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=404,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class MethodNotAllowed(MattermostError):
    """
    Raised when mattermost returns a
    405 Method Not Allowed
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=405,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class ContentTooLarge(MattermostError):
    """
    Raised when mattermost returns a
    413 Content too large
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=413,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )


class FeatureDisabled(MattermostError):
    """
    Raised when mattermost returns a
    501 Feature is disabled
    """

    def __init__(self, message: str, error_id: str, request_id: str, is_oauth_error: bool):
        super().__init__(
            message=message,
            status_code=501,
            error_id=error_id,
            request_id=request_id,
            is_oauth_error=is_oauth_error,
        )
