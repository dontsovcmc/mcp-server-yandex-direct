"""Pydantic models for Keywords service."""

from enum import Enum

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class KeywordStateEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
    SUSPENDED = "SUSPENDED"


class KeywordStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    DRAFT = "DRAFT"


class KeywordsSelectionCriteria(YDBase):
    Ids: list[int] | None = None
    AdGroupIds: list[int] | None = None
    CampaignIds: list[int] | None = None
    States: list[str] | None = None
    Statuses: list[str] | None = None
    ModifiedSince: str | None = None
    ServingStatuses: list[str] | None = None


class KeywordsGetParams(YDBase):
    SelectionCriteria: KeywordsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class KeywordGetItem(YDBase):
    Id: int | None = None
    Keyword: str | None = None
    AdGroupId: int | None = None
    CampaignId: int | None = None
    Bid: int | None = None
    ContextBid: int | None = None
    StrategyPriority: str | None = None
    State: str | None = None
    Status: str | None = None
    ServingStatus: str | None = None
    UserParam1: str | None = None
    UserParam2: str | None = None
    ProductivityL: float | None = None
    Productivity: float | None = None
    StatisticsSearch: dict | None = None
    StatisticsNetwork: dict | None = None


class KeywordsGetResult(YDBase):
    Keywords: list[KeywordGetItem] | None = None
    LimitedBy: int | None = None


class KeywordAddItem(YDBase):
    Keyword: str
    AdGroupId: int
    Bid: int | None = None
    ContextBid: int | None = None
    StrategyPriority: str | None = None
    UserParam1: str | None = None
    UserParam2: str | None = None


class KeywordsAddParams(YDBase):
    Keywords: list[KeywordAddItem]


class KeywordsAddResult(YDBase):
    AddResults: list[ActionResult]


class KeywordUpdateItem(YDBase):
    Id: int
    Keyword: str | None = None
    Bid: int | None = None
    ContextBid: int | None = None
    StrategyPriority: str | None = None
    UserParam1: str | None = None
    UserParam2: str | None = None


class KeywordsUpdateParams(YDBase):
    Keywords: list[KeywordUpdateItem]


class KeywordsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class KeywordsActionParams(YDBase):
    """Used by delete, suspend, resume."""
    SelectionCriteria: IdsCriteria


class KeywordsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = None
    SuspendResults: list[ActionResult] | None = None
    ResumeResults: list[ActionResult] | None = None
