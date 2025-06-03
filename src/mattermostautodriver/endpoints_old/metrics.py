from ._base import Base

__all__ = ["Metrics"]


class Metrics(Base):

    def submit_performance_report(self, options=None):
        """Report client performance metrics

        version: An identifier for the schema of the data being submitted which currently must be "0.1.0"
        client_id: Not currently used
        labels: Labels to be applied to all metrics when recorded by the metrics backend
        start: The time in milliseconds of the first metric in this report
        end: The time in milliseconds of the last metric in this report
        counters: An array of counter metrics to be reported
        histograms: An array of histogram measurements to be reported

        `Read in Mattermost API docs (metrics - SubmitPerformanceReport) <https://developers.mattermost.com/api-documentation/#/operations/SubmitPerformanceReport>`_

        """
        return self.client.post("""/api/v4/client_perf""", options=options)
