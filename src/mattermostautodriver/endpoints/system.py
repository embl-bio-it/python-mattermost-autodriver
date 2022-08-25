from .base import Base


class System(Base):
    def get_supported_timezone(self):
        """Retrieve a list of supported timezones"""
        return self.client.get("""/system/timezones""")

    def get_ping(self, params=None):
        """Check system health

        get_server_status: Check the status of the database and file storage as well
        device_id: Check whether this device id can receive push notifications
        """
        return self.client.get("""/system/ping""", params=params)

    def get_notices(self, teamId, params=None):
        """Get notices for logged in user in specified team

        teamId: ID of the team
        clientVersion: Version of the client (desktop/mobile/web) that issues the request
        locale: Client locale
        client: Client type (web/mobile-ios/mobile-android/desktop)
        """
        return self.client.get(f"/system/notices/{teamId}", params=params)

    def mark_notices_viewed(self, options):
        """Update notices as 'viewed'"""
        return self.client.put("""/system/notices/view""", options=options)

    def database_recycle(self):
        """Recycle database connections"""
        return self.client.post("""/database/recycle""")

    def test_email(self, options):
        """Send a test email"""
        return self.client.post("""/email/test""", options=options)

    def test_site_url(self, options):
        """Checks the validity of a Site URL

        site_url: The Site URL to test
        """
        return self.client.post("""/site_url/test""", options=options)

    def test_s3_connection(self, options):
        """Test AWS S3 connection"""
        return self.client.post("""/file/s3_test""", options=options)

    def get_config(self):
        """Get configuration"""
        return self.client.get("""/config""")

    def update_config(self, options):
        """Update configuration"""
        return self.client.put("""/config""", options=options)

    def reload_config(self):
        """Reload configuration"""
        return self.client.post("""/config/reload""")

    def get_client_config(self, params=None):
        """Get client configuration

        format: Must be ``old``, other formats not implemented yet
        """
        return self.client.get("""/config/client""", params=params)

    def get_environment_config(self):
        """Get configuration made through environment variables"""
        return self.client.get("""/config/environment""")

    def patch_config(self, options):
        """Patch configuration"""
        return self.client.put("""/config/patch""", options=options)

    def upload_license_file(self, files, data=None):
        """Upload license file

        license: The license to be uploaded
        """
        return self.client.post("""/license""", files=files, data=data)

    def remove_license_file(self):
        """Remove license file"""
        return self.client.delete("""/license""")

    def get_client_license(self, params=None):
        """Get client license

        format: Must be ``old``, other formats not implemented yet
        """
        return self.client.get("""/license/client""", params=params)

    def request_license_renewal_link(self):
        """Request the license renewal link"""
        return self.client.get("""/license/renewal""")

    def request_trial_license(self, options):
        """Request and install a trial license for your server

        users: Number of users requested (20% extra is going to be added)
        """
        return self.client.post("""/trial-license""", options=options)

    def get_prev_trial_license(self):
        """Get last trial license used"""
        return self.client.get("""/trial-license/prev""")

    def get_audits(self, params=None):
        """Get audits

        page: The page to select.
        per_page: The number of audits per page.
        """
        return self.client.get("""/audits""", params=params)

    def invalidate_caches(self):
        """Invalidate all the caches"""
        return self.client.post("""/caches/invalidate""")

    def get_logs(self, params=None):
        """Get logs

        page: The page to select.
        logs_per_page: The number of logs per page. There is a maximum limit of 10000 logs per page.
        """
        return self.client.get("""/logs""", params=params)

    def post_log(self, options):
        """Add log message

        level: The error level, ERROR or DEBUG
        message: Message to send to the server logs
        """
        return self.client.post("""/logs""", options=options)

    def get_analytics_old(self, params=None):
        """Get analytics

        name: Possible values are "standard", "bot_post_counts_day", "post_counts_day", "user_counts_with_posts_day" or "extra_counts"
        team_id: The team ID to filter the data by
        """
        return self.client.get("""/analytics/old""", params=params)

    def set_server_busy(self):
        """Set the server busy (high load) flag"""
        return self.client.post("""/server_busy""")

    def get_server_busy_expires(self):
        """Get server busy expiry time."""
        return self.client.get("""/server_busy""")

    def clear_server_busy(self):
        """Clears the server busy (high load) flag"""
        return self.client.delete("""/server_busy""")

    def get_redirect_location(self, params=None):
        """Get redirect location

        url: Url to check
        """
        return self.client.get("""/redirect_location""", params=params)

    def get_image_by_url(self):
        """Get an image by url"""
        return self.client.get("""/image""")

    def upgrade_to_enterprise(self):
        """Executes an inplace upgrade from Team Edition to Enterprise Edition"""
        return self.client.post("""/upgrade_to_enterprise""")

    def upgrade_to_enterprise_status(self):
        """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition"""
        return self.client.get("""/upgrade_to_enterprise/status""")

    def restart_server(self):
        """Restart the system after an upgrade from Team Edition to Enterprise Edition"""
        return self.client.post("""/restart""")

    def get_warn_metrics_status(self):
        """Get the warn metrics status (enabled or disabled)"""
        return self.client.get("""/warn_metrics/status""")

    def send_warn_metric_ack(self, warn_metric_id, options):
        """Acknowledge a warning of a metric status

        warn_metric_id: Warn Metric Id.
        forceAck: Flag which determines if the ack for the metric warning should be directly stored (without trying to send email first) or not
        """
        return self.client.post(f"/warn_metrics/ack/{warn_metric_id}", options=options)

    def send_trial_license_warn_metric_ack(self, warn_metric_id):
        """Request trial license and acknowledge a warning of a metric status

        warn_metric_id: Warn Metric Id.
        """
        return self.client.post(f"/warn_metrics/trial-license-ack/{warn_metric_id}")

    def check_integrity(self):
        """Perform a database integrity check"""
        return self.client.post("""/integrity""")

    def generate_support_packet(self):
        """Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance."""
        return self.client.get("""/system/support_packet""")

    def update_marketplace_visited_by_admin(self, options):
        """Stores that the Plugin Marketplace has been visited by at least an admin."""
        return self.client.post("""/plugins/marketplace/first_admin_visit""", options=options)
