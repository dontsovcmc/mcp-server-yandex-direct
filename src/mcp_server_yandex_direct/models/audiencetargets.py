"""Pydantic models for AudienceTargets service."""

from enum import Enum

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AudienceTargetStateEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
    SUSPENDED = "SUSPENDED"
    DELETED = "DELETED"


class AudienceTargetsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by audience target IDs")
    AdGroupIds: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    RetargetingListIds: list[int] | None = Field(default=None, description="Filter by retargeting list IDs")
    InterestIds: list[int] | None = Field(default=None, description="Filter by interest IDs")
    States: list[str] | None = Field(default=None, description="Filter by audience target states")


class AudienceTargetsGetParams(YDBase):
    SelectionCriteria: AudienceTargetsSelectionCriteria = Field(description="Criteria for selecting audience targets")
    FieldNames: list[str] = Field(description="Audience target field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AudienceTargetGetItem(YDBase):
    Id: int | None = Field(default=None, description="Audience target ID")
    AdGroupId: int | None = Field(default=None, description="ID of the parent ad group")
    CampaignId: int | None = Field(default=None, description="ID of the parent campaign")
    RetargetingListId: int | None = Field(default=None, description="Associated retargeting list ID")
    InterestId: int | None = Field(default=None, description="Associated interest ID")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")
    State: str | None = Field(default=None, description="Audience target state")


class AudienceTargetsGetResult(YDBase):
    AudienceTargets: list[AudienceTargetGetItem] | None = Field(default=None, description="List of audience targets matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AudienceTargetAddItem(YDBase):
    AdGroupId: int = Field(description="ID of the ad group to add the audience target to")
    RetargetingListId: int | None = Field(default=None, description="Retargeting list ID to target")
    InterestId: int | None = Field(default=None, description="Interest ID to target")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")


class AudienceTargetsAddParams(YDBase):
    AudienceTargets: list[AudienceTargetAddItem] = Field(description="List of audience targets to add")


class AudienceTargetsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class AudienceTargetsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of audience targets to delete")


class AudienceTargetsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")


class AudienceTargetsActionParams(YDBase):
    """Used by suspend, resume."""
    SelectionCriteria: IdsCriteria = Field(description="IDs of audience targets to act on")


class AudienceTargetsActionResult(YDBase):
    SuspendResults: list[ActionResult] | None = Field(default=None, description="Results of suspend operations")
    ResumeResults: list[ActionResult] | None = Field(default=None, description="Results of resume operations")


class AudienceTargetBidSetItem(YDBase):
    Id: int = Field(description="Audience target ID to set the bid for")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    StrategyPriority: str | None = Field(default=None, description="Priority for automatic bidding (LOW, NORMAL, HIGH)")


class AudienceTargetsSetBidsParams(YDBase):
    Bids: list[AudienceTargetBidSetItem] = Field(description="List of audience target bids to set")


class AudienceTargetsSetBidsResult(YDBase):
    SetBidsResults: list[ActionResult] = Field(description="Results of set bids operations")
