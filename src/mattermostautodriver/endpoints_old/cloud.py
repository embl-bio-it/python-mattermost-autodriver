from ._base import Base

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

    def create_customer_payment(self):
        """Create a customer setup payment intent
        `Read in Mattermost API docs (cloud - CreateCustomerPayment) <https://developers.mattermost.com/api-documentation/#/operations/CreateCustomerPayment>`_

        """
        return self.client.post("""/api/v4/cloud/payment""")

    def confirm_customer_payment(self, data=None):
        """Completes the payment setup intent

        stripe_setup_intent_id:

        `Read in Mattermost API docs (cloud - ConfirmCustomerPayment) <https://developers.mattermost.com/api-documentation/#/operations/ConfirmCustomerPayment>`_

        """
        return self.client.post("""/api/v4/cloud/payment/confirm""", data=data)

    def get_cloud_customer(self):
        """Get cloud customer
        `Read in Mattermost API docs (cloud - GetCloudCustomer) <https://developers.mattermost.com/api-documentation/#/operations/GetCloudCustomer>`_

        """
        return self.client.get("""/api/v4/cloud/customer""")

    def update_cloud_customer(self, options):
        """Update cloud customer

        name:
        email:
        contact_first_name:
        contact_last_name:
        num_employees:

        `Read in Mattermost API docs (cloud - UpdateCloudCustomer) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCloudCustomer>`_

        """
        return self.client.put("""/api/v4/cloud/customer""", options=options)

    def update_cloud_customer_address(self, options):
        """Update cloud customer address
        `Read in Mattermost API docs (cloud - UpdateCloudCustomerAddress) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCloudCustomerAddress>`_

        """
        return self.client.put("""/api/v4/cloud/customer/address""", options=options)

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

    def get_invoice_for_subscription_as_pdf(self, invoice_id):
        """Get cloud invoice PDF

        invoice_id: Invoice ID

        `Read in Mattermost API docs (cloud - GetInvoiceForSubscriptionAsPdf) <https://developers.mattermost.com/api-documentation/#/operations/GetInvoiceForSubscriptionAsPdf>`_

        """
        return self.client.get(f"/api/v4/cloud/subscription/invoices/{invoice_id}/pdf")

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
