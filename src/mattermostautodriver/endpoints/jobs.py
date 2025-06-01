from .base import Base
from typing import Any, BinaryIO


class Jobs(Base):

    def get_jobs(
        self, page: int | None = 0, per_page: int | None = 5, job_type: str | None = None, status: str | None = None
    ):
        """Get the jobs.

        page: The page to select.
        per_page: The number of jobs per page.
        job_type: The type of jobs to fetch.
        status: The status of jobs to fetch.

        `Read in Mattermost API docs (jobs - GetJobs) <https://api.mattermost.com/#tag/jobs/operation/GetJobs>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "page": page,
            "per_page": per_page,
            "job_type": job_type,
            "status": status,
        }
        return self.client.get("""/api/v4/jobs""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def create_job(self, type: str, data: dict[str, Any] | None = None):
        """Create a new job.

        type: The type of job to create
        data: An object containing any additional data required for this job type

        `Read in Mattermost API docs (jobs - CreateJob) <https://api.mattermost.com/#tag/jobs/operation/CreateJob>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"type": type, "data": data}
        return self.client.post("""/api/v4/jobs""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_job(self, job_id: str):
        """Get a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - GetJob) <https://api.mattermost.com/#tag/jobs/operation/GetJob>`_

        """
        return self.client.get(f"/api/v4/jobs/{job_id}")

    def download_job(self, job_id: str):
        """Download the results of a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - DownloadJob) <https://api.mattermost.com/#tag/jobs/operation/DownloadJob>`_

        """
        return self.client.get(f"/api/v4/jobs/{job_id}/download")

    def cancel_job(self, job_id: str):
        """Cancel a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - CancelJob) <https://api.mattermost.com/#tag/jobs/operation/CancelJob>`_

        """
        return self.client.post(f"/api/v4/jobs/{job_id}/cancel")

    def get_jobs_by_type(self, type: str, page: int | None = 0, per_page: int | None = 60):
        """Get the jobs of the given type.

        type: Job type
        page: The page to select.
        per_page: The number of jobs per page.

        `Read in Mattermost API docs (jobs - GetJobsByType) <https://api.mattermost.com/#tag/jobs/operation/GetJobsByType>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/jobs/type/{type}", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def update_job_status(self, job_id: str, status: str, force: bool | None = None):
        """Update the status of a job

        job_id: Job GUID
        status: The status you want to set
        force: Set this to true to bypass status restrictions

        `Read in Mattermost API docs (jobs - UpdateJobStatus) <https://api.mattermost.com/#tag/jobs/operation/UpdateJobStatus>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"status": status, "force": force}
        return self.client.patch(f"/api/v4/jobs/{job_id}/status", options=options_71f8b7431cd64fcfa0dabd300d0636d2)
