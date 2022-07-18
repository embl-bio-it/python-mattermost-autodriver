from .base import Base


class Cloud(Base):
    def get_cloud_limits(self):
        """Get cloud workspace limits"""
        return self.client.get("""/cloud/limits""")

    def get_cloud_products(self):
        """Get cloud products"""
        return self.client.get("""/cloud/products""")

    def create_customer_payment(self):
        """Create a customer setup payment intent"""
        return self.client.post("""/cloud/payment""")

    def confirm_customer_payment(self, data=None):
        """Completes the payment setup intent

        stripe_setup_intent_id:
        """
        return self.client.post("""/cloud/payment/confirm""", data=data)

    def get_cloud_customer(self):
        """Get cloud customer"""
        return self.client.get("""/cloud/customer""")

    def update_cloud_customer(self, options):
        """Update cloud customer

        name:
        email:
        contact_first_name:
        contact_last_name:
        num_employees:
        """
        return self.client.put("""/cloud/customer""", options=options)

    def update_cloud_customer_address(self, options):
        """Update cloud customer address"""
        return self.client.put("""/cloud/customer/address""", options=options)

    def get_subscription(self):
        """Get cloud subscription"""
        return self.client.get("""/cloud/subscription""")

    def get_invoices_for_subscription(self):
        """Get cloud subscription invoices"""
        return self.client.get("""/cloud/subscription/invoices""")

    def get_invoice_for_subscription_as_pdf(self, invoice_id):
        """Get cloud invoice PDF

        invoice_id: Invoice ID
        """
        return self.client.get(f"/cloud/subscription/invoices/{invoice_id}/pdf")

    def post_endpoint_for_cws_webhooks(self):
        """POST endpoint for CWS Webhooks"""
        return self.client.post("""/cloud/webhook""")

    def get_subscription_stats(self):
        """GET endpoint for cloud subscription stats"""
        return self.client.get("""/cloud/subscription/stats""")

    def send_admin_upgrade_request_email(self):
        """POST endpoint for triggering sending emails to admin with request to upgrade workspace"""
        return self.client.post("""/cloud/subscription/limitreached/invite""")

    def send_admin_upgrade_request_email_on_join(self):
        """POST endpoint for triggering sending emails to admin with request to upgrade workspace"""
        return self.client.post("""/cloud/subscription/limitreached/join""")
