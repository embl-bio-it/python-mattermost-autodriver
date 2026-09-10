from ._base import Base, FileType
from typing import Any

__all__ = ["ScheduledRecaps"]


class ScheduledRecaps(Base):

    def create_scheduled_recap(
        self,
        title: str,
        days_of_week: int,
        time_of_day: str,
        timezone: str,
        time_period: str,
        channel_mode: str,
        agent_id: str,
        channel_ids: list[str] | None = None,
        custom_instructions: str | None = None,
        is_recurring: bool | None = None,
    ):
        """Create a scheduled recap

        title: Title for the scheduled recap
        days_of_week: Bitmask for days of the week the recap should run. Sun=1, Mon=2, Tue=4, Wed=8, Thu=16, Fri=32, Sat=64. For example, weekdays = 62, every day = 127.

        time_of_day: Time of day in HH:MM format (e.g., "09:00")
        timezone: IANA timezone (e.g., "America/New_York")
        time_period: The lookback period for the recap content
        channel_mode: How channels are selected for the recap
        channel_ids: List of channel IDs to include (required when channel_mode is "specific")
        custom_instructions: Custom AI instructions for the recap
        agent_id: ID of the AI agent to use for generating the recap
        is_recurring: Whether the recap runs on a recurring schedule or just once

        `Read in Mattermost API docs (scheduled_recaps - CreateScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/CreateScheduledRecap>`_

        """
        __options = {
            "title": title,
            "days_of_week": days_of_week,
            "time_of_day": time_of_day,
            "timezone": timezone,
            "time_period": time_period,
            "channel_mode": channel_mode,
            "channel_ids": channel_ids,
            "custom_instructions": custom_instructions,
            "agent_id": agent_id,
            "is_recurring": is_recurring,
        }
        return self.client.post("""/api/v4/scheduled_recaps""", options=__options)

    def get_scheduled_recaps(self, page: int | None = None, per_page: int | None = None):
        """Get current user's scheduled recaps

        page: The page to select. Default: ``0`` (applied server-side when omitted)
        per_page: The number of scheduled recaps per page. Default: ``60`` (applied server-side when omitted)

        `Read in Mattermost API docs (scheduled_recaps - GetScheduledRecaps) <https://developers.mattermost.com/api-documentation/#/operations/GetScheduledRecaps>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/scheduled_recaps""", params=__params)

    def get_scheduled_recap(self, scheduled_recap_id: str):
        """Get a scheduled recap

        scheduled_recap_id: Scheduled Recap GUID

        `Read in Mattermost API docs (scheduled_recaps - GetScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/GetScheduledRecap>`_

        """
        return self.client.get(f"/api/v4/scheduled_recaps/{scheduled_recap_id}")

    def update_scheduled_recap(
        self,
        scheduled_recap_id: str,
        title: str | None = None,
        days_of_week: int | None = None,
        time_of_day: str | None = None,
        timezone: str | None = None,
        time_period: str | None = None,
        channel_mode: str | None = None,
        channel_ids: list[str] | None = None,
        custom_instructions: str | None = None,
        agent_id: str | None = None,
        is_recurring: bool | None = None,
        enabled: bool | None = None,
    ):
        """Update a scheduled recap

        scheduled_recap_id: Scheduled Recap GUID
        title: Title for the scheduled recap
        days_of_week: Bitmask for days of the week the recap should run. Sun=1, Mon=2, Tue=4, Wed=8, Thu=16, Fri=32, Sat=64.

        time_of_day: Time of day in HH:MM format (e.g., "09:00")
        timezone: IANA timezone (e.g., "America/New_York")
        time_period: The lookback period for the recap content
        channel_mode: How channels are selected for the recap
        channel_ids: List of channel IDs to include (required when channel_mode is "specific")
        custom_instructions: Custom AI instructions for the recap
        agent_id: ID of the AI agent to use for generating the recap
        is_recurring: Whether the recap runs on a recurring schedule or just once
        enabled: Whether the scheduled recap is active

        `Read in Mattermost API docs (scheduled_recaps - UpdateScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/UpdateScheduledRecap>`_

        """
        __options = {
            "title": title,
            "days_of_week": days_of_week,
            "time_of_day": time_of_day,
            "timezone": timezone,
            "time_period": time_period,
            "channel_mode": channel_mode,
            "channel_ids": channel_ids,
            "custom_instructions": custom_instructions,
            "agent_id": agent_id,
            "is_recurring": is_recurring,
            "enabled": enabled,
        }
        return self.client.put(f"/api/v4/scheduled_recaps/{scheduled_recap_id}", options=__options)

    def delete_scheduled_recap(self, scheduled_recap_id: str):
        """Delete a scheduled recap

        scheduled_recap_id: Scheduled Recap GUID

        `Read in Mattermost API docs (scheduled_recaps - DeleteScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/DeleteScheduledRecap>`_

        """
        return self.client.delete(f"/api/v4/scheduled_recaps/{scheduled_recap_id}")

    def pause_scheduled_recap(self, scheduled_recap_id: str):
        """Pause a scheduled recap

        scheduled_recap_id: Scheduled Recap GUID

        `Read in Mattermost API docs (scheduled_recaps - PauseScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/PauseScheduledRecap>`_

        """
        return self.client.post(f"/api/v4/scheduled_recaps/{scheduled_recap_id}/pause")

    def resume_scheduled_recap(self, scheduled_recap_id: str):
        """Resume a scheduled recap

        scheduled_recap_id: Scheduled Recap GUID

        `Read in Mattermost API docs (scheduled_recaps - ResumeScheduledRecap) <https://developers.mattermost.com/api-documentation/#/operations/ResumeScheduledRecap>`_

        """
        return self.client.post(f"/api/v4/scheduled_recaps/{scheduled_recap_id}/resume")
