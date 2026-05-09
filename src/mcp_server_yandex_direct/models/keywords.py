"""Pydantic models for Keywords service."""

from enum import Enum

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class KeywordStateEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
    SUSPENDED = "SUSPENDED"


class KeywordStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    DRAFT = "DRAFT"


class KeywordsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by keyword IDs")
    AdGroupIds: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    States: list[str] | None = Field(default=None, description="Filter by keyword states")
    Statuses: list[str] | None = Field(default=None, description="Filter by moderation statuses")
    ModifiedSince: str | None = Field(default=None, description="Return keywords modified after this timestamp")
    ServingStatuses: list[str] | None = Field(default=None, description="Filter by serving statuses")


class KeywordsGetParams(YDBase):
    SelectionCriteria: KeywordsSelectionCriteria = Field(description="Criteria for selecting keywords")
    FieldNames: list[str] = Field(description="Keyword field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class KeywordGetItem(YDBase):
    Id: int | None = Field(default=None, description="Keyword ID")
    Keyword: str | None = Field(default=None, description="Keyword text with operators")
    AdGroupId: int | None = Field(default=None, description="ID of the parent ad group")
    CampaignId: int | None = Field(default=None, description="ID of the parent campaign")
    Bid: int | None = Field(default=None, description="Search bid in currency units (micros)")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")
    State: str | None = Field(default=None, description="Keyword state")
    Status: str | None = Field(default=None, description="Moderation status")
    ServingStatus: str | None = Field(default=None, description="Serving status of the keyword")
    UserParam1: str | None = Field(default=None, description="Custom user parameter 1 for URL substitution")
    UserParam2: str | None = Field(default=None, description="Custom user parameter 2 for URL substitution")
    ProductivityL: float | None = Field(default=None, description="Lower bound of keyword productivity")
    Productivity: float | None = Field(default=None, description="Keyword productivity score")
    StatisticsSearch: dict | None = Field(default=None, description="Search impression statistics")
    StatisticsNetwork: dict | None = Field(default=None, description="Network impression statistics")


class KeywordsGetResult(YDBase):
    Keywords: list[KeywordGetItem] | None = Field(default=None, description="List of keywords matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class KeywordAddItem(YDBase):
    Keyword: str = Field(description="Keyword text with operators")
    AdGroupId: int = Field(description="ID of the ad group to add the keyword to")
    Bid: int | None = Field(default=None, description="Search bid in currency units (micros)")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")
    UserParam1: str | None = Field(default=None, description="Custom user parameter 1 for URL substitution")
    UserParam2: str | None = Field(default=None, description="Custom user parameter 2 for URL substitution")


class KeywordsAddParams(YDBase):
    Keywords: list[KeywordAddItem] = Field(description="List of keywords to add")


class KeywordsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class KeywordUpdateItem(YDBase):
    Id: int = Field(description="ID of the keyword to update")
    Keyword: str | None = Field(default=None, description="Keyword text with operators")
    Bid: int | None = Field(default=None, description="Search bid in currency units (micros)")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")
    UserParam1: str | None = Field(default=None, description="Custom user parameter 1 for URL substitution")
    UserParam2: str | None = Field(default=None, description="Custom user parameter 2 for URL substitution")


class KeywordsUpdateParams(YDBase):
    Keywords: list[KeywordUpdateItem] = Field(description="List of keywords to update")


class KeywordsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of update operations")


class KeywordsActionParams(YDBase):
    """Used by delete, suspend, resume."""
    SelectionCriteria: IdsCriteria = Field(description="IDs of keywords to act on")


class KeywordsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = Field(default=None, description="Results of delete operations")
    SuspendResults: list[ActionResult] | None = Field(default=None, description="Results of suspend operations")
    ResumeResults: list[ActionResult] | None = Field(default=None, description="Results of resume operations")
