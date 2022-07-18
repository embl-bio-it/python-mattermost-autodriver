from .base import Base


class Root(Base):
    def acknowledge_notification(self):
        """Acknowledge receiving of a notification"""
        return self.client.post("""/notifications/ack""")
