"""Pydantic models for BidModifiers service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class BidModifiersSelectionCriteria(YDBase):
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")
    AdGroupIds: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    Ids: list[int] | None = Field(default=None, description="Filter by bid modifier IDs")
    Types: list[str] | None = Field(default=None, description="Filter by bid modifier types")
    Levels: list[str] | None = Field(default=None, description="Filter by levels (CAMPAIGN or AD_GROUP)")


class BidModifiersGetParams(YDBase):
    SelectionCriteria: BidModifiersSelectionCriteria = Field(description="Criteria for selecting bid modifiers")
    FieldNames: list[str] = Field(description="Bid modifier field names to return")
    DemographicsAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for demographics adjustments")
    RetargetingAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for retargeting adjustments")
    RegionalAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for regional adjustments")
    VideoAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for video adjustments")
    MobileAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for mobile adjustments")
    DesktopAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for desktop adjustments")
    SmartAdAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for smart ad adjustments")
    IncomeGradeAdjustmentFieldNames: list[str] | None = Field(default=None, description="Fields to return for income grade adjustments")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class BidModifierGetItem(YDBase):
    Id: int | None = Field(default=None, description="Bid modifier ID")
    CampaignId: int | None = Field(default=None, description="Campaign ID the modifier belongs to")
    AdGroupId: int | None = Field(default=None, description="Ad group ID the modifier belongs to")
    Type: str | None = Field(default=None, description="Bid modifier type")
    Level: str | None = Field(default=None, description="Level of the modifier (CAMPAIGN or AD_GROUP)")
    DemographicsAdjustment: dict | None = Field(default=None, description="Demographics bid adjustment parameters")
    RetargetingAdjustment: dict | None = Field(default=None, description="Retargeting bid adjustment parameters")
    RegionalAdjustment: dict | None = Field(default=None, description="Regional bid adjustment parameters")
    VideoAdjustment: dict | None = Field(default=None, description="Video bid adjustment parameters")
    MobileAdjustment: dict | None = Field(default=None, description="Mobile device bid adjustment parameters")
    DesktopAdjustment: dict | None = Field(default=None, description="Desktop device bid adjustment parameters")
    SmartAdAdjustment: dict | None = Field(default=None, description="Smart ad bid adjustment parameters")
    IncomeGradeAdjustment: dict | None = Field(default=None, description="Income grade bid adjustment parameters")


class BidModifiersGetResult(YDBase):
    BidModifiers: list[BidModifierGetItem] | None = Field(default=None, description="List of bid modifiers matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class BidModifierAddItem(YDBase):
    CampaignId: int | None = Field(default=None, description="Campaign ID to add the modifier to")
    AdGroupId: int | None = Field(default=None, description="Ad group ID to add the modifier to")
    DemographicsAdjustment: dict | None = Field(default=None, description="Demographics bid adjustment parameters")
    RetargetingAdjustment: dict | None = Field(default=None, description="Retargeting bid adjustment parameters")
    RegionalAdjustment: dict | None = Field(default=None, description="Regional bid adjustment parameters")
    VideoAdjustment: dict | None = Field(default=None, description="Video bid adjustment parameters")
    MobileAdjustment: dict | None = Field(default=None, description="Mobile device bid adjustment parameters")
    DesktopAdjustment: dict | None = Field(default=None, description="Desktop device bid adjustment parameters")
    SmartAdAdjustment: dict | None = Field(default=None, description="Smart ad bid adjustment parameters")
    IncomeGradeAdjustment: dict | None = Field(default=None, description="Income grade bid adjustment parameters")


class BidModifiersAddParams(YDBase):
    BidModifiers: list[BidModifierAddItem] = Field(description="List of bid modifiers to add")


class BidModifiersAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")


class BidModifiersDeleteParams(YDBase):
    SelectionCriteria: dict = Field(description="Selection criteria for bid modifiers to delete")


class BidModifiersDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of delete operations")


class BidModifierSetItem(YDBase):
    Id: int = Field(description="Bid modifier ID to update")
    BidModifier: int = Field(description="New bid modifier coefficient (percent)")


class BidModifiersSetParams(YDBase):
    BidModifiers: list[BidModifierSetItem] = Field(description="List of bid modifiers to set")


class BidModifiersSetResult(YDBase):
    SetResults: list[ActionResult] = Field(description="Results of set operations")
