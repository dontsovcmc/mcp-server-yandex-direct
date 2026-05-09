"""Pydantic models for Changes service."""

from pydantic import Field

from .common import YDBase


class ChangesCheckParams(YDBase):
    CampaignIds: list[int] | None = Field(default=None, description="Campaign IDs to check for changes")
    AdGroupIds: list[int] | None = Field(default=None, description="Ad group IDs to check for changes")
    AdIds: list[int] | None = Field(default=None, description="Ad IDs to check for changes")
    FieldNames: list[str] = Field(description="Names of object types to check for changes")
    Timestamp: str | None = Field(default=None, description="Timestamp from a previous check to detect changes since")


class ChangesCheckResult(YDBase):
    Timestamp: str | None = Field(default=None, description="Timestamp to use in subsequent change checks")
    CampaignIds: list[int] | None = Field(default=None, description="IDs of campaigns that changed")
    AdGroupIds: list[int] | None = Field(default=None, description="IDs of ad groups that changed")
    AdIds: list[int] | None = Field(default=None, description="IDs of ads that changed")


class ChangesCheckDictionariesResult(YDBase):
    Timestamp: str | None = Field(default=None, description="Timestamp to use in subsequent dictionary change checks")


class ChangesCheckCampaignsParams(YDBase):
    Timestamp: str | None = Field(default=None, description="Timestamp from a previous check to detect changes since")


class ChangesCheckCampaignsResultItem(YDBase):
    CampaignId: int | None = Field(default=None, description="Campaign ID that has changes")
    ChecksResults: list[dict] | None = Field(default=None, description="Details of what changed in the campaign")


class ChangesCheckCampaignsResult(YDBase):
    Timestamp: str | None = Field(default=None, description="Timestamp to use in subsequent change checks")
    Campaigns: list[ChangesCheckCampaignsResultItem] | None = Field(default=None, description="List of campaigns with changes")
