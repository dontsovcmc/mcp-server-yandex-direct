"""Pydantic models for Bids service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class BidsSelectionCriteria(YDBase):
    KeywordIds: list[int] | None = Field(default=None, description="Filter by keyword IDs")
    AdGroupIds: list[int] | None = Field(default=None, description="Filter by ad group IDs")
    CampaignIds: list[int] | None = Field(default=None, description="Filter by campaign IDs")


class BidsGetParams(YDBase):
    SelectionCriteria: BidsSelectionCriteria = Field(description="Criteria for selecting bids")
    FieldNames: list[str] = Field(description="Bid field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class BidGetItem(YDBase):
    KeywordId: int | None = Field(default=None, description="Keyword ID the bid belongs to")
    AdGroupId: int | None = Field(default=None, description="Ad group ID")
    CampaignId: int | None = Field(default=None, description="Campaign ID")
    Bid: int | None = Field(default=None, description="Search bid in currency units (micros)")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")
    CurrentSearchPrice: int | None = Field(default=None, description="Current CPC on search in currency units (micros)")
    MinSearchPrice: int | None = Field(default=None, description="Minimum CPC on search in currency units (micros)")
    CompetitorsBids: list[dict] | None = Field(default=None, description="Competitors' bid information")


class BidsGetResult(YDBase):
    Bids: list[BidGetItem] | None = Field(default=None, description="List of bids matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class BidSetItem(YDBase):
    KeywordId: int = Field(description="Keyword ID to set the bid for")
    Bid: int | None = Field(default=None, description="Search bid in currency units (micros)")
    ContextBid: int | None = Field(default=None, description="Network bid in currency units (micros)")


class BidsSetParams(YDBase):
    Bids: list[BidSetItem] = Field(description="List of bids to set")


class BidsSetResult(YDBase):
    SetResults: list[ActionResult] = Field(description="Results of set operations")


class BidSetAutoItem(YDBase):
    CampaignId: int | None = Field(default=None, description="Campaign ID for auto-bid scope")
    AdGroupId: int | None = Field(default=None, description="Ad group ID for auto-bid scope")
    KeywordId: int | None = Field(default=None, description="Keyword ID for auto-bid scope")


class BidsSetAutoParams(YDBase):
    Bids: list[BidSetAutoItem] = Field(description="List of items to set auto bids for")


class BidsSetAutoResult(YDBase):
    SetAutoResults: list[ActionResult] | None = Field(default=None, description="Results of set auto operations")
