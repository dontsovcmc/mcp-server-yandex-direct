"""Pydantic models for AudienceTargets service."""

from enum import Enum

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AudienceTargetStateEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
    SUSPENDED = "SUSPENDED"
    DELETED = "DELETED"


class AudienceTargetsSelectionCriteria(YDBase):
    Ids: list[int] | None = None
    AdGroupIds: list[int] | None = None
    CampaignIds: list[int] | None = None
    RetargetingListIds: list[int] | None = None
    InterestIds: list[int] | None = None
    States: list[str] | None = None


class AudienceTargetsGetParams(YDBase):
    SelectionCriteria: AudienceTargetsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class AudienceTargetGetItem(YDBase):
    Id: int | None = None
    AdGroupId: int | None = None
    CampaignId: int | None = None
    RetargetingListId: int | None = None
    InterestId: int | None = None
    ContextBid: int | None = None
    StrategyPriority: str | None = None
    State: str | None = None


class AudienceTargetsGetResult(YDBase):
    AudienceTargets: list[AudienceTargetGetItem] | None = None
    LimitedBy: int | None = None


class AudienceTargetAddItem(YDBase):
    AdGroupId: int
    RetargetingListId: int | None = None
    InterestId: int | None = None
    ContextBid: int | None = None
    StrategyPriority: str | None = None


class AudienceTargetsAddParams(YDBase):
    AudienceTargets: list[AudienceTargetAddItem]


class AudienceTargetsAddResult(YDBase):
    AddResults: list[ActionResult]


class AudienceTargetsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class AudienceTargetsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]


class AudienceTargetsActionParams(YDBase):
    """Used by suspend, resume."""
    SelectionCriteria: IdsCriteria


class AudienceTargetsActionResult(YDBase):
    SuspendResults: list[ActionResult] | None = None
    ResumeResults: list[ActionResult] | None = None


class AudienceTargetBidSetItem(YDBase):
    Id: int
    ContextBid: int | None = None
    StrategyPriority: str | None = None


class AudienceTargetsSetBidsParams(YDBase):
    Bids: list[AudienceTargetBidSetItem]


class AudienceTargetsSetBidsResult(YDBase):
    SetBidsResults: list[ActionResult]
