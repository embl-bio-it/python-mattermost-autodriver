from .base import Base


class Jobs(Base):
    def get_jobs(self, params=None):
        """Get the jobs.

        page: The page to select.
        per_page: The number of jobs per page.

        `Read in Mattermost API docs (jobs - GetJobs) <https://api.mattermost.com/#tag/jobs/operation/GetJobs>`_
        """
        return self.client.get("""/api/v4/jobs""", params=params)

    def create_job(self, options):
        """Create a new job.

        type: The type of job to create
        data: An object containing any additional data required for this job type

        `Read in Mattermost API docs (jobs - CreateJob) <https://api.mattermost.com/#tag/jobs/operation/CreateJob>`_
        """
        return self.client.post("""/api/v4/jobs""", options=options)

    def get_job(self, job_id):
        """Get a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - GetJob) <https://api.mattermost.com/#tag/jobs/operation/GetJob>`_
        """
        return self.client.get(f"/api/v4/jobs/{job_id}")

    def download_job(self, job_id):
        """Download the results of a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - DownloadJob) <https://api.mattermost.com/#tag/jobs/operation/DownloadJob>`_
        """
        return self.client.get(f"/api/v4/jobs/{job_id}/download")

    def cancel_job(self, job_id):
        """Cancel a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - CancelJob) <https://api.mattermost.com/#tag/jobs/operation/CancelJob>`_
        """
        return self.client.post(f"/api/v4/jobs/{job_id}/cancel")

    def get_jobs_by_type(self, type, params=None):
        """Get the jobs of the given type.

        type: Job type
        page: The page to select.
        per_page: The number of jobs per page.

        `Read in Mattermost API docs (jobs - GetJobsByType) <https://api.mattermost.com/#tag/jobs/operation/GetJobsByType>`_
        """
        return self.client.get(f"/api/v4/jobs/type/{type}", params=params)
