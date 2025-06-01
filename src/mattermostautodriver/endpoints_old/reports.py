from ._base import Base

__all__ = ["Reports"]


class Reports(Base):

    def start_batch_users_export(self):
        """Starts a job to export the users to a report file.
        `Read in Mattermost API docs (reports - StartBatchUsersExport) <https://api.mattermost.com/#tag/reports/operation/StartBatchUsersExport>`_

        """
        return self.client.post("""/api/v4/reports/users/export""")
