from ._base import Base

__all__ = ["Root"]


class Root(Base):

    def acknowledge_notification(self):
        """Acknowledge receiving of a notification
        `Read in Mattermost API docs (root - AcknowledgeNotification) <https://developers.mattermost.com/api-documentation/#/operations/AcknowledgeNotification>`_

        """
        return self.client.post("""/api/v4/notifications/ack""")
