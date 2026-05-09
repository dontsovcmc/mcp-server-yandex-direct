"""Pydantic models for Leads service."""

from pydantic import Field

from .common import YDBase, LimitOffset


class LeadsSelectionCriteria(YDBase):
    CampaignIds: list[int] | None = Field(default=None, description="Campaign IDs to filter leads by")
    TurboPageIds: list[int] | None = Field(default=None, description="Turbo page IDs to filter leads by")
    DateTimeFrom: str | None = Field(default=None, description="Start of the date range for lead submission")
    DateTimeTo: str | None = Field(default=None, description="End of the date range for lead submission")


class LeadsGetParams(YDBase):
    SelectionCriteria: LeadsSelectionCriteria = Field(description="Criteria for selecting leads")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class LeadGetItem(YDBase):
    Id: int | None = Field(default=None, description="Lead ID")
    TurboPageId: int | None = Field(default=None, description="ID of the turbo page where the lead was submitted")
    TurboPageName: str | None = Field(default=None, description="Name of the turbo page")
    CampaignId: int | None = Field(default=None, description="Campaign ID associated with the lead")
    SubmitDateTime: str | None = Field(default=None, description="Date and time of lead submission")
    FormData: list[dict] | None = Field(default=None, description="Form data submitted by the user")


class LeadsGetResult(YDBase):
    Leads: list[LeadGetItem] | None = Field(default=None, description="List of leads")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")
