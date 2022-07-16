from .base import Base


class Terms_of_service(Base):
    def register_terms_of_service_action(self, user_id, options):
        """Records user action when they accept or decline custom terms of service

        user_id: User GUID
        serviceTermsId: terms of service ID on which the user is acting on
        accepted: true or false, indicates whether the user accepted or rejected the terms of service.
        """
        return self.client.post(f"/users/{user_id}/terms_of_service", options=options)

    def get_user_terms_of_service(self, user_id):
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/terms_of_service")

    def get_terms_of_service(self):
        """Get latest terms of service"""
        return self.client.get("""/terms_of_service""")

    def create_terms_of_service(self):
        """Creates a new terms of service"""
        return self.client.post("""/terms_of_service""")
