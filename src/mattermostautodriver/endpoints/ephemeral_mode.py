from ._base import Base, FileType
from typing import Any

__all__ = ["EphemeralMode"]


class EphemeralMode(Base):

    def log_cleanup(
        self,
        posts_deleted: int | None = None,
        playbook_runs_deleted: int | None = None,
        cleanup_at: int | None = None,
        error_reason: str | None = None,
    ):
        """Log an ephemeral mode cleanup run

        posts_deleted: The number of posts deleted by the cleanup run. Required unless error_reason is provided, since a successful run with no counts records no evidence of what was deleted. If omitted, no posts_deleted value is recorded on the audit event.

        playbook_runs_deleted: The number of playbook runs deleted by the cleanup run. Required unless error_reason is provided. If omitted, no playbook_runs_deleted value is recorded on the audit event.

        cleanup_at: The time in milliseconds the cleanup run completed. Always optional; it does not satisfy the requirement for the deleted record counts. If omitted, no cleanup_at value is recorded on the audit event; the server-observed time is always recorded separately as server_ts.

        error_reason: A reason describing why the cleanup run failed. Its presence alone marks the audit event as a failure, so clients must omit this field entirely (or send null) when the run succeeded; sending an empty string records a failure with no description attached. Reasons longer than 400 characters are truncated to 400 with a trailing ellipsis rather than rejected.


        `Read in Mattermost API docs (ephemeral_mode - LogCleanup) <https://developers.mattermost.com/api-documentation/#/operations/LogCleanup>`_

        """
        __options = {
            "posts_deleted": posts_deleted,
            "playbook_runs_deleted": playbook_runs_deleted,
            "cleanup_at": cleanup_at,
            "error_reason": error_reason,
        }
        return self.client.post("""/api/v4/ephemeral_mode/cleanup""", options=__options)

    def log_offline_purge(
        self, offline_time_minutes: int | None = None, purge_at: int | None = None, error_reason: str | None = None
    ):
        """Log an ephemeral mode offline purge

        offline_time_minutes: The number of minutes the client was offline before the purge. Required unless error_reason is provided, since a successful purge with no offline time records no evidence of why it ran. If omitted, no offline_time_minutes value is recorded on the audit event.

        purge_at: The time in milliseconds the purge completed. Always optional; it does not satisfy the requirement for offline_time_minutes. If omitted, no purge_at value is recorded on the audit event; the server-observed time is always recorded separately as server_ts.

        error_reason: A reason describing why the offline purge failed. Its presence alone marks the audit event as a failure, so clients must omit this field entirely (or send null) when the purge succeeded; sending an empty string records a failure with no description attached. Reasons longer than 400 characters are truncated to 400 with a trailing ellipsis rather than rejected.


        `Read in Mattermost API docs (ephemeral_mode - LogOfflinePurge) <https://developers.mattermost.com/api-documentation/#/operations/LogOfflinePurge>`_

        """
        __options = {"offline_time_minutes": offline_time_minutes, "purge_at": purge_at, "error_reason": error_reason}
        return self.client.post("""/api/v4/ephemeral_mode/purge""", options=__options)

    def log_session_wipe(self, signature: str, wipe_at: int | None = None, error_reason: str | None = None):
        """Log an ephemeral mode session wipe

        signature: The ``signature`` field of the session wipe push notification that triggered this wipe, echoed back verbatim. The server verifies it and takes the actor, device and ack id of the audit event from its claims. Always required, including on failure reports: this endpoint accepts unauthenticated requests, so an unattributable audit record is not accepted.

        wipe_at: The time in milliseconds the wipe completed. Optional. If omitted, no wipe_at value is recorded on the audit event; the server-observed time is always recorded separately as server_ts.

        error_reason: A reason describing why the session wipe failed. Its presence alone marks the audit event as a failure, so clients must omit this field entirely (or send null) when the wipe succeeded; sending an empty string records a failure with no description attached. Reasons longer than 400 characters are truncated to 400 with a trailing ellipsis rather than rejected.


        `Read in Mattermost API docs (ephemeral_mode - LogSessionWipe) <https://developers.mattermost.com/api-documentation/#/operations/LogSessionWipe>`_

        """
        __options = {"signature": signature, "wipe_at": wipe_at, "error_reason": error_reason}
        return self.client.post("""/api/v4/ephemeral_mode/wipe""", options=__options)
