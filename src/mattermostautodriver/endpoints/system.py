from .base import Base


class System(Base):
    def get_supported_timezone(self):
        """Retrieve a list of supported timezones
        `Read in Mattermost API docs (system - GetSupportedTimezone) <https://api.mattermost.com/#tag/system/operation/GetSupportedTimezone>`_
        """
        return self.client.get("""/api/v4/system/timezones""")

    def get_ping(self, params=None):
        """Check system health

        get_server_status: Check the status of the database and file storage as well
        device_id: Check whether this device id can receive push notifications

        `Read in Mattermost API docs (system - GetPing) <https://api.mattermost.com/#tag/system/operation/GetPing>`_
        """
        return self.client.get("""/api/v4/system/ping""", params=params)

    def get_notices(self, teamId, params=None):
        """Get notices for logged in user in specified team

        teamId: ID of the team
        clientVersion: Version of the client (desktop/mobile/web) that issues the request
        locale: Client locale
        client: Client type (web/mobile-ios/mobile-android/desktop)

        `Read in Mattermost API docs (system - GetNotices) <https://api.mattermost.com/#tag/system/operation/GetNotices>`_
        """
        return self.client.get(f"/api/v4/system/notices/{teamId}", params=params)

    def mark_notices_viewed(self, options):
        """Update notices as 'viewed'
        `Read in Mattermost API docs (system - MarkNoticesViewed) <https://api.mattermost.com/#tag/system/operation/MarkNoticesViewed>`_
        """
        return self.client.put("""/api/v4/system/notices/view""", options=options)

    def database_recycle(self):
        """Recycle database connections
        `Read in Mattermost API docs (system - DatabaseRecycle) <https://api.mattermost.com/#tag/system/operation/DatabaseRecycle>`_
        """
        return self.client.post("""/api/v4/database/recycle""")

    def test_email(self, options):
        """Send a test email
        `Read in Mattermost API docs (system - TestEmail) <https://api.mattermost.com/#tag/system/operation/TestEmail>`_
        """
        return self.client.post("""/api/v4/email/test""", options=options)

    def test_site_url(self, options):
        """Checks the validity of a Site URL

        site_url: The Site URL to test

        `Read in Mattermost API docs (system - TestSiteURL) <https://api.mattermost.com/#tag/system/operation/TestSiteURL>`_
        """
        return self.client.post("""/api/v4/site_url/test""", options=options)

    def test_s3_connection(self, options):
        """Test AWS S3 connection
        `Read in Mattermost API docs (system - TestS3Connection) <https://api.mattermost.com/#tag/system/operation/TestS3Connection>`_
        """
        return self.client.post("""/api/v4/file/s3_test""", options=options)

    def get_config(self):
        """Get configuration
        `Read in Mattermost API docs (system - GetConfig) <https://api.mattermost.com/#tag/system/operation/GetConfig>`_
        """
        return self.client.get("""/api/v4/config""")

    def update_config(self, options):
        """Update configuration
        `Read in Mattermost API docs (system - UpdateConfig) <https://api.mattermost.com/#tag/system/operation/UpdateConfig>`_
        """
        return self.client.put("""/api/v4/config""", options=options)

    def reload_config(self):
        """Reload configuration
        `Read in Mattermost API docs (system - ReloadConfig) <https://api.mattermost.com/#tag/system/operation/ReloadConfig>`_
        """
        return self.client.post("""/api/v4/config/reload""")

    def get_client_config(self, params=None):
        """Get client configuration

        format: Must be ``old``, other formats not implemented yet

        `Read in Mattermost API docs (system - GetClientConfig) <https://api.mattermost.com/#tag/system/operation/GetClientConfig>`_
        """
        return self.client.get("""/api/v4/config/client""", params=params)

    def get_environment_config(self):
        """Get configuration made through environment variables
        `Read in Mattermost API docs (system - GetEnvironmentConfig) <https://api.mattermost.com/#tag/system/operation/GetEnvironmentConfig>`_
        """
        return self.client.get("""/api/v4/config/environment""")

    def patch_config(self, options):
        """Patch configuration
        `Read in Mattermost API docs (system - PatchConfig) <https://api.mattermost.com/#tag/system/operation/PatchConfig>`_
        """
        return self.client.put("""/api/v4/config/patch""", options=options)

    def upload_license_file(self, files, data=None):
        """Upload license file

        license: The license to be uploaded

        `Read in Mattermost API docs (system - UploadLicenseFile) <https://api.mattermost.com/#tag/system/operation/UploadLicenseFile>`_
        """
        return self.client.post("""/api/v4/license""", files=files, data=data)

    def remove_license_file(self):
        """Remove license file
        `Read in Mattermost API docs (system - RemoveLicenseFile) <https://api.mattermost.com/#tag/system/operation/RemoveLicenseFile>`_
        """
        return self.client.delete("""/api/v4/license""")

    def get_client_license(self, params=None):
        """Get client license

        format: Must be ``old``, other formats not implemented yet

        `Read in Mattermost API docs (system - GetClientLicense) <https://api.mattermost.com/#tag/system/operation/GetClientLicense>`_
        """
        return self.client.get("""/api/v4/license/client""", params=params)

    def request_license_renewal_link(self):
        """Request the license renewal link
        `Read in Mattermost API docs (system - RequestLicenseRenewalLink) <https://api.mattermost.com/#tag/system/operation/RequestLicenseRenewalLink>`_
        """
        return self.client.get("""/api/v4/license/renewal""")

    def request_trial_license(self, options):
        """Request and install a trial license for your server

        users: Number of users requested (20% extra is going to be added)

        `Read in Mattermost API docs (system - RequestTrialLicense) <https://api.mattermost.com/#tag/system/operation/RequestTrialLicense>`_
        """
        return self.client.post("""/api/v4/trial-license""", options=options)

    def get_prev_trial_license(self):
        """Get last trial license used
        `Read in Mattermost API docs (system - GetPrevTrialLicense) <https://api.mattermost.com/#tag/system/operation/GetPrevTrialLicense>`_
        """
        return self.client.get("""/api/v4/trial-license/prev""")

    def get_audits(self, params=None):
        """Get audits

        page: The page to select.
        per_page: The number of audits per page.

        `Read in Mattermost API docs (system - GetAudits) <https://api.mattermost.com/#tag/system/operation/GetAudits>`_
        """
        return self.client.get("""/api/v4/audits""", params=params)

    def invalidate_caches(self):
        """Invalidate all the caches
        `Read in Mattermost API docs (system - InvalidateCaches) <https://api.mattermost.com/#tag/system/operation/InvalidateCaches>`_
        """
        return self.client.post("""/api/v4/caches/invalidate""")

    def get_logs(self, params=None):
        """Get logs

        page: The page to select.
        logs_per_page: The number of logs per page. There is a maximum limit of 10000 logs per page.

        `Read in Mattermost API docs (system - GetLogs) <https://api.mattermost.com/#tag/system/operation/GetLogs>`_
        """
        return self.client.get("""/api/v4/logs""", params=params)

    def post_log(self, options):
        """Add log message

        level: The error level, ERROR or DEBUG
        message: Message to send to the server logs

        `Read in Mattermost API docs (system - PostLog) <https://api.mattermost.com/#tag/system/operation/PostLog>`_
        """
        return self.client.post("""/api/v4/logs""", options=options)

    def get_analytics_old(self, params=None):
        """Get analytics

        name: Possible values are "standard", "bot_post_counts_day", "post_counts_day", "user_counts_with_posts_day" or "extra_counts"
        team_id: The team ID to filter the data by

        `Read in Mattermost API docs (system - GetAnalyticsOld) <https://api.mattermost.com/#tag/system/operation/GetAnalyticsOld>`_
        """
        return self.client.get("""/api/v4/analytics/old""", params=params)

    def set_server_busy(self):
        """Set the server busy (high load) flag
        `Read in Mattermost API docs (system - SetServerBusy) <https://api.mattermost.com/#tag/system/operation/SetServerBusy>`_
        """
        return self.client.post("""/api/v4/server_busy""")

    def get_server_busy_expires(self):
        """Get server busy expiry time.
        `Read in Mattermost API docs (system - GetServerBusyExpires) <https://api.mattermost.com/#tag/system/operation/GetServerBusyExpires>`_
        """
        return self.client.get("""/api/v4/server_busy""")

    def clear_server_busy(self):
        """Clears the server busy (high load) flag
        `Read in Mattermost API docs (system - ClearServerBusy) <https://api.mattermost.com/#tag/system/operation/ClearServerBusy>`_
        """
        return self.client.delete("""/api/v4/server_busy""")

    def get_redirect_location(self, params=None):
        """Get redirect location

        url: Url to check

        `Read in Mattermost API docs (system - GetRedirectLocation) <https://api.mattermost.com/#tag/system/operation/GetRedirectLocation>`_
        """
        return self.client.get("""/api/v4/redirect_location""", params=params)

    def get_image_by_url(self):
        """Get an image by url
        `Read in Mattermost API docs (system - GetImageByUrl) <https://api.mattermost.com/#tag/system/operation/GetImageByUrl>`_
        """
        return self.client.get("""/api/v4/image""")

    def upgrade_to_enterprise(self):
        """Executes an inplace upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - UpgradeToEnterprise) <https://api.mattermost.com/#tag/system/operation/UpgradeToEnterprise>`_
        """
        return self.client.post("""/api/v4/upgrade_to_enterprise""")

    def upgrade_to_enterprise_status(self):
        """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - UpgradeToEnterpriseStatus) <https://api.mattermost.com/#tag/system/operation/UpgradeToEnterpriseStatus>`_
        """
        return self.client.get("""/api/v4/upgrade_to_enterprise/status""")

    def restart_server(self):
        """Restart the system after an upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - RestartServer) <https://api.mattermost.com/#tag/system/operation/RestartServer>`_
        """
        return self.client.post("""/api/v4/restart""")

    def get_warn_metrics_status(self):
        """Get the warn metrics status (enabled or disabled)
        `Read in Mattermost API docs (system - GetWarnMetricsStatus) <https://api.mattermost.com/#tag/system/operation/GetWarnMetricsStatus>`_
        """
        return self.client.get("""/api/v4/warn_metrics/status""")

    def send_warn_metric_ack(self, warn_metric_id, options):
        """Acknowledge a warning of a metric status

        warn_metric_id: Warn Metric Id.
        forceAck: Flag which determines if the ack for the metric warning should be directly stored (without trying to send email first) or not

        `Read in Mattermost API docs (system - SendWarnMetricAck) <https://api.mattermost.com/#tag/system/operation/SendWarnMetricAck>`_
        """
        return self.client.post(f"/api/v4/warn_metrics/ack/{warn_metric_id}", options=options)

    def send_trial_license_warn_metric_ack(self, warn_metric_id):
        """Request trial license and acknowledge a warning of a metric status

        warn_metric_id: Warn Metric Id.

        `Read in Mattermost API docs (system - SendTrialLicenseWarnMetricAck) <https://api.mattermost.com/#tag/system/operation/SendTrialLicenseWarnMetricAck>`_
        """
        return self.client.post(f"/api/v4/warn_metrics/trial-license-ack/{warn_metric_id}")

    def check_integrity(self):
        """Perform a database integrity check
        `Read in Mattermost API docs (system - CheckIntegrity) <https://api.mattermost.com/#tag/system/operation/CheckIntegrity>`_
        """
        return self.client.post("""/api/v4/integrity""")

    def generate_support_packet(self):
        """Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance.
        `Read in Mattermost API docs (system - GenerateSupportPacket) <https://api.mattermost.com/#tag/system/operation/GenerateSupportPacket>`_
        """
        return self.client.get("""/api/v4/system/support_packet""")

    def update_marketplace_visited_by_admin(self, options):
        """Stores that the Plugin Marketplace has been visited by at least an admin.
        `Read in Mattermost API docs (system - UpdateMarketplaceVisitedByAdmin) <https://api.mattermost.com/#tag/system/operation/UpdateMarketplaceVisitedByAdmin>`_
        """
        return self.client.post("""/api/v4/plugins/marketplace/first_admin_visit""", options=options)
