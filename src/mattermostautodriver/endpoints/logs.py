from .base import Base
from typing import Any


class Logs(Base):

    def download_system_logs(self):
        """Download system logs
        `Read in Mattermost API docs (logs - DownloadSystemLogs) <https://api.mattermost.com/#tag/logs/operation/DownloadSystemLogs>`_

        """
        return self.client.get("""/api/v4/logs/download""")
