from ._base import Base

__all__ = ["Jobs"]


class Jobs(Base):

    def get_jobs(self, params=None):
        """Get the jobs.

        page: The page to select.
        per_page: The number of jobs per page.
        job_type: The type of jobs to fetch.
        status: The status of jobs to fetch.

        `Read in Mattermost API docs (jobs - GetJobs) <https://developers.mattermost.com/api-documentation/#/operations/GetJobs>`_

        """
        return self.client.get("""/api/v4/jobs""", params=params)

    def create_job(self, options):
        """Create a new job.

        type: The type of job to create
        data: An object containing any additional data required for this job type

        `Read in Mattermost API docs (jobs - CreateJob) <https://developers.mattermost.com/api-documentation/#/operations/CreateJob>`_

        """
        return self.client.post("""/api/v4/jobs""", options=options)

    def get_job(self, job_id):
        """Get a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - GetJob) <https://developers.mattermost.com/api-documentation/#/operations/GetJob>`_

        """
        return self.client.get(f"/api/v4/jobs/{job_id}")

    def download_job(self, job_id):
        """Download the results of a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - DownloadJob) <https://developers.mattermost.com/api-documentation/#/operations/DownloadJob>`_

        """
        return self.client.get(f"/api/v4/jobs/{job_id}/download")

    def cancel_job(self, job_id):
        """Cancel a job.

        job_id: Job GUID

        `Read in Mattermost API docs (jobs - CancelJob) <https://developers.mattermost.com/api-documentation/#/operations/CancelJob>`_

        """
        return self.client.post(f"/api/v4/jobs/{job_id}/cancel")

    def get_jobs_by_type(self, type, params=None):
        """Get the jobs of the given type.

        type: Job type
        page: The page to select.
        per_page: The number of jobs per page.

        `Read in Mattermost API docs (jobs - GetJobsByType) <https://developers.mattermost.com/api-documentation/#/operations/GetJobsByType>`_

        """
        return self.client.get(f"/api/v4/jobs/type/{type}", params=params)

    def update_job_status(self, job_id, options):
        """Update the status of a job

        job_id: Job GUID
        status: The status you want to set
        force: Set this to true to bypass status restrictions

        `Read in Mattermost API docs (jobs - UpdateJobStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateJobStatus>`_

        """
        return self.client.patch(f"/api/v4/jobs/{job_id}/status", options=options)
