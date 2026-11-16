from ._base import Base, FileType
from typing import Any

__all__ = ["Health"]


class Health(Base):

    def get_health_findings(self, muted: str | None = None):
        """Get health findings

        muted: Which findings to return by mute state. Omit to return only unmuted findings; ``included``
        returns muted and unmuted findings; ``only`` returns only muted findings.


        `Read in Mattermost API docs (health - GetHealthFindings) <https://developers.mattermost.com/api-documentation/#/operations/GetHealthFindings>`_

        """
        __params = {"muted": muted}
        return self.client.get("""/api/v4/health/findings""", params=__params)

    def mute_health_finding(self, fingerprint: str):
        """Mute a health finding

        fingerprint: The finding's fingerprint, 32 lowercase hexadecimal characters.

        `Read in Mattermost API docs (health - MuteHealthFinding) <https://developers.mattermost.com/api-documentation/#/operations/MuteHealthFinding>`_

        """
        return self.client.post(f"/api/v4/health/findings/{fingerprint}/mute")

    def unmute_health_finding(self, fingerprint: str):
        """Unmute a health finding

        fingerprint: The finding's fingerprint, 32 lowercase hexadecimal characters.

        `Read in Mattermost API docs (health - UnmuteHealthFinding) <https://developers.mattermost.com/api-documentation/#/operations/UnmuteHealthFinding>`_

        """
        return self.client.delete(f"/api/v4/health/findings/{fingerprint}/mute")
