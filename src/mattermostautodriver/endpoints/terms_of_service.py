from ._base import Base
from typing import Any, BinaryIO

__all__ = ["TermsOfService"]


class TermsOfService(Base):

    def register_terms_of_service_action(self, user_id: str, serviceTermsId: str, accepted: str):
        """Records user action when they accept or decline custom terms of service

        user_id: User GUID
        serviceTermsId: terms of service ID on which the user is acting on
        accepted: true or false, indicates whether the user accepted or rejected the terms of service.

        `Read in Mattermost API docs (terms_of_service - RegisterTermsOfServiceAction) <https://developers.mattermost.com/api-documentation/#/operations/RegisterTermsOfServiceAction>`_

        """
        __options = {"serviceTermsId": serviceTermsId, "accepted": accepted}
        return self.client.post(f"/api/v4/users/{user_id}/terms_of_service", options=__options)

    def get_user_terms_of_service(self, user_id: str):
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        user_id: User GUID

        `Read in Mattermost API docs (terms_of_service - GetUserTermsOfService) <https://developers.mattermost.com/api-documentation/#/operations/GetUserTermsOfService>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/terms_of_service")

    def get_terms_of_service(self):
        """Get latest terms of service
        `Read in Mattermost API docs (terms_of_service - GetTermsOfService) <https://developers.mattermost.com/api-documentation/#/operations/GetTermsOfService>`_

        """
        return self.client.get("""/api/v4/terms_of_service""")

    def create_terms_of_service(self):
        """Creates a new terms of service
        `Read in Mattermost API docs (terms_of_service - CreateTermsOfService) <https://developers.mattermost.com/api-documentation/#/operations/CreateTermsOfService>`_

        """
        return self.client.post("""/api/v4/terms_of_service""")
