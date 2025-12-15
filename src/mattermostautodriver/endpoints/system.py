from ._base import Base
from typing import Any, BinaryIO

__all__ = ["System"]


class System(Base):

    def get_supported_timezone(self):
        """Retrieve a list of supported timezones
        `Read in Mattermost API docs (system - GetSupportedTimezone) <https://developers.mattermost.com/api-documentation/#/operations/GetSupportedTimezone>`_

        """
        return self.client.get("""/api/v4/system/timezones""")

    def get_ping(
        self,
        get_server_status: bool | None = None,
        device_id: str | None = None,
        use_rest_semantics: bool | None = None,
    ):
        """Check system health

        get_server_status: Check the status of the database and file storage as well. When true, adds ``database_status`` and ``filestore_status`` to the response. If authenticated with ``manage_system`` permission, also adds ``root_status``.

        device_id: Check whether this device id can receive push notifications
        use_rest_semantics: Returns 200 status code even if the server status is unhealthy.

        `Read in Mattermost API docs (system - GetPing) <https://developers.mattermost.com/api-documentation/#/operations/GetPing>`_

        """
        __params = {
            "get_server_status": get_server_status,
            "device_id": device_id,
            "use_rest_semantics": use_rest_semantics,
        }
        return self.client.get("""/api/v4/system/ping""", params=__params)

    def get_notices(self, teamId: str, clientVersion: str, client: str, locale: str | None = None):
        """Get notices for logged in user in specified team

        teamId: ID of the team
        clientVersion: Version of the client (desktop/mobile/web) that issues the request
        locale: Client locale
        client: Client type (web/mobile-ios/mobile-android/desktop)

        `Read in Mattermost API docs (system - GetNotices) <https://developers.mattermost.com/api-documentation/#/operations/GetNotices>`_

        """
        __params = {"clientVersion": clientVersion, "locale": locale, "client": client}
        return self.client.get(f"/api/v4/system/notices/{teamId}", params=__params)

    def mark_notices_viewed(self, options: list[str]):
        """Update notices as 'viewed'
        `Read in Mattermost API docs (system - MarkNoticesViewed) <https://developers.mattermost.com/api-documentation/#/operations/MarkNoticesViewed>`_

        """
        return self.client.put("""/api/v4/system/notices/view""", options=options)

    def database_recycle(self):
        """Recycle database connections
        `Read in Mattermost API docs (system - DatabaseRecycle) <https://developers.mattermost.com/api-documentation/#/operations/DatabaseRecycle>`_

        """
        return self.client.post("""/api/v4/database/recycle""")

    def test_email(self, options: Any):
        """Send a test email
        `Read in Mattermost API docs (system - TestEmail) <https://developers.mattermost.com/api-documentation/#/operations/TestEmail>`_

        """
        return self.client.post("""/api/v4/email/test""", options=options)

    def test_notification(self):
        """Send a test notification
        `Read in Mattermost API docs (system - TestNotification) <https://developers.mattermost.com/api-documentation/#/operations/TestNotification>`_

        """
        return self.client.post("""/api/v4/notifications/test""")

    def test_site_url(self, site_url: str):
        """Checks the validity of a Site URL

        site_url: The Site URL to test

        `Read in Mattermost API docs (system - TestSiteURL) <https://developers.mattermost.com/api-documentation/#/operations/TestSiteURL>`_

        """
        __options = {"site_url": site_url}
        return self.client.post("""/api/v4/site_url/test""", options=__options)

    def test_s3_connection(self, options: Any):
        """Test AWS S3 connection
        `Read in Mattermost API docs (system - TestS3Connection) <https://developers.mattermost.com/api-documentation/#/operations/TestS3Connection>`_

        """
        return self.client.post("""/api/v4/file/s3_test""", options=options)

    def get_config(self, remove_masked: bool | None = False, remove_defaults: str | None = False):
        """Get configuration

        remove_masked: Remove masked values from the exported configuration.

        *Minimum server version*: 10.4.0

        remove_defaults: Remove default values from the exported configuration.

        *Minimum server version*: 10.4.0


        `Read in Mattermost API docs (system - GetConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetConfig>`_

        """
        __params = {"remove_masked": remove_masked, "remove_defaults": remove_defaults}
        return self.client.get("""/api/v4/config""", params=__params)

    def update_config(self, options: Any):
        """Update configuration
        `Read in Mattermost API docs (system - UpdateConfig) <https://developers.mattermost.com/api-documentation/#/operations/UpdateConfig>`_

        """
        return self.client.put("""/api/v4/config""", options=options)

    def reload_config(self):
        """Reload configuration
        `Read in Mattermost API docs (system - ReloadConfig) <https://developers.mattermost.com/api-documentation/#/operations/ReloadConfig>`_

        """
        return self.client.post("""/api/v4/config/reload""")

    def get_client_config(self):
        """Get client configuration
        `Read in Mattermost API docs (system - GetClientConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetClientConfig>`_

        """
        return self.client.get("""/api/v4/config/client""")

    def get_environment_config(self):
        """Get configuration made through environment variables
        `Read in Mattermost API docs (system - GetEnvironmentConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetEnvironmentConfig>`_

        """
        return self.client.get("""/api/v4/config/environment""")

    def patch_config(self, options: Any):
        """Patch configuration
        `Read in Mattermost API docs (system - PatchConfig) <https://developers.mattermost.com/api-documentation/#/operations/PatchConfig>`_

        """
        return self.client.put("""/api/v4/config/patch""", options=options)

    def upload_license_file(self, license: BinaryIO):
        """Upload license file

        license: The license to be uploaded

        `Read in Mattermost API docs (system - UploadLicenseFile) <https://developers.mattermost.com/api-documentation/#/operations/UploadLicenseFile>`_

        """
        __files = {"license": license}
        return self.client.post("""/api/v4/license""", files=__files)

    def remove_license_file(self):
        """Remove license file
        `Read in Mattermost API docs (system - RemoveLicenseFile) <https://developers.mattermost.com/api-documentation/#/operations/RemoveLicenseFile>`_

        """
        return self.client.delete("""/api/v4/license""")

    def get_client_license(self, format: str):
        """Get client license

        format: Must be ``old``, other formats not implemented yet

        `Read in Mattermost API docs (system - GetClientLicense) <https://developers.mattermost.com/api-documentation/#/operations/GetClientLicense>`_

        """
        __params = {"format": format}
        return self.client.get("""/api/v4/license/client""", params=__params)

    def get_license_load_metric(self):
        """Get license load metric
        `Read in Mattermost API docs (system - GetLicenseLoadMetric) <https://developers.mattermost.com/api-documentation/#/operations/GetLicenseLoadMetric>`_

        """
        return self.client.get("""/api/v4/license/load_metric""")

    def request_license_renewal_link(self):
        """Request the license renewal link
        `Read in Mattermost API docs (system - RequestLicenseRenewalLink) <https://developers.mattermost.com/api-documentation/#/operations/RequestLicenseRenewalLink>`_

        """
        return self.client.get("""/api/v4/license/renewal""")

    def request_trial_license(self, users: int):
        """Request and install a trial license for your server

        users: Number of users requested (20% extra is going to be added)

        `Read in Mattermost API docs (system - RequestTrialLicense) <https://developers.mattermost.com/api-documentation/#/operations/RequestTrialLicense>`_

        """
        __options = {"users": users}
        return self.client.post("""/api/v4/trial-license""", options=__options)

    def get_prev_trial_license(self):
        """Get last trial license used
        `Read in Mattermost API docs (system - GetPrevTrialLicense) <https://developers.mattermost.com/api-documentation/#/operations/GetPrevTrialLicense>`_

        """
        return self.client.get("""/api/v4/trial-license/prev""")

    def get_audits(self, page: int | None = 0, per_page: int | None = 60):
        """Get audits

        page: The page to select.
        per_page: The number of audits per page.

        `Read in Mattermost API docs (system - GetAudits) <https://developers.mattermost.com/api-documentation/#/operations/GetAudits>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/audits""", params=__params)

    def invalidate_caches(self):
        """Invalidate all the caches
        `Read in Mattermost API docs (system - InvalidateCaches) <https://developers.mattermost.com/api-documentation/#/operations/InvalidateCaches>`_

        """
        return self.client.post("""/api/v4/caches/invalidate""")

    def get_logs(self, page: int | None = 0, logs_per_page: str | None = "10000"):
        """Get logs

        page: The page to select.
        logs_per_page: The number of logs per page. There is a maximum limit of 10000 logs per page.

        `Read in Mattermost API docs (system - GetLogs) <https://developers.mattermost.com/api-documentation/#/operations/GetLogs>`_

        """
        __params = {"page": page, "logs_per_page": logs_per_page}
        return self.client.get("""/api/v4/logs""", params=__params)

    def post_log(self, level: str, message: str):
        """Add log message

        level: The error level, ERROR or DEBUG
        message: Message to send to the server logs

        `Read in Mattermost API docs (system - PostLog) <https://developers.mattermost.com/api-documentation/#/operations/PostLog>`_

        """
        __options = {"level": level, "message": message}
        return self.client.post("""/api/v4/logs""", options=__options)

    def get_analytics_old(self, name: str | None = "standard", team_id: str | None = None):
        """Get analytics

        name: Possible values are "standard", "bot_post_counts_day", "post_counts_day", "user_counts_with_posts_day" or "extra_counts"
        team_id: The team ID to filter the data by

        `Read in Mattermost API docs (system - GetAnalyticsOld) <https://developers.mattermost.com/api-documentation/#/operations/GetAnalyticsOld>`_

        """
        __params = {"name": name, "team_id": team_id}
        return self.client.get("""/api/v4/analytics/old""", params=__params)

    def set_server_busy(self):
        """Set the server busy (high load) flag
        `Read in Mattermost API docs (system - SetServerBusy) <https://developers.mattermost.com/api-documentation/#/operations/SetServerBusy>`_

        """
        return self.client.post("""/api/v4/server_busy""")

    def get_server_busy_expires(self):
        """Get server busy expiry time.
        `Read in Mattermost API docs (system - GetServerBusyExpires) <https://developers.mattermost.com/api-documentation/#/operations/GetServerBusyExpires>`_

        """
        return self.client.get("""/api/v4/server_busy""")

    def clear_server_busy(self):
        """Clears the server busy (high load) flag
        `Read in Mattermost API docs (system - ClearServerBusy) <https://developers.mattermost.com/api-documentation/#/operations/ClearServerBusy>`_

        """
        return self.client.delete("""/api/v4/server_busy""")

    def get_redirect_location(self, url: str):
        """Get redirect location

        url: Url to check

        `Read in Mattermost API docs (system - GetRedirectLocation) <https://developers.mattermost.com/api-documentation/#/operations/GetRedirectLocation>`_

        """
        __params = {"url": url}
        return self.client.get("""/api/v4/redirect_location""", params=__params)

    def get_image_by_url(self):
        """Get an image by url
        `Read in Mattermost API docs (system - GetImageByUrl) <https://developers.mattermost.com/api-documentation/#/operations/GetImageByUrl>`_

        """
        return self.client.get("""/api/v4/image""")

    def upgrade_to_enterprise(self):
        """Executes an inplace upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - UpgradeToEnterprise) <https://developers.mattermost.com/api-documentation/#/operations/UpgradeToEnterprise>`_

        """
        return self.client.post("""/api/v4/upgrade_to_enterprise""")

    def upgrade_to_enterprise_status(self):
        """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - UpgradeToEnterpriseStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpgradeToEnterpriseStatus>`_

        """
        return self.client.get("""/api/v4/upgrade_to_enterprise/status""")

    def is_allowed_to_upgrade_to_enterprise(self):
        """Check if the user is allowed to upgrade to Enterprise Edition
        `Read in Mattermost API docs (system - IsAllowedToUpgradeToEnterprise) <https://developers.mattermost.com/api-documentation/#/operations/IsAllowedToUpgradeToEnterprise>`_

        """
        return self.client.get("""/api/v4/upgrade_to_enterprise/allowed""")

    def restart_server(self):
        """Restart the system after an upgrade from Team Edition to Enterprise Edition
        `Read in Mattermost API docs (system - RestartServer) <https://developers.mattermost.com/api-documentation/#/operations/RestartServer>`_

        """
        return self.client.post("""/api/v4/restart""")

    def check_integrity(self):
        """Perform a database integrity check
        `Read in Mattermost API docs (system - CheckIntegrity) <https://developers.mattermost.com/api-documentation/#/operations/CheckIntegrity>`_

        """
        return self.client.post("""/api/v4/integrity""")

    def generate_support_packet(self, basic_server_logs: bool | None = None, plugin_packets: str | None = None):
        """Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance.

        basic_server_logs: Specifies whether the server should include or exclude log files. Default value is true.

        *Minimum server version*: 9.8.0

        plugin_packets: Specifies plugin identifiers whose content should be included in the Support Packet.

        *Minimum server version*: 9.8.0


        `Read in Mattermost API docs (system - GenerateSupportPacket) <https://developers.mattermost.com/api-documentation/#/operations/GenerateSupportPacket>`_

        """
        __params = {"basic_server_logs": basic_server_logs, "plugin_packets": plugin_packets}
        return self.client.get("""/api/v4/system/support_packet""", params=__params)

    def update_marketplace_visited_by_admin(self, options: Any):
        """Stores that the Plugin Marketplace has been visited by at least an admin.
        `Read in Mattermost API docs (system - UpdateMarketplaceVisitedByAdmin) <https://developers.mattermost.com/api-documentation/#/operations/UpdateMarketplaceVisitedByAdmin>`_

        """
        return self.client.post("""/api/v4/plugins/marketplace/first_admin_visit""", options=options)
