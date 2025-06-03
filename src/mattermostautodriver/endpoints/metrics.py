from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Metrics"]


class Metrics(Base):

    def submit_performance_report(
        self,
        version: str,
        start: int,
        end: int,
        client_id: str | None = None,
        labels: list[str] | None = None,
        counters: list[dict[str, Any]] | None = None,
        histograms: list[dict[str, Any]] | None = None,
    ):
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
        __options = {
            "version": version,
            "client_id": client_id,
            "labels": labels,
            "start": start,
            "end": end,
            "counters": counters,
            "histograms": histograms,
        }
        return self.client.post("""/api/v4/client_perf""", options=__options)
