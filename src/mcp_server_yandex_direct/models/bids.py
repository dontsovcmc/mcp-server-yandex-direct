"""Pydantic models for Bids service."""

from .common import YDBase, LimitOffset, ActionResult


class BidsSelectionCriteria(YDBase):
    KeywordIds: list[int] | None = None
    AdGroupIds: list[int] | None = None
    CampaignIds: list[int] | None = None


class BidsGetParams(YDBase):
    SelectionCriteria: BidsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class BidGetItem(YDBase):
    KeywordId: int | None = None
    AdGroupId: int | None = None
    CampaignId: int | None = None
    Bid: int | None = None
    ContextBid: int | None = None
    CurrentSearchPrice: int | None = None
    MinSearchPrice: int | None = None
    CompetitorsBids: list[dict] | None = None


class BidsGetResult(YDBase):
    Bids: list[BidGetItem] | None = None
    LimitedBy: int | None = None


class BidSetItem(YDBase):
    KeywordId: int
    Bid: int | None = None
    ContextBid: int | None = None


class BidsSetParams(YDBase):
    Bids: list[BidSetItem]


class BidsSetResult(YDBase):
    SetResults: list[ActionResult]


class BidSetAutoItem(YDBase):
    CampaignId: int | None = None
    AdGroupId: int | None = None
    KeywordId: int | None = None


class BidsSetAutoParams(YDBase):
    Bids: list[BidSetAutoItem]


class BidsSetAutoResult(YDBase):
    SetAutoResults: list[ActionResult] | None = None
