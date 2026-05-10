"""Pydantic model for Reports API."""

from pydantic import Field

from .common import YDBase


class ReportsGetBody(YDBase):
    """Parameters for Reports API request."""

    body: dict = Field(
        description=(
            "Report definition: SelectionCriteria (DateFrom/DateTo), FieldNames, "
            "ReportName, ReportType, DateRangeType, Format (TSV/CSV), "
            "IncludeVAT, IncludeDiscount, Filters, Goals, OrderBy, Page"
        )
    )
    extra_headers: dict | None = Field(
        default=None,
        description="Optional extra HTTP headers (e.g. for asynchronous report retrieval)",
    )
