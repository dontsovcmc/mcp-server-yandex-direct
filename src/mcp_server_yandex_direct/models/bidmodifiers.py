"""Pydantic models for BidModifiers service."""

from .common import YDBase, LimitOffset, ActionResult


class BidModifiersSelectionCriteria(YDBase):
    CampaignIds: list[int] | None = None
    AdGroupIds: list[int] | None = None
    Ids: list[int] | None = None
    Types: list[str] | None = None
    Levels: list[str] | None = None


class BidModifiersGetParams(YDBase):
    SelectionCriteria: BidModifiersSelectionCriteria
    FieldNames: list[str]
    DemographicsAdjustmentFieldNames: list[str] | None = None
    RetargetingAdjustmentFieldNames: list[str] | None = None
    RegionalAdjustmentFieldNames: list[str] | None = None
    VideoAdjustmentFieldNames: list[str] | None = None
    MobileAdjustmentFieldNames: list[str] | None = None
    DesktopAdjustmentFieldNames: list[str] | None = None
    SmartAdAdjustmentFieldNames: list[str] | None = None
    IncomeGradeAdjustmentFieldNames: list[str] | None = None
    Page: LimitOffset | None = None


class BidModifierGetItem(YDBase):
    Id: int | None = None
    CampaignId: int | None = None
    AdGroupId: int | None = None
    Type: str | None = None
    Level: str | None = None
    DemographicsAdjustment: dict | None = None
    RetargetingAdjustment: dict | None = None
    RegionalAdjustment: dict | None = None
    VideoAdjustment: dict | None = None
    MobileAdjustment: dict | None = None
    DesktopAdjustment: dict | None = None
    SmartAdAdjustment: dict | None = None
    IncomeGradeAdjustment: dict | None = None


class BidModifiersGetResult(YDBase):
    BidModifiers: list[BidModifierGetItem] | None = None
    LimitedBy: int | None = None


class BidModifierAddItem(YDBase):
    CampaignId: int | None = None
    AdGroupId: int | None = None
    DemographicsAdjustment: dict | None = None
    RetargetingAdjustment: dict | None = None
    RegionalAdjustment: dict | None = None
    VideoAdjustment: dict | None = None
    MobileAdjustment: dict | None = None
    DesktopAdjustment: dict | None = None
    SmartAdAdjustment: dict | None = None
    IncomeGradeAdjustment: dict | None = None


class BidModifiersAddParams(YDBase):
    BidModifiers: list[BidModifierAddItem]


class BidModifiersAddResult(YDBase):
    AddResults: list[ActionResult]


class BidModifiersDeleteParams(YDBase):
    SelectionCriteria: dict


class BidModifiersDeleteResult(YDBase):
    DeleteResults: list[ActionResult]


class BidModifierSetItem(YDBase):
    Id: int
    BidModifier: int


class BidModifiersSetParams(YDBase):
    BidModifiers: list[BidModifierSetItem]


class BidModifiersSetResult(YDBase):
    SetResults: list[ActionResult]
