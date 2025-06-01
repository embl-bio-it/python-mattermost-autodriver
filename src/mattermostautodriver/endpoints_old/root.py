from ._base import Base

__all__ = ["Root"]


class Root(Base):

    def acknowledge_notification(self):
        """Acknowledge receiving of a notification
        `Read in Mattermost API docs (root - AcknowledgeNotification) <https://api.mattermost.com/#tag/root/operation/AcknowledgeNotification>`_

        """
        return self.client.post("""/api/v4/notifications/ack""")
