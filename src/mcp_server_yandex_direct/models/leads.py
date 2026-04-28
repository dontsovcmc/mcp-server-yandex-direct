"""Pydantic models for Leads service."""

from .common import YDBase, LimitOffset


class LeadsSelectionCriteria(YDBase):
    CampaignIds: list[int] | None = None
    TurboPageIds: list[int] | None = None
    DateTimeFrom: str | None = None
    DateTimeTo: str | None = None


class LeadsGetParams(YDBase):
    SelectionCriteria: LeadsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class LeadGetItem(YDBase):
    Id: int | None = None
    TurboPageId: int | None = None
    TurboPageName: str | None = None
    CampaignId: int | None = None
    SubmitDateTime: str | None = None
    FormData: list[dict] | None = None


class LeadsGetResult(YDBase):
    Leads: list[LeadGetItem] | None = None
    LimitedBy: int | None = None
