from .base import Base


class Cloud(Base):
    def get_cloud_limits(self):
        """Get cloud workspace limits
        `Read in Mattermost API docs (cloud - GetCloudLimits) <https://api.mattermost.com/#tag/cloud/operation/GetCloudLimits>`_
        """
        return self.client.get("""/cloud/limits""")

    def get_cloud_products(self):
        """Get cloud products
        `Read in Mattermost API docs (cloud - GetCloudProducts) <https://api.mattermost.com/#tag/cloud/operation/GetCloudProducts>`_
        """
        return self.client.get("""/cloud/products""")

    def create_customer_payment(self):
        """Create a customer setup payment intent
        `Read in Mattermost API docs (cloud - CreateCustomerPayment) <https://api.mattermost.com/#tag/cloud/operation/CreateCustomerPayment>`_
        """
        return self.client.post("""/cloud/payment""")

    def confirm_customer_payment(self, data=None):
        """Completes the payment setup intent

        stripe_setup_intent_id:

        `Read in Mattermost API docs (cloud - ConfirmCustomerPayment) <https://api.mattermost.com/#tag/cloud/operation/ConfirmCustomerPayment>`_
        """
        return self.client.post("""/cloud/payment/confirm""", data=data)

    def get_cloud_customer(self):
        """Get cloud customer
        `Read in Mattermost API docs (cloud - GetCloudCustomer) <https://api.mattermost.com/#tag/cloud/operation/GetCloudCustomer>`_
        """
        return self.client.get("""/cloud/customer""")

    def update_cloud_customer(self, options):
        """Update cloud customer

        name:
        email:
        contact_first_name:
        contact_last_name:
        num_employees:

        `Read in Mattermost API docs (cloud - UpdateCloudCustomer) <https://api.mattermost.com/#tag/cloud/operation/UpdateCloudCustomer>`_
        """
        return self.client.put("""/cloud/customer""", options=options)

    def update_cloud_customer_address(self, options):
        """Update cloud customer address
        `Read in Mattermost API docs (cloud - UpdateCloudCustomerAddress) <https://api.mattermost.com/#tag/cloud/operation/UpdateCloudCustomerAddress>`_
        """
        return self.client.put("""/cloud/customer/address""", options=options)

    def get_subscription(self):
        """Get cloud subscription
        `Read in Mattermost API docs (cloud - GetSubscription) <https://api.mattermost.com/#tag/cloud/operation/GetSubscription>`_
        """
        return self.client.get("""/cloud/subscription""")

    def get_invoices_for_subscription(self):
        """Get cloud subscription invoices
        `Read in Mattermost API docs (cloud - GetInvoicesForSubscription) <https://api.mattermost.com/#tag/cloud/operation/GetInvoicesForSubscription>`_
        """
        return self.client.get("""/cloud/subscription/invoices""")

    def get_invoice_for_subscription_as_pdf(self, invoice_id):
        """Get cloud invoice PDF

        invoice_id: Invoice ID

        `Read in Mattermost API docs (cloud - GetInvoiceForSubscriptionAsPdf) <https://api.mattermost.com/#tag/cloud/operation/GetInvoiceForSubscriptionAsPdf>`_
        """
        return self.client.get(f"/cloud/subscription/invoices/{invoice_id}/pdf")

    def post_endpoint_for_cws_webhooks(self):
        """POST endpoint for CWS Webhooks
        `Read in Mattermost API docs (cloud - PostEndpointForCwsWebhooks) <https://api.mattermost.com/#tag/cloud/operation/PostEndpointForCwsWebhooks>`_
        """
        return self.client.post("""/cloud/webhook""")

    def get_subscription_stats(self):
        """GET endpoint for cloud subscription stats
        `Read in Mattermost API docs (cloud - GetSubscriptionStats) <https://api.mattermost.com/#tag/cloud/operation/GetSubscriptionStats>`_
        """
        return self.client.get("""/cloud/subscription/stats""")

    def send_admin_upgrade_request_email(self):
        """POST endpoint for triggering sending emails to admin with request to upgrade workspace
        `Read in Mattermost API docs (cloud - SendAdminUpgradeRequestEmail) <https://api.mattermost.com/#tag/cloud/operation/SendAdminUpgradeRequestEmail>`_
        """
        return self.client.post("""/cloud/subscription/limitreached/invite""")

    def send_admin_upgrade_request_email_on_join(self):
        """POST endpoint for triggering sending emails to admin with request to upgrade workspace
        `Read in Mattermost API docs (cloud - SendAdminUpgradeRequestEmailOnJoin) <https://api.mattermost.com/#tag/cloud/operation/SendAdminUpgradeRequestEmailOnJoin>`_
        """
        return self.client.post("""/cloud/subscription/limitreached/join""")
