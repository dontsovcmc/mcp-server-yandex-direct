"""Pydantic models for AdVideos service."""

from pydantic import Field

from .common import YDBase, LimitOffset, ActionResult


class AdVideosSelectionCriteria(YDBase):
    Ids: list[int] | None = Field(default=None, description="Filter by ad video IDs")


class AdVideosGetParams(YDBase):
    SelectionCriteria: AdVideosSelectionCriteria = Field(description="Criteria for selecting ad videos")
    FieldNames: list[str] = Field(description="Ad video field names to return")
    Page: LimitOffset | None = Field(default=None, description="Pagination settings")


class AdVideoGetItem(YDBase):
    Id: int | None = Field(default=None, description="Ad video ID")
    Name: str | None = Field(default=None, description="Ad video name")
    Status: str | None = Field(default=None, description="Video processing status")
    PreviewUrl: str | None = Field(default=None, description="URL of the video preview")
    ThumbnailUrl: str | None = Field(default=None, description="URL of the video thumbnail")


class AdVideosGetResult(YDBase):
    AdVideos: list[AdVideoGetItem] | None = Field(default=None, description="List of ad videos matching the criteria")
    LimitedBy: int | None = Field(default=None, description="Indicates next page offset if results were truncated")


class AdVideoAddItem(YDBase):
    Url: str | None = Field(default=None, description="URL of the video to upload")
    Name: str | None = Field(default=None, description="Ad video name")


class AdVideosAddParams(YDBase):
    AdVideos: list[AdVideoAddItem] = Field(description="List of ad videos to add")


class AdVideosAddResult(YDBase):
    AddResults: list[ActionResult] = Field(description="Results of add operations")
