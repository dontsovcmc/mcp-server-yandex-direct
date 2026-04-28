"""Pydantic models for Feeds service."""

from enum import Enum

from .common import YDBase, IdsCriteria, LimitOffset, ActionResult


class FeedStatusEnum(str, Enum):
    ACCEPTED = "ACCEPTED"
    INVALID = "INVALID"
    NEW = "NEW"
    OUTDATED = "OUTDATED"
    UPDATING = "UPDATING"


class FeedsSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class FeedsGetParams(YDBase):
    SelectionCriteria: FeedsSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class FeedGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    BusinessType: str | None = None
    SourceType: str | None = None
    UrlFeed: dict | None = None
    FileFeed: dict | None = None
    Status: str | None = None
    StatusChangeTime: str | None = None
    NumberOfItems: int | None = None


class FeedsGetResult(YDBase):
    Feeds: list[FeedGetItem] | None = None
    LimitedBy: int | None = None


class FeedAddItem(YDBase):
    Name: str
    BusinessType: str | None = None
    SourceType: str | None = None
    UrlFeed: dict | None = None
    FileFeed: dict | None = None


class FeedsAddParams(YDBase):
    Feeds: list[FeedAddItem]


class FeedsAddResult(YDBase):
    AddResults: list[ActionResult]


class FeedUpdateItem(YDBase):
    Id: int
    Name: str | None = None
    UrlFeed: dict | None = None
    FileFeed: dict | None = None


class FeedsUpdateParams(YDBase):
    Feeds: list[FeedUpdateItem]


class FeedsUpdateResult(YDBase):
    UpdateResults: list[ActionResult]


class FeedsDeleteParams(YDBase):
    SelectionCriteria: IdsCriteria


class FeedsDeleteResult(YDBase):
    DeleteResults: list[ActionResult]
