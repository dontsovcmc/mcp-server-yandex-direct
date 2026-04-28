"""Pydantic models for AdVideos service."""

from .common import YDBase, LimitOffset, ActionResult


class AdVideosSelectionCriteria(YDBase):
    Ids: list[int] | None = None


class AdVideosGetParams(YDBase):
    SelectionCriteria: AdVideosSelectionCriteria
    FieldNames: list[str]
    Page: LimitOffset | None = None


class AdVideoGetItem(YDBase):
    Id: int | None = None
    Name: str | None = None
    Status: str | None = None
    PreviewUrl: str | None = None
    ThumbnailUrl: str | None = None


class AdVideosGetResult(YDBase):
    AdVideos: list[AdVideoGetItem] | None = None
    LimitedBy: int | None = None


class AdVideoAddItem(YDBase):
    Url: str | None = None
    Name: str | None = None


class AdVideosAddParams(YDBase):
    AdVideos: list[AdVideoAddItem]


class AdVideosAddResult(YDBase):
    AddResults: list[ActionResult]
