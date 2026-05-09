"""Pydantic models for AdGroups service."""

from enum import Enum

from pydantic import Field

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
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    Ids: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    Types: list[str] | None = Field(default=None, description="Filter by ad group types")
    Statuses: list[str] | None = Field(default=None, description="Filter by moderation statuses")
    AppIconStatuses: list[str] | None = Field(default=None, description="Filter by app icon moderation statuses")


class AdGroupsGetParams(YDBase):
    SelectionCriteria: AdGroupsSelectionCriteria = Field(description="Criteria for selecting ad groups")
    FieldNames: list[str] = Field(description="Ad group field names to return")
    DynamicTextAdGroupFieldNames: list[str] | None = Field(default=None, description="Fields to return for dynamic text ad groups")
    DynamicTextFeedAdGroupFieldNames: list[str] | None = Field(default=None, description="Fields to return for dynamic text feed ad groups")
    MobileAppAdGroupFieldNames: list[str] | None = Field(default=None, description="Fields to return for mobile app ad groups")
    SmartAdGroupFieldNames: list[str] | None = Field(default=None, description="Fields to return for smart ad groups")
    UnifiedAdGroupFieldNames: list[str] | None = Field(default=None, description="Fields to return for unified ad groups")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AdGroupGetItem(YDBase):
    Id: int | None = Field(default=None, description="Ad group ID")
    Name: str | None = Field(default=None, description="Ad group name")
    CampaignId: int | None = Field(default=None, description="ID of the parent campaign")
    RegionIds: list[int] | None = Field(default=None, description="Geo-targeting region IDs")
    NegativeKeywords: dict | None = Field(default=None, description="Ad group negative keywords")
    NegativeKeywordSharedSetIds: list[int] | None = Field(default=None, description="IDs of shared negative keyword sets")
    TrackingParams: str | None = Field(default=None, description="Tracking parameters for URLs")
    Status: str | None = Field(default=None, description="Moderation status")
    ServingStatus: str | None = Field(default=None, description="Serving status of the ad group")
    Type: str | None = Field(default=None, description="Ad group type")
    Subtype: str | None = Field(default=None, description="Ad group subtype")


class AdGroupsGetResult(YDBase):
    AdGroups: list[AdGroupGetItem] | None = Field(default=None, description="List of ad groups matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AdGroupAddItem(YDBase):
    Name: str = Field(description="Ad group name")
    CampaignId: int = Field(description="ID of the parent campaign")
    RegionIds: list[int] = Field(description="Geo-targeting region IDs")
    NegativeKeywords: dict | None = Field(default=None, description="Ad group negative keywords")
    NegativeKeywordSharedSetIds: list[int] | None = Field(default=None, description="IDs of shared negative keyword sets")
    TrackingParams: str | None = Field(default=None, description="Tracking parameters for URLs")


class AdGroupsAddParams(YDBase):
    AdGroups: list[AdGroupAddItem] = Field(description="List of ad groups to add")


class AdGroupsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class AdGroupUpdateItem(YDBase):
    Id: int = Field(description="ID of the ad group to update")
    Name: str | None = Field(default=None, description="Ad group name")
    RegionIds: list[int] | None = Field(default=None, description="Geo-targeting region IDs")
    NegativeKeywords: dict | None = Field(default=None, description="Ad group negative keywords")
    NegativeKeywordSharedSetIds: list[int] | None = Field(default=None, description="IDs of shared negative keyword sets")
    TrackingParams: str | None = Field(default=None, description="Tracking parameters for URLs")


class AdGroupsUpdateParams(YDBase):
    AdGroups: list[AdGroupUpdateItem] = Field(description="List of ad groups to update")


class AdGroupsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of update operations")


class AdGroupsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of ad groups to delete")


class AdGroupsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")
