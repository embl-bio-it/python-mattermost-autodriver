from typing import IO, Mapping

# File upload types accepted by HTTPX: raw content, or tuples of
# (filename, content), (filename, content, content_type) or
# (filename, content, content_type, headers)
FileContent = IO[bytes] | bytes | str
FileType = (
    FileContent
    | tuple[str | None, FileContent]
    | tuple[str | None, FileContent, str | None]
    | tuple[str | None, FileContent, str | None, Mapping[str, str]]
)


class Base:
    def __init__(self, client):
        self.client = client
