"""Pydantic models for Campaigns service."""

from enum import Enum

from pydantic import Field

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
    Ids: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    Types: list[str] | None = Field(default=None, description="Filter by campaign types")
    States: list[str] | None = Field(default=None, description="Filter by campaign states")
    Statuses: list[str] | None = Field(default=None, description="Filter by campaign moderation statuses")
    StatusesPayment: list[str] | None = Field(default=None, description="Filter by payment statuses")


class CampaignsGetParams(YDBase):
    SelectionCriteria: CampaignsSelectionCriteria = Field(description="Criteria for selecting campaigns")
    FieldNames: list[str] = Field(description="Campaign-level field names to return")
    TextCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for text campaigns")
    DynamicTextCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for dynamic text campaigns")
    MobileAppCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for mobile app campaigns")
    CpmBannerCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for CPM banner campaigns")
    SmartCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for smart campaigns")
    UnifiedCampaignFieldNames: list[str] | None = Field(default=None, description="Fields to return for unified campaigns")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class CampaignGetItem(YDBase):
    Id: int | None = Field(default=None, description="Campaign ID")
    Name: str | None = Field(default=None, description="Campaign name")
    Type: str | None = Field(default=None, description="Campaign type")
    Status: str | None = Field(default=None, description="Campaign moderation status")
    State: str | None = Field(default=None, description="Campaign state")
    StatusPayment: str | None = Field(default=None, description="Payment status")
    StatusClarification: str | None = Field(default=None, description="Reason for rejection or other status clarification")
    StartDate: str | None = Field(default=None, description="Campaign start date (YYYY-MM-DD)")
    EndDate: str | None = Field(default=None, description="Campaign end date (YYYY-MM-DD)")
    DailyBudget: dict | None = Field(default=None, description="Daily budget settings")
    NegativeKeywords: dict | None = Field(default=None, description="Campaign-level negative keywords")
    BlockedIps: list[str] | None = Field(default=None, description="List of blocked IP addresses")
    ExcludedSites: list[str] | None = Field(default=None, description="List of excluded placements")
    Currency: str | None = Field(default=None, description="Campaign currency code")
    Funds: dict | None = Field(default=None, description="Campaign funding information")
    RepresentedBy: dict | None = Field(default=None, description="Agency representative information")
    Statistics: dict | None = Field(default=None, description="Campaign statistics summary")
    TextCampaign: dict | None = Field(default=None, description="Text campaign specific settings")
    DynamicTextCampaign: dict | None = Field(default=None, description="Dynamic text campaign specific settings")
    MobileAppCampaign: dict | None = Field(default=None, description="Mobile app campaign specific settings")
    CpmBannerCampaign: dict | None = Field(default=None, description="CPM banner campaign specific settings")
    SmartCampaign: dict | None = Field(default=None, description="Smart campaign specific settings")
    UnifiedCampaign: dict | None = Field(default=None, description="Unified campaign specific settings")
    TimeTargeting: dict | None = Field(default=None, description="Time targeting settings")
    Notification: dict | None = Field(default=None, description="Notification settings")
    TimeZone: str | None = Field(default=None, description="Campaign timezone")
    ClientInfo: str | None = Field(default=None, description="Client information text")
    SourceId: int | None = Field(default=None, description="ID of the source campaign (for copies)")


class CampaignsGetResult(YDBase):
    Campaigns: list[CampaignGetItem] | None = Field(default=None, description="List of campaigns matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class CampaignAddItem(YDBase):
    Name: str = Field(description="Campaign name")
    StartDate: str = Field(description="Campaign start date (YYYY-MM-DD)")
    ClientInfo: str | None = Field(default=None, description="Client information text")
    EndDate: str | None = Field(default=None, description="Campaign end date (YYYY-MM-DD)")
    TimeZone: str | None = Field(default=None, description="Campaign timezone")
    DailyBudget: dict | None = Field(default=None, description="Daily budget settings")
    NegativeKeywords: dict | None = Field(default=None, description="Campaign-level negative keywords")
    BlockedIps: list[str] | None = Field(default=None, description="List of blocked IP addresses")
    ExcludedSites: list[str] | None = Field(default=None, description="List of excluded placements")
    TextCampaign: dict | None = Field(default=None, description="Text campaign specific settings")
    DynamicTextCampaign: dict | None = Field(default=None, description="Dynamic text campaign specific settings")
    MobileAppCampaign: dict | None = Field(default=None, description="Mobile app campaign specific settings")
    CpmBannerCampaign: dict | None = Field(default=None, description="CPM banner campaign specific settings")
    SmartCampaign: dict | None = Field(default=None, description="Smart campaign specific settings")
    UnifiedCampaign: dict | None = Field(default=None, description="Unified campaign specific settings")
    TimeTargeting: dict | None = Field(default=None, description="Time targeting settings")
    Notification: dict | None = Field(default=None, description="Notification settings")


class CampaignsAddParams(YDBase):
    Campaigns: list[CampaignAddItem] = Field(description="List of campaigns to add")


class CampaignsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class CampaignUpdateItem(YDBase):
    Id: int = Field(description="ID of the campaign to update")
    Name: str | None = Field(default=None, description="Campaign name")
    StartDate: str | None = Field(default=None, description="Campaign start date (YYYY-MM-DD)")
    EndDate: str | None = Field(default=None, description="Campaign end date (YYYY-MM-DD)")
    DailyBudget: dict | None = Field(default=None, description="Daily budget settings")
    NegativeKeywords: dict | None = Field(default=None, description="Campaign-level negative keywords")
    BlockedIps: list[str] | None = Field(default=None, description="List of blocked IP addresses")
    ExcludedSites: list[str] | None = Field(default=None, description="List of excluded placements")
    TextCampaign: dict | None = Field(default=None, description="Text campaign specific settings")
    DynamicTextCampaign: dict | None = Field(default=None, description="Dynamic text campaign specific settings")
    MobileAppCampaign: dict | None = Field(default=None, description="Mobile app campaign specific settings")
    CpmBannerCampaign: dict | None = Field(default=None, description="CPM banner campaign specific settings")
    SmartCampaign: dict | None = Field(default=None, description="Smart campaign specific settings")
    UnifiedCampaign: dict | None = Field(default=None, description="Unified campaign specific settings")
    TimeTargeting: dict | None = Field(default=None, description="Time targeting settings")
    Notification: dict | None = Field(default=None, description="Notification settings")
    TimeZone: str | None = Field(default=None, description="Campaign timezone")
    ClientInfo: str | None = Field(default=None, description="Client information text")


class CampaignsUpdateParams(YDBase):
    Campaigns: list[CampaignUpdateItem] = Field(description="List of campaigns to update")


class CampaignsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of update operations")


class CampaignsActionParams(YDBase):
    """Used by delete, suspend, resume, archive, unarchive."""
    SelectionCriteria: IdsCriteria = Field(description="IDs of campaigns to act on")


class CampaignsActionResult(YDBase):
    DeleteResults: list[ActionResult] | None = Field(default=None, description="Results of delete operations")
    SuspendResults: list[ActionResult] | None = Field(default=None, description="Results of suspend operations")
    ResumeResults: list[ActionResult] | None = Field(default=None, description="Results of resume operations")
    ArchiveResults: list[ActionResult] | None = Field(default=None, description="Results of archive operations")
    UnarchiveResults: list[ActionResult] | None = Field(default=None, description="Results of unarchive operations")
