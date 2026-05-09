"""Pydantic models for Ads service."""

from enum import Enum

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class AdTypeEnum(str, Enum):
    TEXT_AD = "TEXT_AD"
    DYNAMIC_TEXT_AD = "DYNAMIC_TEXT_AD"
    MOBILE_APP_AD = "MOBILE_APP_AD"
    IMAGE_AD = "IMAGE_AD"
    TEXT_IMAGE_AD = "TEXT_IMAGE_AD"
    CPC_VIDEO_AD = "CPC_VIDEO_AD"
    CPM_BANNER_AD = "CPM_BANNER_AD"
    CPM_VIDEO_AD = "CPM_VIDEO_AD"
    SMART_AD = "SMART_AD"


class AdStateEnum(str, Enum):
    ON = "ON"
    OFF = "OFF"
    OFF_BY_MONITORING = "OFF_BY_MONITORING"
    SUSPENDED = "SUSPENDED"
    ARCHIVED = "ARCHIVED"


class AdStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    DRAFT = "DRAFT"
    MODERATION = "MODERATION"
    PREACCEPTED = "PREACCEPTED"
    REJECTED = "REJECTED"


class AdsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by ad IDs")
    AdGroupIds: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    States: list[str] | None = Field(default=None, description="Filter by ad states")
    Statuses: list[str] | None = Field(default=None, description="Filter by moderation statuses")
    Types: list[str] | None = Field(default=None, description="Filter by ad types")


class AdsGetParams(YDBase):
    SelectionCriteria: AdsSelectionCriteria = Field(description="Criteria for selecting ads")
    FieldNames: list[str] = Field(description="Ad-level field names to return")
    TextAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for text ads")
    DynamicTextAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for dynamic text ads")
    MobileAppAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for mobile app ads")
    TextImageAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for text image ads")
    CpcVideoAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for CPC video ads")
    CpmBannerAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for CPM banner ads")
    CpmVideoAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for CPM video ads")
    SmartAdFieldNames: list[str] | None = Field(default=None, description="Fields to return for smart ads")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AdGetItem(YDBase):
    Id: int | None = Field(default=None, description="Ad ID")
    CampaignId: int | None = Field(default=None, description="ID of the parent campaign")
    AdGroupId: int | None = Field(default=None, description="ID of the parent ad group")
    Status: str | None = Field(default=None, description="Moderation status")
    State: str | None = Field(default=None, description="Ad state")
    StatusClarification: str | None = Field(default=None, description="Reason for rejection or other status clarification")
    Type: str | None = Field(default=None, description="Ad type")
    Subtype: str | None = Field(default=None, description="Ad subtype")
    TextAd: dict | None = Field(default=None, description="Text ad parameters")
    DynamicTextAd: dict | None = Field(default=None, description="Dynamic text ad parameters")
    MobileAppAd: dict | None = Field(default=None, description="Mobile app ad parameters")
    TextImageAd: dict | None = Field(default=None, description="Text image ad parameters")
    CpcVideoAd: dict | None = Field(default=None, description="CPC video ad parameters")
    CpmBannerAd: dict | None = Field(default=None, description="CPM banner ad parameters")
    CpmVideoAd: dict | None = Field(default=None, description="CPM video ad parameters")
    SmartAd: dict | None = Field(default=None, description="Smart ad parameters")


class AdsGetResult(YDBase):
    Ads: list[AdGetItem] | None = Field(default=None, description="List of ads matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AdAddItem(YDBase):
    AdGroupId: int = Field(description="ID of the ad group to add the ad to")
    TextAd: dict | None = Field(default=None, description="Text ad parameters")
    DynamicTextAd: dict | None = Field(default=None, description="Dynamic text ad parameters")
    MobileAppAd: dict | None = Field(default=None, description="Mobile app ad parameters")
    TextImageAd: dict | None = Field(default=None, description="Text image ad parameters")
    CpcVideoAd: dict | None = Field(default=None, description="CPC video ad parameters")
    CpmBannerAd: dict | None = Field(default=None, description="CPM banner ad parameters")
    CpmVideoAd: dict | None = Field(default=None, description="CPM video ad parameters")
    SmartAd: dict | None = Field(default=None, description="Smart ad parameters")


class AdsAddParams(YDBase):
    Ads: list[AdAddItem] = Field(description="List of ads to add")


class AdsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class AdUpdateItem(YDBase):
    Id: int = Field(description="ID of the ad to update")
    TextAd: dict | None = Field(default=None, description="Text ad parameters")
    DynamicTextAd: dict | None = Field(default=None, description="Dynamic text ad parameters")
    MobileAppAd: dict | None = Field(default=None, description="Mobile app ad parameters")
    TextImageAd: dict | None = Field(default=None, description="Text image ad parameters")
    CpcVideoAd: dict | None = Field(default=None, description="CPC video ad parameters")
    CpmBannerAd: dict | None = Field(default=None, description="CPM banner ad parameters")
    CpmVideoAd: dict | None = Field(default=None, description="CPM video ad parameters")
    SmartAd: dict | None = Field(default=None, description="Smart ad parameters")


class AdsUpdateParams(YDBase):
    Ads: list[AdUpdateItem] = Field(description="List of ads to update")


class AdsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of update operations")


class AdsActionParams(YDBase):
    """Used by delete, suspend, resume, archive, unarchive, moderate."""
    SelectionCriteria: IdsCriteria = Field(description="IDs of ads to act on")


class AdsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = Field(default=None, description="Results of delete operations")
    SuspendResults: list[ActionResult] | None = Field(default=None, description="Results of suspend operations")
    ResumeResults: list[ActionResult] | None = Field(default=None, description="Results of resume operations")
    ArchiveResults: list[ActionResult] | None = Field(default=None, description="Results of archive operations")
    UnarchiveResults: list[ActionResult] | None = Field(default=None, description="Results of unarchive operations")
    ModerateResults: list[ActionResult] | None = Field(default=None, description="Results of moderate operations")
