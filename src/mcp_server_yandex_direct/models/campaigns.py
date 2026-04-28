"""Pydantic models for Campaigns service."""

from enum import Enum

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class CampaignStateEnum(str, Enum):
    CONVERTED = "CONVERTED"
    ARCHIVED = "ARCHIVED"
    SUSPENDED = "SUSPENDED"
    ON = "ON"
    OFF = "OFF"
    ENDED = "ENDED"


class CampaignStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    DRAFT = "DRAFT"
    MODERATION = "MODERATION"
    REJECTED = "REJECTED"


class CampaignTypeEnum(str, Enum):
    TEXT_CAMPAIGN = "TEXT_CAMPAIGN"
    DYNAMIC_TEXT_CAMPAIGN = "DYNAMIC_TEXT_CAMPAIGN"
    MOBILE_APP_CAMPAIGN = "MOBILE_APP_CAMPAIGN"
    CPM_BANNER_CAMPAIGN = "CPM_BANNER_CAMPAIGN"
    SMART_CAMPAIGN = "SMART_CAMPAIGN"
    UNIFIED_CAMPAIGN = "UNIFIED_CAMPAIGN"


class CampaignsSelectionCriteria(YDBase):
    Ids: list[int] | None = None
    Types: list[str] | None = None
    States: list[str] | None = None
    Statuses: list[str] | None = None
    StatusesPayment: list[str] | None = None


class CampaignsGetParams(YDBase):
    SelectionCriteria: CampaignsSelectionCriteria
    FieldNames: list[str]
    TextCampaignFieldNames: list[str] | None = None
    DynamicTextCampaignFieldNames: list[str] | None = None
    MobileAppCampaignFieldNames: list[str] | None = None
    CpmBannerCampaignFieldNames: list[str] | None = None
    SmartCampaignFieldNames: list[str] | None = None
    UnifiedCampaignFieldNames: list[str] | None = None
    Page: LimitOffset | None = None


class CampaignGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    Type: str | None = None
    Status: str | None = None
    State: str | None = None
    StatusPayment: str | None = None
    StatusClarification: str | None = None
    StartDate: str | None = None
    EndDate: str | None = None
    DailyBudget: dict | None = None
    NegativeKeywords: dict | None = None
    BlockedIps: list[str] | None = None
    ExcludedSites: list[str] | None = None
    Currency: str | None = None
    Funds: dict | None = None
    RepresentedBy: dict | None = None
    Statistics: dict | None = None
    TextCampaign: dict | None = None
    DynamicTextCampaign: dict | None = None
    MobileAppCampaign: dict | None = None
    CpmBannerCampaign: dict | None = None
    SmartCampaign: dict | None = None
    UnifiedCampaign: dict | None = None
    TimeTargeting: dict | None = None
    Notification: dict | None = None
    TimeZone: str | None = None
    ClientInfo: str | None = None
    SourceId: int | None = None


class CampaignsGetResult(YDBase):
    Campaigns: list[CampaignGetItem] | None = None
    LimitedBy: int | None = None


class CampaignAddItem(YDBase):
    Name: str
    StartDate: str
    ClientInfo: str | None = None
    EndDate: str | None = None
    TimeZone: str | None = None
    DailyBudget: dict | None = None
    NegativeKeywords: dict | None = None
    BlockedIps: list[str] | None = None
    ExcludedSites: list[str] | None = None
    TextCampaign: dict | None = None
    DynamicTextCampaign: dict | None = None
    MobileAppCampaign: dict | None = None
    CpmBannerCampaign: dict | None = None
    SmartCampaign: dict | None = None
    UnifiedCampaign: dict | None = None
    TimeTargeting: dict | None = None
    Notification: dict | None = None


class CampaignsAddParams(YDBase):
    Campaigns: list[CampaignAddItem]


class CampaignsAddResult(YDBase):
    AddResults: list[ActionResult]


class CampaignUpdateItem(YDBase):
    Id: int
    Name: str | None = None
    StartDate: str | None = None
    EndDate: str | None = None
    DailyBudget: dict | None = None
    NegativeKeywords: dict | None = None
    BlockedIps: list[str] | None = None
    ExcludedSites: list[str] | None = None
    TextCampaign: dict | None = None
    DynamicTextCampaign: dict | None = None
    MobileAppCampaign: dict | None = None
    CpmBannerCampaign: dict | None = None
    SmartCampaign: dict | None = None
    UnifiedCampaign: dict | None = None
    TimeTargeting: dict | None = None
    Notification: dict | None = None
    TimeZone: str | None = None
    ClientInfo: str | None = None


class CampaignsUpdateParams(YDBase):
    Campaigns: list[CampaignUpdateItem]


class CampaignsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class CampaignsActionParams(YDBase):
    """Used by delete, suspend, resume, archive, unarchive."""
    SelectionCriteria: IdsCriteria


class CampaignsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = None
    SuspendResults: list[ActionResult] | None = None
    ResumeResults: list[ActionResult] | None = None
    ArchiveResults: list[ActionResult] | None = None
    UnarchiveResults: list[ActionResult] | None = None
