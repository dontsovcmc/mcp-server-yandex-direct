"""Pydantic models for Ads service."""

from enum import Enum

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
    Ids: list[int] | None = None
    AdGroupIds: list[int] | None = None
    CampaignIds: list[int] | None = None
    States: list[str] | None = None
    Statuses: list[str] | None = None
    Types: list[str] | None = None


class AdsGetParams(YDBase):
    SelectionCriteria: AdsSelectionCriteria
    FieldNames: list[str]
    TextAdFieldNames: list[str] | None = None
    DynamicTextAdFieldNames: list[str] | None = None
    MobileAppAdFieldNames: list[str] | None = None
    TextImageAdFieldNames: list[str] | None = None
    CpcVideoAdFieldNames: list[str] | None = None
    CpmBannerAdFieldNames: list[str] | None = None
    CpmVideoAdFieldNames: list[str] | None = None
    SmartAdFieldNames: list[str] | None = None
    Page: LimitOffset | None = None


class AdGetItem(YDBase):
    Id: int | None = None
    CampaignId: int | None = None
    AdGroupId: int | None = None
    Status: str | None = None
    State: str | None = None
    StatusClarification: str | None = None
    Type: str | None = None
    Subtype: str | None = None
    TextAd: dict | None = None
    DynamicTextAd: dict | None = None
    MobileAppAd: dict | None = None
    TextImageAd: dict | None = None
    CpcVideoAd: dict | None = None
    CpmBannerAd: dict | None = None
    CpmVideoAd: dict | None = None
    SmartAd: dict | None = None


class AdsGetResult(YDBase):
    Ads: list[AdGetItem] | None = None
    LimitedBy: int | None = None


class AdAddItem(YDBase):
    AdGroupId: int
    TextAd: dict | None = None
    DynamicTextAd: dict | None = None
    MobileAppAd: dict | None = None
    TextImageAd: dict | None = None
    CpcVideoAd: dict | None = None
    CpmBannerAd: dict | None = None
    CpmVideoAd: dict | None = None
    SmartAd: dict | None = None


class AdsAddParams(YDBase):
    Ads: list[AdAddItem]


class AdsAddResult(YDBase):
    AddResults: list[ActionResult]


class AdUpdateItem(YDBase):
    Id: int
    TextAd: dict | None = None
    DynamicTextAd: dict | None = None
    MobileAppAd: dict | None = None
    TextImageAd: dict | None = None
    CpcVideoAd: dict | None = None
    CpmBannerAd: dict | None = None
    CpmVideoAd: dict | None = None
    SmartAd: dict | None = None


class AdsUpdateParams(YDBase):
    Ads: list[AdUpdateItem]


class AdsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class AdsActionParams(YDBase):
    """Used by delete, suspend, resume, archive, unarchive, moderate."""
    SelectionCriteria: IdsCriteria


class AdsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = None
    SuspendResults: list[ActionResult] | None = None
    ResumeResults: list[ActionResult] | None = None
    ArchiveResults: list[ActionResult] | None = None
    UnarchiveResults: list[ActionResult] | None = None
    ModerateResults: list[ActionResult] | None = None
