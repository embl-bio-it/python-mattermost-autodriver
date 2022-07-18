from .base import Base


class Threads(Base):
    def get_user_threads(self, user_id, team_id, params=None):
        """Get all threads that user is following

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        since: Since filters the threads based on their LastUpdateAt timestamp.
        deleted: Deleted will specify that even deleted threads should be returned (For mobile sync).
        extended: Extended will enrich the response with participant details.
        page: Page specifies which part of the results to return, by PageSize.
        pageSize: PageSize specifies the size of the returned chunk of results.
        totalsOnly: Setting this to true will only return the total counts.
        """
        return self.client.get(f"/users/{user_id}/teams/{team_id}/threads", params=params)

    def get_thread_mention_counts_by_channel(self, user_id, team_id):
        """Get all unread mention counts from followed threads, per-channel

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        """
        return self.client.get(f"/users/{user_id}/teams/{team_id}/threads/mention_counts")

    def update_threads_read_for_user(self, user_id, team_id):
        """Mark all threads that user is following as read

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        """
        return self.client.put(f"/users/{user_id}/teams/{team_id}/threads/read")

    def update_thread_read_for_user(self, user_id, team_id, thread_id, timestamp):
        """Mark a thread that user is following read state to the timestamp

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to update
        timestamp: The timestamp to which the thread's "last read" state will be reset.
        """
        return self.client.put(f"/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}")

    def start_following_thread(self, user_id, team_id, thread_id):
        """Start following a thread

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to follow
        """
        return self.client.put(f"/users/{user_id}/teams/{team_id}/threads/{thread_id}/following")

    def stop_following_thread(self, user_id, team_id, thread_id):
        """Stop following a thread

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to update
        """
        return self.client.delete(f"/users/{user_id}/teams/{team_id}/threads/{thread_id}/following")

    def get_user_thread(self, user_id, team_id, thread_id):
        """Get a thread followed by the user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        team_id: The ID of the team in which the thread is.
        thread_id: The ID of the thread to follow
        """
        return self.client.get(f"/users/{user_id}/teams/{team_id}/threads/{thread_id}")
