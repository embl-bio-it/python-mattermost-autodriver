from ._base import Base, FileType
from typing import Any

__all__ = ["DeliveryTracking"]


class DeliveryTracking(Base):

    def get_delivery_tracking_config(self):
        """Get the post delivery audit logging configuration
        `Read in Mattermost API docs (delivery_tracking - GetDeliveryTrackingConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetDeliveryTrackingConfig>`_

        """
        return self.client.get("""/api/v4/delivery_tracking/config""")

    def update_delivery_tracking_config(self, options: Any):
        """Update the post delivery audit logging configuration
        `Read in Mattermost API docs (delivery_tracking - UpdateDeliveryTrackingConfig) <https://developers.mattermost.com/api-documentation/#/operations/UpdateDeliveryTrackingConfig>`_

        """
        return self.client.put("""/api/v4/delivery_tracking/config""", options=options)
