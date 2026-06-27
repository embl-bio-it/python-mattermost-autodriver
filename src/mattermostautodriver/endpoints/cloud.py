from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Cloud"]


class Cloud(Base):

    def get_cloud_limits(self):
        """Get cloud workspace limits
        `Read in Mattermost API docs (cloud - GetCloudLimits) <https://developers.mattermost.com/api-documentation/#/operations/GetCloudLimits>`_

        """
        return self.client.get("""/api/v4/cloud/limits""")

    def get_cloud_products(self):
        """Get cloud products
        `Read in Mattermost API docs (cloud - GetCloudProducts) <https://developers.mattermost.com/api-documentation/#/operations/GetCloudProducts>`_

        """
        return self.client.get("""/api/v4/cloud/products""")

    def get_cloud_customer(self):
        """Get cloud customer
        `Read in Mattermost API docs (cloud - GetCloudCustomer) <https://developers.mattermost.com/api-documentation/#/operations/GetCloudCustomer>`_

        """
        return self.client.get("""/api/v4/cloud/customer""")

    def update_cloud_customer(
        self,
        name: str | None = None,
        email: str | None = None,
        contact_first_name: str | None = None,
        contact_last_name: str | None = None,
        num_employees: str | None = None,
    ):
        """Update cloud customer

        name:
        email:
        contact_first_name:
        contact_last_name:
        num_employees:

        `Read in Mattermost API docs (cloud - UpdateCloudCustomer) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCloudCustomer>`_

        """
        __options = {
            "name": name,
            "email": email,
            "contact_first_name": contact_first_name,
            "contact_last_name": contact_last_name,
            "num_employees": num_employees,
        }
        return self.client.put("""/api/v4/cloud/customer""", options=__options)

    def update_cloud_customer_address(self, options: Any):
        """Update cloud customer address
        `Read in Mattermost API docs (cloud - UpdateCloudCustomerAddress) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCloudCustomerAddress>`_

        """
        return self.client.put("""/api/v4/cloud/customer/address""", options=options)

    def validate_business_email(self, email: str):
        """Validate business email

        email:

        `Read in Mattermost API docs (cloud - ValidateBusinessEmail) <https://developers.mattermost.com/api-documentation/#/operations/ValidateBusinessEmail>`_

        """
        __options = {"email": email}
        return self.client.post("""/api/v4/cloud/validate-business-email""", options=__options)

    def validate_workspace_business_email(self):
        """Validate workspace business email
        `Read in Mattermost API docs (cloud - ValidateWorkspaceBusinessEmail) <https://developers.mattermost.com/api-documentation/#/operations/ValidateWorkspaceBusinessEmail>`_

        """
        return self.client.post("""/api/v4/cloud/validate-workspace-business-email""")

    def get_subscription(self):
        """Get cloud subscription
        `Read in Mattermost API docs (cloud - GetSubscription) <https://developers.mattermost.com/api-documentation/#/operations/GetSubscription>`_

        """
        return self.client.get("""/api/v4/cloud/subscription""")

    def get_endpoint_for_installation_information(self):
        """GET endpoint for Installation information
        `Read in Mattermost API docs (cloud - GetEndpointForInstallationInformation) <https://developers.mattermost.com/api-documentation/#/operations/GetEndpointForInstallationInformation>`_

        """
        return self.client.get("""/api/v4/cloud/installation""")

    def get_invoices_for_subscription(self):
        """Get cloud subscription invoices
        `Read in Mattermost API docs (cloud - GetInvoicesForSubscription) <https://developers.mattermost.com/api-documentation/#/operations/GetInvoicesForSubscription>`_

        """
        return self.client.get("""/api/v4/cloud/subscription/invoices""")

    def get_invoice_for_subscription_as_pdf(self, invoice_id: str):
        """Get cloud invoice PDF

        invoice_id: Invoice ID

        `Read in Mattermost API docs (cloud - GetInvoiceForSubscriptionAsPdf) <https://developers.mattermost.com/api-documentation/#/operations/GetInvoiceForSubscriptionAsPdf>`_

        """
        return self.client.get(f"/api/v4/cloud/subscription/invoices/{invoice_id}/pdf")

    def hosted_customer_signup_available(self):
        """Check hosted signup availability
        `Read in Mattermost API docs (cloud - HostedCustomerSignupAvailable) <https://developers.mattermost.com/api-documentation/#/operations/HostedCustomerSignupAvailable>`_

        """
        return self.client.get("""/api/v4/hosted_customer/signup_available""")

    def check_cws_connection(self):
        """Check CWS connection
        `Read in Mattermost API docs (cloud - CheckCWSConnection) <https://developers.mattermost.com/api-documentation/#/operations/CheckCWSConnection>`_

        """
        return self.client.get("""/api/v4/cloud/check-cws-connection""")

    def post_endpoint_for_cws_webhooks(self):
        """POST endpoint for CWS Webhooks
        `Read in Mattermost API docs (cloud - PostEndpointForCwsWebhooks) <https://developers.mattermost.com/api-documentation/#/operations/PostEndpointForCwsWebhooks>`_

        """
        return self.client.post("""/api/v4/cloud/webhook""")

    def get_preview_modal_data(self):
        """Get cloud preview modal data
        `Read in Mattermost API docs (cloud - GetPreviewModalData) <https://developers.mattermost.com/api-documentation/#/operations/GetPreviewModalData>`_

        """
        return self.client.get("""/api/v4/cloud/preview/modal_data""")
