"""Pydantic models for Feeds service."""

from enum import Enum

from pydantic import Field

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class FeedStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    INVALID = "INVALID"
    NEW = "NEW"
    OUTDATED = "OUTDATED"
    UPDATING = "UPDATING"


class FeedsSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Feed IDs to filter by")


class FeedsGetParams(YDBase):
    SelectionCriteria: FeedsSelectionCriteria = Field(description="Criteria for selecting feeds")
    FieldNames: list[str] = Field(description="Names of fields to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class FeedGetItem(YDBase):
    Id: int | None = Field(default=None, description="Feed ID")
    Name: str | None = Field(default=None, description="Feed name")
    BusinessType: str | None = Field(default=None, description="Business type for the feed")
    SourceType: str | None = Field(default=None, description="Feed source type (URL or FILE)")
    UrlFeed: dict | None = Field(default=None, description="URL feed parameters")
    FileFeed: dict | None = Field(default=None, description="File feed parameters")
    Status: str | None = Field(default=None, description="Feed processing status")
    StatusChangeTime: str | None = Field(default=None, description="Time when the status last changed")
    NumberOfItems: int | None = Field(default=None, description="Number of items in the feed")


class FeedsGetResult(YDBase):
    Feeds: list[FeedGetItem] | None = Field(default=None, description="List of feeds")
    LimitedBy: int | None = Field(default=None, description="Offset for the next page if results are truncated")


class FeedAddItem(YDBase):
    Name: str = Field(description="Feed name")
    BusinessType: str | None = Field(default=None, description="Business type for the feed")
    SourceType: str | None = Field(default=None, description="Feed source type (URL or FILE)")
    UrlFeed: dict | None = Field(default=None, description="URL feed parameters")
    FileFeed: dict | None = Field(default=None, description="File feed parameters")


class FeedsAddParams(YDBase):
    Feeds: list[FeedAddItem] = Field(description="Feeds to add")


class FeedsAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of the add operation")


class FeedUpdateItem(YDBase):
    Id: int = Field(description="Feed ID to update")
    Name: str | None = Field(default=None, description="New feed name")
    UrlFeed: dict | None = Field(default=None, description="New URL feed parameters")
    FileFeed: dict | None = Field(default=None, description="New file feed parameters")


class FeedsUpdateParams(YDBase):
    Feeds: list[FeedUpdateItem] = Field(description="Feeds to update")


class FeedsUpdateResult(YDBase):
    UpdateResults: list[ActionResult] = Field(description="Results of the update operation")


class FeedsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria = Field(description="IDs of feeds to delete")


class FeedsDeleteResult(YDBase):
    DeleteResults: list[ActionResult] = Field(description="Results of the delete operation")
