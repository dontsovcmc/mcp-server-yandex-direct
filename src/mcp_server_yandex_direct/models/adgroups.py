"""Pydantic models for AdGroups service."""

from enum import Enum

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AdGroupTypeEnum(str, Enum):
    TEXT_AD_GROUP = "TEXT_AD_GROUP"
    DYNAMIC_TEXT_AD_GROUP = "DYNAMIC_TEXT_AD_GROUP"
    MOBILE_APP_AD_GROUP = "MOBILE_APP_AD_GROUP"
    CPM_BANNER_AD_GROUP = "CPM_BANNER_AD_GROUP"
    CPM_VIDEO_AD_GROUP = "CPM_VIDEO_AD_GROUP"
    SMART_AD_GROUP = "SMART_AD_GROUP"
    UNIFIED_AD_GROUP = "UNIFIED_AD_GROUP"


class AdGroupStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    DRAFT = "DRAFT"
    MODERATION = "MODERATION"
    PREACCEPTED = "PREACCEPTED"
    REJECTED = "REJECTED"


class AdGroupsSelectionCriteria(YDBase):
    CampaignIds: list[int] | None = None
    Ids: list[int] | None = None
    Types: list[str] | None = None
    Statuses: list[str] | None = None
    AppIconStatuses: list[str] | None = None


class AdGroupsGetParams(YDBase):
    SelectionCriteria: AdGroupsSelectionCriteria
    FieldNames: list[str]
    DynamicTextAdGroupFieldNames: list[str] | None = None
    DynamicTextFeedAdGroupFieldNames: list[str] | None = None
    MobileAppAdGroupFieldNames: list[str] | None = None
    SmartAdGroupFieldNames: list[str] | None = None
    UnifiedAdGroupFieldNames: list[str] | None = None
    Page: LimitOffset | None = None


class AdGroupGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    CampaignId: int | None = None
    RegionIds: list[int] | None = None
    NegativeKeywords: dict | None = None
    NegativeKeywordSharedSetIds: list[int] | None = None
    TrackingParams: str | None = None
    Status: str | None = None
    ServingStatus: str | None = None
    Type: str | None = None
    Subtype: str | None = None


class AdGroupsGetResult(YDBase):
    AdGroups: list[AdGroupGetItem] | None = None
    LimitedBy: int | None = None


class AdGroupAddItem(YDBase):
    Name: str
    CampaignId: int
    RegionIds: list[int]
    NegativeKeywords: dict | None = None
    NegativeKeywordSharedSetIds: list[int] | None = None
    TrackingParams: str | None = None


class AdGroupsAddParams(YDBase):
    AdGroups: list[AdGroupAddItem]


class AdGroupsAddResult(YDBase):
    AddResults: list[ActionResult]


class AdGroupUpdateItem(YDBase):
    Id: int
    Name: str | None = None
    RegionIds: list[int] | None = None
    NegativeKeywords: dict | None = None
    NegativeKeywordSharedSetIds: list[int] | None = None
    TrackingParams: str | None = None


class AdGroupsUpdateParams(YDBase):
    AdGroups: list[AdGroupUpdateItem]


class AdGroupsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class AdGroupsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class AdGroupsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
