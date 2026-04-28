"""Pydantic models for Changes service."""

from .common import YDBase


class ChangesCheckParams(YDBase):
    CampaignIds: list[int] | None = None
    AdGroupIds: list[int] | None = None
    AdIds: list[int] | None = None
    FieldNames: list[str]
    Timestamp: str | None = None


class ChangesCheckResult(YDBase):
    Timestamp: str | None = None
    CampaignIds: list[int] | None = None
    AdGroupIds: list[int] | None = None
    AdIds: list[int] | None = None


class ChangesCheckDictionariesResult(YDBase):
    Timestamp: str | None = None


class ChangesCheckCampaignsParams(YDBase):
    Timestamp: str | None = None


class ChangesCheckCampaignsResultItem(YDBase):
    CampaignId: int | None = None
    ChecksResults: list[dict] | None = None


class ChangesCheckCampaignsResult(YDBase):
    Timestamp: str | None = None
    Campaigns: list[ChangesCheckCampaignsResultItem] | None = None
