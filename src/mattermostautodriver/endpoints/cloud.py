from .base import Base


class Cloud(Base):
    def get_cloud_limits(self):
        """Get cloud workspace limits
        `Read in Mattermost API docs (cloud - GetCloudLimits) <https://api.mattermost.com/#tag/cloud/operation/GetCloudLimits>`_
        """
        return self.client.get("""/api/v4/cloud/limits""")

    def get_cloud_products(self):
        """Get cloud products
        `Read in Mattermost API docs (cloud - GetCloudProducts) <https://api.mattermost.com/#tag/cloud/operation/GetCloudProducts>`_
        """
        return self.client.get("""/api/v4/cloud/products""")

    def create_customer_payment(self):
        """Create a customer setup payment intent
        `Read in Mattermost API docs (cloud - CreateCustomerPayment) <https://api.mattermost.com/#tag/cloud/operation/CreateCustomerPayment>`_
        """
        return self.client.post("""/api/v4/cloud/payment""")

    def confirm_customer_payment(self, data=None):
        """Completes the payment setup intent

        stripe_setup_intent_id:

        `Read in Mattermost API docs (cloud - ConfirmCustomerPayment) <https://api.mattermost.com/#tag/cloud/operation/ConfirmCustomerPayment>`_
        """
        return self.client.post("""/api/v4/cloud/payment/confirm""", data=data)

    def get_cloud_customer(self):
        """Get cloud customer
        `Read in Mattermost API docs (cloud - GetCloudCustomer) <https://api.mattermost.com/#tag/cloud/operation/GetCloudCustomer>`_
        """
        return self.client.get("""/api/v4/cloud/customer""")

    def update_cloud_customer(self, options):
        """Update cloud customer

        name:
        email:
        contact_first_name:
        contact_last_name:
        num_employees:

        `Read in Mattermost API docs (cloud - UpdateCloudCustomer) <https://api.mattermost.com/#tag/cloud/operation/UpdateCloudCustomer>`_
        """
        return self.client.put("""/api/v4/cloud/customer""", options=options)

    def update_cloud_customer_address(self, options):
        """Update cloud customer address
        `Read in Mattermost API docs (cloud - UpdateCloudCustomerAddress) <https://api.mattermost.com/#tag/cloud/operation/UpdateCloudCustomerAddress>`_
        """
        return self.client.put("""/api/v4/cloud/customer/address""", options=options)

    def get_subscription(self):
        """Get cloud subscription
        `Read in Mattermost API docs (cloud - GetSubscription) <https://api.mattermost.com/#tag/cloud/operation/GetSubscription>`_
        """
        return self.client.get("""/api/v4/cloud/subscription""")

    def get_endpoint_for_installation_information(self):
        """GET endpoint for Installation information
        `Read in Mattermost API docs (cloud - GetEndpointForInstallationInformation) <https://api.mattermost.com/#tag/cloud/operation/GetEndpointForInstallationInformation>`_
        """
        return self.client.get("""/api/v4/cloud/installation""")

    def get_invoices_for_subscription(self):
        """Get cloud subscription invoices
        `Read in Mattermost API docs (cloud - GetInvoicesForSubscription) <https://api.mattermost.com/#tag/cloud/operation/GetInvoicesForSubscription>`_
        """
        return self.client.get("""/api/v4/cloud/subscription/invoices""")

    def get_invoice_for_subscription_as_pdf(self, invoice_id):
        """Get cloud invoice PDF

        invoice_id: Invoice ID

        `Read in Mattermost API docs (cloud - GetInvoiceForSubscriptionAsPdf) <https://api.mattermost.com/#tag/cloud/operation/GetInvoiceForSubscriptionAsPdf>`_
        """
        return self.client.get(f"/api/v4/cloud/subscription/invoices/{invoice_id}/pdf")

    def post_endpoint_for_cws_webhooks(self):
        """POST endpoint for CWS Webhooks
        `Read in Mattermost API docs (cloud - PostEndpointForCwsWebhooks) <https://api.mattermost.com/#tag/cloud/operation/PostEndpointForCwsWebhooks>`_
        """
        return self.client.post("""/api/v4/cloud/webhook""")
