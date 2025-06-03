from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Logs"]


class Logs(Base):

    def download_system_logs(self):
        """Download system logs
        `Read in Mattermost API docs (logs - DownloadSystemLogs) <https://developers.mattermost.com/api-documentation/#/operations/DownloadSystemLogs>`_

        """
        return self.client.get("""/api/v4/logs/download""")
